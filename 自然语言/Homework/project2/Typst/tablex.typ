// Welcome to tablex!
// Feel free to contribute with any features you think are missing.

// -- table counter --

#let _tablex-table-counter = counter("_tablex-table-counter")

// -- compat --

#let calc-mod(a, b) = {
  calc.floor(a) - calc.floor(b * calc.floor(a / b))
}

// ------------

// -- types --

#let hlinex(
    start: 0, end: auto, y: auto,
    stroke: auto,
    stop-pre-gutter: auto, gutter-restrict: none,
    stroke-expand: true,
    expand: none
) = (
    tablex-dict-type: "hline",
    start: start,
    end: end,
    y: y,
    stroke: stroke,
    stop-pre-gutter: stop-pre-gutter,
    gutter-restrict: gutter-restrict,
    stroke-expand: stroke-expand,
    expand: expand,
    parent: none,  // if hline was broken into multiple
)

#let vlinex(
    start: 0, end: auto, x: auto,
    stroke: auto,
    stop-pre-gutter: auto, gutter-restrict: none,
    stroke-expand: true,
    expand: none
) = (
    tablex-dict-type: "vline",
    start: start,
    end: end,
    x: x,
    stroke: stroke,
    stop-pre-gutter: stop-pre-gutter,
    gutter-restrict: gutter-restrict,
    stroke-expand: stroke-expand,
    expand: expand,
    parent: none,
)

#let cellx(content,
    x: auto, y: auto,
    rowspan: 1, colspan: 1,
    fill: auto, align: auto,
    inset: auto
) = (
    tablex-dict-type: "cell",
    content: content,
    rowspan: rowspan,
    colspan: colspan,
    align: align,
    fill: fill,
    inset: inset,
    x: x,
    y: y,
)

#let occupied(x: 0, y: 0, parent_x: none, parent_y: none) = (
    tablex-dict-type: "occupied",
    x: x,
    y: y,
    parent_x: parent_x,
    parent_y: parent_y
)

// -- end: types --

// -- type checks, transformers and validators --

// Is this a valid dict created by this library?
#let is-tablex-dict(x) = (
    type(x) == "dictionary"
        and "tablex-dict-type" in x
)

#let is-tablex-dict-type(x, ..dict_types) = (
    is-tablex-dict(x)
        and x.tablex-dict-type in dict_types.pos()
)

#let is-tablex-cell(x) = is-tablex-dict-type(x, "cell")
#let is-tablex-hline(x) = is-tablex-dict-type(x, "hline")
#let is-tablex-vline(x) = is-tablex-dict-type(x, "vline")
#let is-some-tablex-line(x) = is-tablex-dict-type(x, "hline", "vline")
#let is-tablex-occupied(x) = is-tablex-dict-type(x, "occupied")

#let table-item-convert(item, keep_empty: true) = {
    if type(item) == "function" {  // dynamic cell content
        cellx(item)
    } else if keep_empty and item == () {
        item
    } else if type(item) != "dictionary" or "tablex-dict-type" not in item {
        cellx[#item]
    } else {
        item
    }
}

#let rowspanx(length, content, ..cell_options) = {
    if is-tablex-cell(content) {
        (..content, rowspan: length, ..cell_options.named())
    } else {
        cellx(
            content,
            rowspan: length,
            ..cell_options.named())
    }
}

#let colspanx(length, content, ..cell_options) = {
    if is-tablex-cell(content) {
        (..content, colspan: length, ..cell_options.named())
    } else {
        cellx(
            content,
            colspan: length,
            ..cell_options.named())
    }
}

// Get expected amount of cell positions
// in the table (considering colspan and rowspan)
#let get-expected-grid-len(items, col_len: 0) = {
    let len = 0

    // maximum explicit 'y' specified
    let max_explicit_y = items
        .filter(c => c.y != auto)
        .fold(0, (acc, cell) => {
            if (is-tablex-cell(cell)
                    and type(cell.y) in ("integer", "float")
                    and cell.y > acc) {
                cell.y
            } else {
                acc
            }
        })

    for item in items {
        if is-tablex-cell(item) and item.x == auto and item.y == auto {
            // cell occupies (colspan * rowspan) spaces
            len += item.colspan * item.rowspan
        } else if type(item) == "content" {
            len += 1
        }
    }

    let rows(len) = calc.ceil(len / col_len)

    while rows(len) < max_explicit_y {
        len += col_len
    }

    len
}

#let validate-cols-rows(columns, rows, items: ()) = {
    if type(columns) == "integer" {
        assert(columns >= 0, message: "Error: Cannot have a negative amount of columns.")

        columns = (auto,) * columns
    }

    if type(rows) == "integer" {
        assert(rows >= 0, message: "Error: Cannot have a negative amount of rows.")
        rows = (auto,) * rows
    }

    if type(columns) != "array" {
        columns = (columns,)
    }
    
    if type(rows) != "array" {
        rows = (rows,)
    }

    // default empty column to a single auto column
    if columns.len() == 0 {
        columns = (auto,)
    }

    // default empty row to a single auto row
    if rows.len() == 0 {
        rows = (auto,)
    }

    let col_row_is_valid(col_row) = (
        col_row == auto or type(col_row) in (
            "fraction", "length", "relative length", "ratio"
            )
    )

    if not columns.all(col_row_is_valid) {
        panic("Invalid column sizes (must all be 'auto' or a valid length specifier).")
    }

    if not rows.all(col_row_is_valid) {
        panic("Invalid row sizes (must all be 'auto' or a valid length specifier).")
    }

    let col_len = columns.len()

    let grid_len = get-expected-grid-len(items, col_len: col_len)

    let expected_rows = calc.ceil(grid_len / col_len)

    // more cells than expected => add rows
    if rows.len() < expected_rows {
        let missing_rows = expected_rows - rows.len()

        rows += (rows.last(),) * missing_rows
    }

    let new_items = ()

    let is_at_first_column(grid_len) = calc-mod(grid_len, col_len) == 0

    while not is_at_first_column(get-expected-grid-len(items + new_items, col_len: col_len)) {  // fix incomplete rows
        new_items.push(cellx[])
    }

    (columns: columns, rows: rows, items: new_items)
}

// -- end: type checks and validators --

// -- utility functions --

// Which positions does a cell occupy
// (Usually just its own, but increases if colspan / rowspan
// is greater than 1)
#let positions-spanned-by(cell, x: 0, y: 0, x_limit: 0, y_limit: none) = {
    let result = ()
    let rowspan = if "rowspan" in cell { cell.rowspan } else { 1 }
    let colspan = if "colspan" in cell { cell.colspan } else { 1 }

    if rowspan < 1 {
        panic("Cell rowspan must be 1 or greater (bad cell: " + repr((x, y)) + ")")
    } else if colspan < 1 {
        panic("Cell colspan must be 1 or greater (bad cell: " + repr((x, y)) + ")")
    }

    let max_x = x + colspan
    let max_y = y + rowspan

    if x_limit != none {
        max_x = calc.min(x_limit, max_x)
    }

    if y_limit != none {
        max_y = calc.min(y_limit, max_y)
    }

    for x in range(x, max_x) {
        for y in range(y, max_y) {
            result.push((x, y))
        }
    }

    result
}

// initialize an array with a certain element or init function, repeated
#let init-array(amount, element: none, init_function: none) = {
    let nones = ()

    if init_function == none {
        init_function = () => element
    }

    range(amount).map(i => init_function())
}

// Default 'x' to a certain value if it is equal to the forbidden value
// ('none' by default)
#let default-if-not(x, default, if_isnt: none) = {
    if x == if_isnt {
        default
    } else {
        x
    }
}

// Default 'x' to a certain value if it is none
#let default-if-none(x, default) = default-if-not(x, default, if_isnt: none)

// Default 'x' to a certain value if it is auto
#let default-if-auto(x, default) = default-if-not(x, default, if_isnt: auto)

// Default 'x' to a certain value if it is auto or none
#let default-if-auto-or-none(x, default) = if x in (auto, none) {
    default
} else {
    x
}

// The max between a, b, or the other one if either is 'none'.
#let max-if-not-none(a, b) = if a in (none, auto) {
    b
} else if b in (none, auto) {
    a
} else {
    calc.max(a, b)
}

// Backwards-compatible enumerate
#let enumerate(arr) = {
    if type(arr) != "array" {
        return arr
    }

    let new-arr = ()
    let i = 0

    for x in arr {
        new-arr.push((i, x))

        i += 1
    }

    new-arr
}

// Gets the topmost parent of a line.
#let get-top-parent(line) = {
    let previous = none
    let current = line

    while current != none {
        previous = current
        current = previous.parent
    }

    previous
}

// Convert a certain (non-relative) length to pt
//
// styles: from style()
// page_size: equivalent to 100%
// frac_amount: amount of 'fr' specified
// frac_total: total space shared by fractions
#let convert-length-to-pt(
    len,
    styles: none, page_size: none, frac_amount: none, frac_total: none
) = {
    page_size = 0pt + page_size

    if type(len) == "length" {
        if "em" in repr(len) {
            if styles == none {
                panic("Cannot convert length to pt ('styles' not specified).")
            }

            measure(line(length: len), styles).width + 0pt
        } else {
            len + 0pt  // mm, in, pt
        }
    } else if type(len) == "ratio" {
        if page_size == none {
            panic("Cannot convert ratio to pt ('page_size' not specified).")
        }

        ((len / 1%) / 100) * page_size + 0pt  // e.g. 100% / 1% = 100; / 100 = 1; 1 * page_size
    } else if type(len) == "fraction" {
        if frac_amount == none {
            panic("Cannot convert fraction to pt ('frac_amount' not specified).")
        }

        if frac_total == none {
            panic("Cannot convert fraction to pt ('frac_total' not specified).")
        }

        if frac_amount <= 0 {
            return 0pt
        }

        let len_per_frac = frac_total / frac_amount

        (len_per_frac * (len / 1fr)) + 0pt
    } else if type(len) == "relative length" {
        if styles == none {
            panic("Cannot convert relative length to pt ('styles' not specified).")
        }

        let ratio_regex = regex("^\\d+%")
        let ratio = repr(len).find(ratio_regex)

        if ratio == none {  // 2em + 5pt  (doesn't contain 100% or something)
            measure(line(length: len), styles).width
        } else {  // 100% + 2em + 5pt  --> extract the "100%" part
            if page_size == none {
                panic("Cannot convert relative length to pt ('page_size' not specified).")
            }

            // SAFETY: guaranteed to be a ratio by regex
            let ratio_part = eval(ratio)
            assert(type(ratio_part) == "ratio", message: "Eval didn't return a ratio")

            let other_part = len - ratio_part  // get the (2em + 5pt) part

            let ratio_part_pt = ((ratio_part / 1%) / 100) * page_size
            let other_part_pt = 0pt

            if other_part < 0pt {
                other_part_pt = -measure(line(length: -other_part), styles).width
            } else {
                other_part_pt = measure(line(length: other_part), styles).width
            }

            ratio_part_pt + other_part_pt + 0pt
        }
    } else {
        panic("Cannot convert '" + type(len) + "' to length.")
    }
}

// Convert a stroke to its thickness
#let stroke-len(stroke, stroke-auto: 1pt) = {
    let stroke = default-if-auto(stroke, stroke-auto)
    if type(stroke) in ("length", "relative length") {
        stroke
    } else if type(stroke) == "color" {
        1pt
    } else if type(stroke) == "stroke" {  // 2em + blue
        let r = regex("^\\d+(?:em|pt|cm|in|%)")
        let s = repr(stroke).find(r)

        if s == none {
        1pt
        } else {
        eval(s)
        }
    } else if type(stroke) == "dictionary" and "thickness" in stroke {
        stroke.thickness
    } else {
        1pt
    }
}

// --- end: utility functions ---


// --- grid functions ---

#let create-grid(width, initial_height) = (
    tablex-dict-type: "grid",
    items: init-array(width * initial_height),
    width: width
)

#let is-tablex-grid(value) = is-tablex-dict-type("grid")

// Gets the index of (x, y) in a grid's array.
#let grid-index-at(x, y, grid: none, width: none) = {
    width = default-if-none(grid, (width: width)).width
    width = calc.floor(width)
    (y * width) + calc-mod(x, width)
}

// Gets the cell at the given grid x, y position.
// Width (amount of columns) per line must be known.
// E.g. grid-at(grid, 5, 2, width: 7)  => 5th column, 2nd row  (7 columns per row)
#let grid-at(grid, x, y) = {
    let index = grid-index-at(x, y, width: grid.width)

    if index < grid.items.len() {
        grid.items.at(index)
    } else {
        none
    }
}

// Returns 'true' if the cell at (x, y)
// exists in the grid.
#let grid-has-pos(grid, x, y) = (
    grid-index-at(x, y, grid: grid) < grid.items.len()
)

// How many rows are in this grid? (Given its width)
#let grid-count-rows(grid) = (
    calc.floor(grid.items.len() / grid.width)
)

// Converts a grid array index to (x, y)
#let grid-index-to-pos(grid, index) = (
    (calc-mod(index, grid.width), calc.floor(index / grid.width))   
)

// Fetches an entire row of cells (all positions with the given y).
#let grid-get-row(grid, y) = {
    range(grid.width).map(x => grid-at(grid, x, y))
}

// Fetches an entire column of cells (all positions with the given x).
#let grid-get-column(grid, x) = {
    range(grid-count-rows(grid)).map(y => grid-at(grid, x, y))
}

// Expand grid to the given coords (add the missing cells)
#let grid-expand-to(grid, x, y, fill_with: (grid) => none) = {
    let rows = grid-count-rows(grid)
    let rowws = rows

    // quickly add missing rows
    while rows < y {
        grid.items += (fill_with(grid),) * grid.width
        rows += 1
    }

    let now = grid-index-to-pos(grid, grid.items.len() - 1)
    // now columns and/or last missing row
    while not grid-has-pos(grid, x, y) {
        grid.items.push(fill_with(grid))
    }
    let new = grid-index-to-pos(grid, grid.items.len() - 1)

    grid
}

// if occupied (extension of a cell) => get the cell that generated it.
// if a normal cell => return it, untouched.
#let get-parent-cell(cell, grid: none) = {
    if is-tablex-occupied(cell) {
        grid-at(grid, cell.parent_x, cell.parent_y)
    } else if is-tablex-cell(cell) {
        cell
    } else {
        panic("Cannot get parent table cell of a non-cell object: " + repr(cell))
    }
}

// Return the next position available on the grid
#let next-available-position(
    grid, x: 0, y: 0, x_limit: 0, y_limit: 0
) = {
    let cell = (x, y)
    let there_is_next(cell_pos) = {
        let grid_cell = grid-at(grid, ..cell_pos)
        grid_cell != none
    }

    while there_is_next(cell) {
        x += 1

        if x >= x_limit {
            x = 0
            y += 1
        }

        cell = (x, y)

        if y >= y_limit {  // last row reached - stop
            break
        }
    }

    cell
}

// Organize cells in a grid from the given items,
// and also get all given lines
#let generate-grid(items, x_limit: 0, y_limit: 0, map-cells: c => c) = {
    // init grid as a matrix
    // y_limit  x   x_limit
    let grid = create-grid(x_limit, y_limit)

    let grid-index-at = grid-index-at.with(width: x_limit)

    let hlines = ()
    let vlines = ()

    let prev_x = 0
    let prev_y = 0

    let x = 0
    let y = 0

    let first_cell_reached = false  // if true, hline should always be placed after the current row
    let row_wrapped = false  // if true, a vline should be added to the end of a row

    let range_of_items = range(items.len())

    let new_empty_cell(grid, index: auto) = {
        let empty_cell = cellx[]
        let index = default-if-auto(index, grid.items.len())
        let new_cell_pos = grid-index-to-pos(grid, index)
        empty_cell.x = new_cell_pos.at(0)
        empty_cell.y = new_cell_pos.at(1)

        empty_cell
    }

    // go through all input
    for i in range_of_items {
        let item = items.at(i)

        // allow specifying () to change vline position
        if type(item) == "array" and item.len() == 0 {
            if x == 0 and y == 0 {  // increment vline's secondary counter
                prev_x += 1
            }

            continue  // ignore all '()'
        }

        let item = table-item-convert(item)


        if is-some-tablex-line(item) {  // detect lines' x, y
            if is-tablex-hline(item) {
                let this_y = if first_cell_reached {
                    prev_y + 1
                } else {
                    prev_y
                }

                item.y = default-if-auto(item.y, this_y)

                hlines.push(item)
            } else if is-tablex-vline(item) {
                if item.x == auto {
                    if x == 0 and y == 0 {  // placed before any elements
                        item.x = prev_x
                        prev_x += 1  // use this as a 'secondary counter'
                                     // in the meantime

                        if prev_x > x_limit + 1 {
                            panic("Error: Specified way too many vlines or empty () cells before the first row of the table. (Note that () is used to separate vline()s at the beginning of the table.)  Please specify at most " + str(x_limit + 1) + " empty cells or vlines before the first cell of the table.")
                        }
                    } else if row_wrapped {
                        item.x = x_limit  // allow v_line at the last column
                        row_wrapped = false
                    } else {
                        item.x = x
                    }
                }

                vlines.push(item)
            } else {
                panic("Invalid line received (must be hline or vline).")
            }
            items.at(i) = item  // override item with the new x / y coord set
            continue
        }

        let cell = item

        assert(is-tablex-cell(cell), message: "All table items must be cells or lines.")

        first_cell_reached = true

        let this_x = default-if-auto(cell.x, x)
        let this_y = default-if-auto(cell.y, y)

        if cell.x == none or cell.y == none {
            panic("Error: Received cell with 'none' as x or y.")
        }

        if this_x == none or this_y == none {
            panic("Internal tablex error: Grid wasn't large enough to fit the given cells. (Previous position: " + repr((prev_x, prev_y)) + ", new cell: " + repr(cell) + ")")
        }

        cell.x = this_x
        cell.y = this_y
        cell = table-item-convert(map-cells(cell))

        assert(is-tablex-cell(cell), message: "Tablex error: 'map-cells' returned something that isn't a valid cell.")

        if row_wrapped {
            row_wrapped = false
        }

        let content = cell.content
        let content = if type(content) == "function" {
            let res = content(this_x, this_y)
            if is-tablex-cell(res) {
                cell = res
                this_x = cell.x
                this_y = cell.y
                [#res.content]
            } else {
                [#res]
            }
        } else {
            [#content]
        }

        if this_x == none or this_y == none {
            panic("Error: Cell with function as content returned another cell with 'none' as x or y!")
        }

        if type(this_x) != "integer" or type(this_y) != "integer" {
            panic("Error: Cell coordinates must be integers. Invalid pair: " + repr((this_x, this_y)))
        }

        cell.content = content

        // up to which 'y' does this cell go
        let max_x = this_x + cell.colspan - 1
        let max_y = this_y + cell.rowspan - 1

        if this_x >= x_limit {
            panic("Error: Cell at " + repr((this_x, this_y)) + " is placed at an inexistent column.")
        }

        if max_x >= x_limit {
            panic("Error: Cell at " + repr((this_x, this_y)) + " has a colspan of " + repr(cell.colspan) + ", which would exceed the available columns.")
        }

        let cell_positions = positions-spanned-by(cell, x: this_x, y: this_y, x_limit: x_limit, y_limit: none)

        for position in cell_positions {
            let px = position.at(0)
            let py = position.at(1)
            let currently_there = grid-at(grid, px, py)

            if currently_there != none {
                let parent_cell = get-parent-cell(currently_there, grid: grid)

                panic("Error: Multiple cells attempted to occupy the cell position at " + repr((px, py)) + ": one starting at " + repr((this_x, this_y)) + ", and one starting at " + repr((parent_cell.x, parent_cell.y)))
            }

            // initial position => assign it to the cell's x/y
            if position == (this_x, this_y) {
                cell.x = this_x
                cell.y = this_y

                // expand grid to allow placing this cell (including colspan / rowspan)
                let grid_expand_res = grid-expand-to(grid, grid.width - 1, max_y)

                grid = grid_expand_res
                y_limit = grid-count-rows(grid)

                let index = grid-index-at(this_x, this_y)

                if index > grid.items.len() {
                    panic("Internal tablex error: Could not expand grid to include cell at " + repr((this_x, this_y)))
                }
                grid.items.at(index) = cell
                items.at(i) = cell

            // other secondary position (from colspan / rowspan)
            } else {
                let index = grid-index-at(px, py)

                grid.items.at(index) = occupied(x: px, y: py, parent_x: this_x, parent_y: this_y)  // indicate this position's parent cell (to join them later)
            }
        }

        let next_pos = next-available-position(grid, x: this_x, y: this_y, x_limit: x_limit, y_limit: y_limit)

        prev_x = this_x
        prev_y = this_y

        x = next_pos.at(0)
        y = next_pos.at(1)

        if prev_y != y {
            row_wrapped = true  // we changed rows!
        }
    }

    // for missing cell positions: add empty cell
    for index_item in enumerate(grid.items) {
        let index = index_item.at(0)
        let item = index_item.at(1)
        if item == none {
            grid.items.at(index) = new_empty_cell(grid, index: index)
        }
    }

    // while there are incomplete rows for some reason, add empty cells
    while calc-mod(grid.items.len(), grid.width) != 0 {
        grid.items.push(new_empty_cell(grid))
    }

    (
        grid: grid,
        items: grid.items,
        hlines: hlines,
        vlines: vlines,
        new_row_count: grid-count-rows(grid)
    )
}

// -- end: grid functions --

// -- col/row size functions --

// Makes a cell's box, using the given options
// cell - The cell data (including content)
// width, height - The cell's dimensions
// inset - The table's inset
// align_default - The default alignment if the cell doesn't specify one
// fill_default - The default fill color / etc if the cell doesn't specify one
#let make-cell-box(
        cell,
        width: 0pt, height: 0pt, inset: 5pt,
        align_default: left,
        fill_default: none) = {

    let align_default = if type(align_default) == "function" {
        align_default(cell.x, cell.y)  // column, row
    } else {
        align_default
    }

    let fill_default = if type(fill_default) == "function" {
        fill_default(cell.x, cell.y)  // row, column
    } else {
        fill_default
    }

    let content = cell.content

    let inset = default-if-auto(cell.inset, inset)

    // use default align (specified in
    // table 'align:')
    // when the cell align is 'auto'
    let cell_align = default-if-auto(cell.align, align_default)

    // same here for fill
    let cell_fill = default-if-auto(cell.fill, fill_default)

    if cell_align != auto and type(cell_align) not in ("alignment", "2d alignment") {
        panic("Invalid alignment specified (must be either a function (row, column) -> alignment, an alignment value - such as 'left' or 'center + top' -, or 'auto').")
    }

    let aligned_cell_content = if cell_align == auto {
        [#content]
    } else {
        align(cell_align)[#content]
    }

    box(
        width: width, height: height,
        inset: inset, fill: cell_fill,
        // avoid #set problems
        baseline: 0pt,
        outset: 0pt, radius: 0pt, stroke: none,
        aligned_cell_content)
}

// Sums the sizes of fixed-size tracks (cols/rows). Anything else
// (auto, 1fr, ...) is ignored.
#let sum-fixed-size-tracks(tracks) = {
    tracks.fold(0pt, (acc, el) => {
        if type(el) == "length" {
            acc + el
        } else {
            acc
        }
    })
}

// Calculate the size of fraction tracks (cols/rows) (1fr, 2fr, ...),
// based on the remaining sizes (after fixed-size and auto columns)
#let determine-frac-tracks(tracks, remaining: 0pt, gutter: none) = {
    let frac-tracks = enumerate(tracks).filter(t => type(t.at(1)) == "fraction")

    let amount-frac = frac-tracks.fold(0, (acc, el) => acc + (el.at(1) / 1fr))

    if type(gutter) == "fraction" {
        amount-frac += (gutter / 1fr) * (tracks.len() - 1)
    }

    let frac-width = if amount-frac > 0 {
        remaining / amount-frac
    } else {
        0pt
    }

    if type(gutter) == "fraction" {
        gutter = frac-width * (gutter / 1fr)
    }

    for i_size in frac-tracks {
        let i = i_size.at(0)
        let size = i_size.at(1)

        tracks.at(i) = frac-width * (size / 1fr)
    }

    (tracks: tracks, gutter: gutter)
}

// Gets the last (rightmost) auto column a cell is inserted in, for
// due expansion
#let get-colspan-last-auto-col(cell, columns: none) = {
    let cell_cols = range(cell.x, cell.x + cell.colspan)
    let last_auto_col = none

    for i_col in enumerate(columns).filter(i_col => i_col.at(0) in cell_cols) {
        let i = i_col.at(0)
        let col = i_col.at(1)

        if col == auto {
            last_auto_col = max-if-not-none(last_auto_col, i)
        }
    }

    last_auto_col
}

// Gets the last (bottom-most) auto row a cell is inserted in, for
// due expansion
#let get-rowspan-last-auto-row(cell, rows: none) = {
    let cell_rows = range(cell.y, cell.y + cell.rowspan)
    let last_auto_row = none

    for i_row in enumerate(rows).filter(i_row => i_row.at(0) in cell_rows) {
        let i = i_row.at(0)
        let row = i_row.at(1)

        if row == auto {
            last_auto_row = max-if-not-none(last_auto_row, i)
        }
    }

    last_auto_row
}

// Given a cell that may span one or more columns, sums the
// sizes of the columns it spans, when those columns have fixed sizes.
// Useful to subtract from the total width to find out how much more
// should an auto column extend to have that cell fit in the table.
#let get-colspan-fixed-size-covered(cell, columns: none) = {
    let cell_cols = range(cell.x, cell.x + cell.colspan)
    let size = 0pt

    for i_col in enumerate(columns).filter(i_col => i_col.at(0) in cell_cols) {
        let i = i_col.at(0)
        let col = i_col.at(1)

        if type(col) == "length" {
            size += col
        }
    }
    size
}

// Given a cell that may span one or more rows, sums the
// sizes of the rows it spans, when those rows have fixed sizes.
// Useful to subtract from the total height to find out how much more
// should an auto row extend to have that cell fit in the table.
#let get-rowspan-fixed-size-covered(cell, rows: none) = {
    let cell_rows = range(cell.y, cell.y + cell.rowspan)
    let size = 0pt

    for i_row in enumerate(rows).filter(i_row => i_row.at(0) in cell_rows) {
        let i = i_row.at(0)
        let row = i_row.at(1)

        if type(row) == "length" {
            size += row
        }
    }
    size
}

// calculate the size of auto columns (based on the max width of their cells)
#let determine-auto-columns(grid: (), styles: none, columns: none, inset: none) = {
    assert(styles != none, message: "Cannot measure auto columns without styles")
    let total_auto_size = 0pt
    let auto_sizes = ()
    let new_columns = columns

    for i_col in enumerate(columns) {
        let i = i_col.at(0)
        let col = i_col.at(1)

        if col == auto {
            // max cell width
            let col_size = grid-get-column(grid, i)
                .fold(0pt, (max, cell) => {
                    if cell == none {
                        panic("Not enough cells specified for the given amount of rows and columns.")
                    }

                    let pcell = get-parent-cell(cell, grid: grid)  // in case this is a colspan
                    let last_auto_col = get-colspan-last-auto-col(pcell, columns: columns)

                    // only expand the last auto column of a colspan,
                    // and only the amount necessary that isn't already
                    // covered by fixed size columns.
                    if last_auto_col == i {
                        // take extra inset as extra width or height on 'auto'
                        let cell_inset = default-if-auto(pcell.inset, inset)

                        let cell_inset = convert-length-to-pt(cell_inset, styles: styles)

                        let width = measure(pcell.content, styles).width + 2*cell_inset
                        let fixed_size = get-colspan-fixed-size-covered(pcell, columns: columns)

                        calc.max(max, width - fixed_size, 0pt)
                    } else {
                        max
                    }
                })

            total_auto_size += col_size
            auto_sizes.push((i, col_size))
            new_columns.at(i) = col_size
        }
    }

    (total: total_auto_size, sizes: auto_sizes, columns: new_columns)
}

#let fit-auto-columns(available: 0pt, auto_cols: none, columns: none) = {
    let remaining = available
    let auto_cols_remaining = auto_cols.len()

    if auto_cols_remaining <= 0 {
        return columns
    }

    let fair_share = remaining / auto_cols_remaining

    for i_col in auto_cols {
        let i = i_col.at(0)
        let col = i_col.at(1)

        auto_cols_remaining -= 1

        if auto_cols_remaining <= 0 {
            return columns  // no more to share
        }

        if col < fair_share {  // ok, keep your size, it's less than the limit
            remaining -= col
            fair_share = remaining / auto_cols_remaining
        } else {  // you surpassed the limit!!!
            remaining -= fair_share
            columns.at(i) = fair_share
        }
    }

    columns
}

#let determine-column-sizes(grid: (), page_width: 0pt, styles: none, columns: none, inset: none, col-gutter: none) = {
    let columns = columns.map(c => {
        if type(c) in ("length", "relative length", "ratio") {
            convert-length-to-pt(c, styles: styles, page_size: page_width)
        } else if c == none {
            0pt
        } else {
            c
        }
    })

    // what is the fixed size of the gutter?
    // (calculate it later if it's fractional)
    let fixed-size-gutter = if type(col-gutter) == "length" {
        col-gutter
    } else {
        0pt
    }

    let total_fixed_size = sum-fixed-size-tracks(columns) + fixed-size-gutter * (columns.len() - 1)

    let available_size = page_width - total_fixed_size

    // page_width == 0pt => page width is 'auto'
    // so we don't have to restrict our table's size
    if available_size >= 0pt or page_width == 0pt {
        let auto_cols_result = determine-auto-columns(grid: grid, styles: styles, columns: columns, inset: inset)
        let total_auto_size = auto_cols_result.total
        let auto_sizes = auto_cols_result.sizes
        columns = auto_cols_result.columns

        let remaining_size = available_size - total_auto_size
        if remaining_size >= 0pt {
            let frac_res = determine-frac-tracks(
                columns,
                remaining: remaining_size,
                gutter: col-gutter
            )

            columns = frac_res.tracks
            fixed-size-gutter = frac_res.gutter
        } else {
            // don't shrink on width 'auto'
            if page_width != 0pt {
                columns = fit-auto-columns(
                    available: available_size,
                    auto_cols: auto_sizes,
                    columns: columns
                )
            }

            columns = columns.map(c => {
                if type(c) == "fraction" {
                    0pt  // no space left to be divided
                } else {
                    c
                }
            })
        }
    } else {
        columns = columns.map(c => {
            if c == auto or type(c) == "fraction" {
                0pt  // no space remaining!
            } else {
                c
            }
        })
    }

    (
        columns: columns,
        gutter: if col-gutter == none {
            none
        } else {
            fixed-size-gutter
        }
    )
}

// calculate the size of auto rows (based on the max height of their cells)
#let determine-auto-rows(grid: (), styles: none, columns: none, rows: none, align: auto, inset: none) = {
    assert(styles != none, message: "Cannot measure auto rows without styles")
    let total_auto_size = 0pt
    let auto_sizes = ()
    let new_rows = rows

    for i_row in enumerate(rows) {
        let i = i_row.at(0)
        let row = i_row.at(1)

        if row == auto {
            // max cell height
            let row_size = grid-get-row(grid, i)
                .fold(0pt, (max, cell) => {
                    if cell == none {
                        panic("Not enough cells specified for the given amount of rows and columns.")
                    }

                    let pcell = get-parent-cell(cell, grid: grid)  // in case this is a rowspan
                    let last_auto_row = get-rowspan-last-auto-row(pcell, rows: rows)

                    // only expand the last auto row of a rowspan,
                    // and only the amount necessary that isn't already
                    // covered by fixed size rows.
                    if last_auto_row == i {
                        let width = get-colspan-fixed-size-covered(pcell, columns: columns)

                        // take extra inset as extra width or height on 'auto'
                        let cell_inset = default-if-auto(pcell.inset, inset)

                        let cell_inset = convert-length-to-pt(cell_inset, styles: styles)

                        let cell-box = make-cell-box(
                            pcell,
                            width: width, height: auto,
                            inset: cell_inset, align_default: align
                        )

                        // measure the cell's actual height,
                        // with its calculated width
                        // and with other constraints
                        let height = measure(cell-box, styles).height// + 2*cell_inset (box already considers inset)
                        let fixed_size = get-rowspan-fixed-size-covered(pcell, rows: rows)

                        calc.max(max, height - fixed_size, 0pt)
                    } else {
                        max
                    }
                })

            total_auto_size += row_size
            auto_sizes.push((i, row_size))
            new_rows.at(i) = row_size
        }
    }

    (total: total_auto_size, sizes: auto_sizes, rows: new_rows)
}

#let determine-row-sizes(grid: (), page_height: 0pt, styles: none, columns: none, rows: none, align: auto, inset: none, row-gutter: none) = {
    let rows = rows.map(r => {
        if type(r) in ("length", "relative length", "ratio") {
            convert-length-to-pt(r, styles: styles, page_size: page_height)
        } else {
            r
        }
    })

    let auto_rows_res = determine-auto-rows(
        grid: grid, columns: columns, rows: rows, styles: styles, align: align, inset: inset
    )

    let auto_size = auto_rows_res.total
    rows = auto_rows_res.rows

    // what is the fixed size of the gutter?
    // (calculate it later if it's fractional)
    let fixed-size-gutter = if type(row-gutter) == "length" {
        row-gutter
    } else {
        0pt
    }

    let remaining = page_height - sum-fixed-size-tracks(rows) - auto_size - fixed-size-gutter * (rows.len() - 1)

    if remaining >= 0pt {  // split fractions in one page
        let frac_res = determine-frac-tracks(rows, remaining: remaining, gutter: row-gutter)
        (
            rows: frac_res.tracks,
            gutter: frac_res.gutter
        )
    } else {
        (
            rows: rows.map(r => {
                if type(r) == "fraction" {  // no space remaining in this page or box
                    0pt
                } else {
                    r
                }
            }),
            gutter: if row-gutter == none {
                none
            } else {
                fixed-size-gutter
            }
        )
    }
}

// Determine the size of 'auto' and 'fr' columns and rows
#let determine-auto-column-row-sizes(
    grid: (),
    page_width: 0pt, page_height: 0pt,
    styles: none,
    columns: none, rows: none,
    inset: none, gutter: none,
    align: auto,
) = {
    let inset = convert-length-to-pt(inset, styles: styles)

    let columns_res = determine-column-sizes(
        grid: grid,
        page_width: page_width, styles: styles, columns: columns,
        inset: inset,
        col-gutter: gutter.col
    )
    columns = columns_res.columns
    gutter.col = columns_res.gutter

    let rows_res = determine-row-sizes(
        grid: grid,
        page_height: page_height, styles: styles,
        columns: columns,  // so we consider available width
        rows: rows,
        inset: inset,
        align: align,
        row-gutter: gutter.row
    )
    rows = rows_res.rows
    gutter.row = rows_res.gutter

    (
        columns: columns,
        rows: rows,
        gutter: gutter
    )
}

// -- end: col/row size functions --

// -- width/height utilities --

#let width-between(start: 0, end: none, columns: (), gutter: none, pre-gutter: false) = {
    let col-gutter = default-if-none(default-if-none(gutter, (col: 0pt)).col, 0pt)
    end = default-if-none(end, columns.len())

    let col_range = range(start, calc.min(columns.len() + 1, end))

    let sum = 0pt
    for i in col_range {
        sum += columns.at(i) + col-gutter
    }

    // if the end is after all columns, there is
    // no gutter at the end.
    if pre-gutter or end == columns.len() {
        sum = calc.max(0pt, sum - col-gutter) // remove extra gutter from last col
    }

    sum
}

#let height-between(start: 0, end: none, rows: (), gutter: none, pre-gutter: false) = {
    let row-gutter = default-if-none(default-if-none(gutter, (row: 0pt)).row, 0pt)
    end = default-if-none(end, rows.len())

    let row_range = range(start, calc.min(rows.len() + 1, end))

    let sum = 0pt
    for i in row_range {
        sum += rows.at(i) + row-gutter
    }

    // if the end is after all rows, there is
    // no gutter at the end.
    if pre-gutter or end == rows.len() {
        sum = calc.max(0pt, sum - row-gutter) // remove extra gutter from last row
    }

    sum
}

#let cell-width(x, colspan: 1, columns: (), gutter: none) = {
    width-between(start: x, end: x + colspan, columns: columns, gutter: gutter, pre-gutter: true)
}

#let cell-height(y, rowspan: 1, rows: (), gutter: none) = {
    height-between(start: y, end: y + rowspan, rows: rows, gutter: gutter, pre-gutter: true)
}

// overide start and end for vlines and hlines (keep styling options and stuff)
#let v-or-hline-with-span(v_or_hline, start: none, end: none) = {
    (
        ..v_or_hline,
        start: start,
        end: end,
        parent: v_or_hline  // the one that generated this
    )
}

// check the subspan a hline or vline goes through inside a larger span
#let get-included-span(l_start, l_end, start: 0, end: 0, limit: 0) = {
    if l_start in (none, auto) {
        l_start = 0
    }

    if l_end in (none, auto) {
        l_end = limit
    }

    l_start = calc.max(0, l_start)
    l_end = calc.min(end, limit)

    // ---- ====     or ==== ----
    if l_end < start or l_start > end {
        return none
    }

    // --##==   ;   ==##-- ;  #### ; ... : intersection.
    (calc.max(l_start, start), calc.min(l_end, end))
}

// restrict hlines and vlines to the cells' borders.
// i.e.
//                | (vline)
//                |
// (hline) ----====---      (= and || indicate intersection)
//             |  ||
//             ----   <--- sample cell
#let v-and-hline-spans-for-cell(cell, hlines: (), vlines: (), x_limit: 0, y_limit: 0, grid: ()) = {
    // only draw lines from the parent cell
    if is-tablex-occupied(cell) {
        return (
            hlines: (),
            vlines: ()
        );
    }

    let hlines = hlines
        .filter(h => {
            let y = h.y

            let in_top_or_bottom = y in (cell.y, cell.y + cell.rowspan)

            let hline_hasnt_already_ended = (
                h.end in (auto, none)  // always goes towards the right
                or h.end >= cell.x + cell.colspan  // ends at or after this cell
            )

            (in_top_or_bottom
                and hline_hasnt_already_ended)
        })
        .map(h => {
            // get the intersection between the hline and the cell's x-span.
            let span = get-included-span(h.start, h.end, start: cell.x, end: cell.x + cell.colspan, limit: x_limit)

            if span == none {  // no intersection!
                none
            } else {
                v-or-hline-with-span(h, start: span.at(0), end: span.at(1))
            }
        })
        .filter(x => x != none)

    let vlines = vlines
        .filter(v => {
            let x = v.x

            let at_left_or_right = x in (cell.x, cell.x + cell.colspan)

            let vline_hasnt_already_ended = (
                v.end in (auto, none)  // always goes towards the bottom
                or v.end >= cell.y + cell.rowspan  // ends at or after this cell
            )

            (at_left_or_right
                and vline_hasnt_already_ended)
        })
        .map(v => {
            // get the intersection between the hline and the cell's x-span.
            let span = get-included-span(v.start, v.end, start: cell.y, end: cell.y + cell.rowspan, limit: y_limit)

            if span == none {  // no intersection!
                none
            } else {
                v-or-hline-with-span(v, start: span.at(0), end: span.at(1))
            }
        })
        .filter(x => x != none)

    (
        hlines: hlines,
        vlines: vlines
    )
}

// Are two hlines the same?
// (Check to avoid double drawing)
#let is-same-hline(a, b) = (
    is-tablex-hline(a)
        and is-tablex-hline(b)
        and a.y == b.y
        and a.start == b.start
        and a.end == b.end
        and a.gutter-restrict == b.gutter-restrict
)

#let _largest-stroke-among-lines(lines, stroke-auto: 1pt) = (
    calc.max(0pt, ..lines.map(l => stroke-len(l.stroke, stroke-auto: stroke-auto)))
)

#let _largest-stroke-among-hlines-at-y(y, hlines: none, stroke-auto: 1pt) = {
    _largest-stroke-among-lines(hlines.filter(h => h.y == y), stroke-auto: stroke-auto)
}

#let _largest-stroke-among-vlines-at-x(x, vlines: none, stroke-auto: 1pt) = {
    _largest-stroke-among-lines(vlines.filter(v => v.x == x), stroke-auto: stroke-auto)
}

// -- end: width/height utilities --

// -- drawing --

#let parse-stroke(stroke) = {
    if type(stroke) == "color" {
        stroke + 1pt
    } else if type(stroke) in ("length", "relative length", "ratio", "stroke", "dictionary") or stroke in (none, auto) {
        stroke
    } else {
        panic("Invalid stroke '" + repr(stroke) + "'.")
    }
}

// How much should this line expand?
// If it's not at the edge of the parent line => don't expand
// spanned-tracks-len: row_len (if vline), col_len (if hline)
#let get-actual-expansion(line, spanned-tracks-len: 0) = {
    // TODO: better handle negative expansion
    if line.expand in (none, (none, none), auto, (auto, auto)) {
        return (none, none)
    }
    if type(line.expand) != "array" {
        line.expand = (line.expand, line.expand)
    }

    let parent = get-top-parent(line)
    let parent-start = default-if-auto-or-none(parent.start, 0)
    let parent-end = default-if-auto-or-none(parent.end, spanned-tracks-len)

    let start = default-if-auto-or-none(line.start, 0)
    let end = default-if-auto-or-none(line.end, spanned-tracks-len)

    let expansion = (none, none)

    if start == parent-start {  // starts where its parent starts
        expansion.at(0) = default-if-auto(line.expand.at(0), 0pt)  // => expand to the left
    }

    if end == parent-end {  // ends where its parent ends
        expansion.at(1) = default-if-auto(line.expand.at(1), 0pt)  // => expand to the right
    }

    expansion
}

#let draw-hline(hline, initial_x: 0, initial_y: 0, columns: (), rows: (), stroke: auto, vlines: (), gutter: none, pre-gutter: false) = {
    let start = hline.start
    let end = hline.end
    let stroke-auto = parse-stroke(stroke)
    let stroke = default-if-auto(hline.stroke, stroke)
    let stroke = parse-stroke(stroke)

    if default-if-auto-or-none(start, 0) == default-if-auto-or-none(end, columns.len()) { return }

    if (pre-gutter and hline.gutter-restrict == bottom) or (not pre-gutter and hline.gutter-restrict == top) {
        return
    }

    let expand = get-actual-expansion(hline, spanned-tracks-len: columns.len())
    let left-expand = default-if-auto-or-none(expand.at(0), 0pt)
    let right-expand = default-if-auto-or-none(expand.at(1), 0pt)

    if default-if-auto(hline.stroke-expand, true) == true {
        let largest-stroke = _largest-stroke-among-vlines-at-x.with(vlines: vlines, stroke-auto: stroke-auto)
        left-expand += largest-stroke(default-if-auto-or-none(start, 0)) / 2  // expand to the left to close stroke gap
        right-expand += largest-stroke(default-if-auto-or-none(end, columns.len())) / 2  // close stroke gap to the right
    }

    let y = height-between(start: initial_y, end: hline.y, rows: rows, gutter: gutter, pre-gutter: pre-gutter)
    let start_x = width-between(start: initial_x, end: start, columns: columns, gutter: gutter, pre-gutter: false) - left-expand
    let end_x = width-between(start: initial_x, end: end, columns: columns, gutter: gutter, pre-gutter: hline.stop-pre-gutter == true) + right-expand

    if end_x - start_x < 0pt {
        return  // negative length
    }

    let start = (
        start_x,
        y
    )
    let end = (
        end_x,
        y
    )

    if stroke != auto {
        if stroke != none {
            line(start: start, end: end, stroke: stroke)
        }
    } else {
        line(start: start, end: end)
    }
}

#let draw-vline(vline, initial_x: 0, initial_y: 0, columns: (), rows: (), stroke: auto, gutter: none, hlines: (), pre-gutter: false, stop-before-row-gutter: false) = {
    let start = vline.start
    let end = vline.end
    let stroke-auto = parse-stroke(stroke)
    let stroke = default-if-auto(vline.stroke, stroke)
    let stroke = parse-stroke(stroke)

    if default-if-auto-or-none(start, 0) == default-if-auto-or-none(end, rows.len()) { return }

    if (pre-gutter and vline.gutter-restrict == right) or (not pre-gutter and vline.gutter-restrict == left) {
        return
    }

    let expand = get-actual-expansion(vline, spanned-tracks-len: rows.len())
    let top-expand = default-if-auto-or-none(expand.at(0), 0pt)
    let bottom-expand = default-if-auto-or-none(expand.at(1), 0pt)

    if default-if-auto(vline.stroke-expand, true) == true {
        let largest-stroke = _largest-stroke-among-hlines-at-y.with(hlines: hlines, stroke-auto: stroke-auto)
        top-expand += largest-stroke(default-if-auto-or-none(start, 0)) / 2  // close stroke gap to the top
        bottom-expand += largest-stroke(default-if-auto-or-none(end, rows.len())) / 2  // close stroke gap to the bottom
    }

    let x = width-between(start: initial_x, end: vline.x, columns: columns, gutter: gutter, pre-gutter: pre-gutter)
    let start_y = height-between(start: initial_y, end: start, rows: rows, gutter: gutter) - top-expand
    let end_y = height-between(start: initial_y, end: end, rows: rows, gutter: gutter, pre-gutter: stop-before-row-gutter or vline.stop-pre-gutter == true) + bottom-expand

    if end_y - start_y < 0pt {
        return  // negative length
    }

    let start = (
        x,
        start_y
    )
    let end = (
        x,
        end_y
    )

    if stroke != auto {
        if stroke != none {
            line(start: start, end: end, stroke: stroke)
        }
    } else {
        line(start: start, end: end)
    }
}

// -- end: drawing

// main functions

// Gets a state variable that holds the page's max x ("width") and max y ("height"),
// considering the left and top margins.
// Requires placing 'get-page-dim-writer(the_returned_state)' on the
// document.
// The id is to differentiate the state for each table.
#let get-page-dim-state(id) = state("tablex_tablex_page_dims__" + repr(id), (width: 0pt, height: 0pt, top_left: none, bottom_right: none))

// A little trick to get the page max width and max height.
// Places a component on the page (or outer container)'s top left,
// and one on the page's bottom right, and subtracts their coordinates.
//
// Must be fed a state variable, which is updated with (width: max x, height: max y).
// The content it returns must be placed in the document for the page state to be
// written to.
//
// NOTE: This function cannot differentiate between the actual page
// and a possible box or block where the component using this function
// could be contained in.
#let get-page-dim-writer() = locate(w_loc => {
    let table_id = _tablex-table-counter.at(w_loc)
    let page_dim_state = get-page-dim-state(table_id)

    place(top + left, locate(loc => {
        page_dim_state.update(s => {
            if s.top_left != none {
                s
            } else {
                let pos = loc.position()
                let width = s.width - pos.x
                let height = s.width - pos.y
                (width: width, height: height, top_left: pos, bottom_right: s.bottom_right)
            }
        })
    }))

    place(bottom + right, locate(loc => {
        page_dim_state.update(s => {
            if s.bottom_right != none {
                s
            } else {
                let pos = loc.position()
                let width = s.width + pos.x
                let height = s.width + pos.y
                (width: width, height: height, top_left: s.top_left, bottom_right: pos)
            }
        })
    }))
})

// Draws a row group using locate() and a block().
#let draw-row-group(
    row-group,
    is-header: false,
    header-pages-state: none,
    first-row-group: none,
    columns: none, rows: none,
    stroke: none,
    gutter: none,
    repeat-header: false,
    styles: none,
    min-pos: none,
    max-pos: none,
    header-hlines-have-priority: true,
    table-loc: none,
    total-width: none,
    global-hlines: (),
    global-vlines: (),
) = {
    let width-between = width-between.with(columns: columns, gutter: gutter)
    let height-between = height-between.with(rows: rows, gutter: gutter)
    let draw-hline = draw-hline.with(columns: columns, rows: rows, stroke: stroke, gutter: gutter, vlines: global-vlines)
    let draw-vline = draw-vline.with(columns: columns, rows: rows, stroke: stroke, gutter: gutter, hlines: global-hlines)

    let group-rows = row-group.rows
    let hlines = row-group.hlines
    let vlines = row-group.vlines
    let start-y = row-group.y_span.at(0)
    let end-y = row-group.y_span.at(1)

    locate(loc => {
        // let old_page = latest-page-state.at(loc)
        // let this_page = loc.page()

        // let page_turned = not is-header and old_page not in (this_page, -1)
        let pos = loc.position()
        let page = pos.page
        let rel_page = page - table-loc.page() + 1

        let at_top = pos.y == min-pos.y  // to guard against re-draw issues
        let header_pages = header-pages-state.at(loc)
        let header_count = header_pages.len()
        let page_turned = page not in header_pages

        // draw row group
        block(
            breakable: false,
            fill: none, radius: 0pt, stroke: none,
        {
            let added_header_height = 0pt  // if we added a header, move down

            // page turned => add header
            if page_turned and at_top and not is-header {
                if repeat-header != false {
                    header-pages-state.update(l => l + (page,))
                    if (repeat-header == true) or (type(repeat-header) == "integer" and rel_page <= repeat-header) or (type(repeat-header) == "array" and rel_page in repeat-header) {
                        let measures = measure(first-row-group.content, styles)
                        place(top+left, first-row-group.content)  // add header
                        added_header_height = measures.height
                    }
                }
            }

            let row_gutter_dy = default-if-none(gutter.row, 0pt)

            // move lines down by the height of the added header
            show line: place.with(top + left, dy: added_header_height)

            let first_x = none
            let first_y = none

            let row_heights = 0pt

            let first_row = true
            for row in group-rows {
                if row.len() > 0 {
                    let first_cell = row.at(0)
                    row_heights += rows.at(first_cell.cell.y)
                }
                for cell_box in row {
                    let x = cell_box.cell.x
                    let y = cell_box.cell.y
                    first_x = default-if-none(first_x, x)
                    first_y = default-if-none(first_y, y)

                    // place the cell!
                    place(top+left,
                        dx: width-between(start: first_x, end: x),
                        dy: height-between(start: first_y, end: y) + added_header_height,
                        cell_box.box)

                    // let box_h = measure(cell_box.box, styles).height
                    // tallest_box_h = calc.max(tallest_box_h, box_h)
                }
                first_row = false
            }

            let row_group_height = row_heights + added_header_height + (row_gutter_dy * group-rows.len())

            let is_last_row = pos.y + row_group_height + row_gutter_dy >= max-pos.y

            if is_last_row {
                row_group_height -= row_gutter_dy
                // one less gutter at the end
            }

            hide(rect(width: total-width, height: row_group_height))

            let draw-hline = draw-hline.with(initial_x: first_x, initial_y: first_y)
            let draw-vline = draw-vline.with(initial_x: first_x, initial_y: first_y)

            let header_last_y = if first-row-group != none {
                first-row-group.row_group.y_span.at(1)
            } else {
                none
            }
            // if this is the second row, and the header's hlines
            // do not have priority (thus are not drawn by them,
            // otherwise they'd repeat on every page), then
            // we draw its hlines for the header, below it.
            let hlines = if not header-hlines-have-priority and not is-header and start-y == header_last_y + 1 {
                let hlines_below_header = first-row-group.row_group.hlines.filter(h => h.y == header_last_y + 1)

                hlines + hlines_below_header
            } else {
                hlines
            }

            for hline in hlines {
                // only draw the top hline
                // if header's wasn't already drawn
                if hline.y == start-y {
                    let header_last_y = if first-row-group != none {
                        first-row-group.row_group.y_span.at(1)
                    } else {
                        none
                    }
                    if not header-hlines-have-priority and not is-header and start-y == header_last_y + 1 {
                        // second row (after header, and it has no hline priority).
                        draw-hline(hline, pre-gutter: false)
                    } else if hline.y == 0 or (gutter.row != none and hline.gutter-restrict == top) {
                        draw-hline(hline, pre-gutter: false)
                    } else if page_turned and (added_header_height == 0pt or not header-hlines-have-priority) {
                        draw-hline(hline, pre-gutter: false)
                        // no header repeated, but still at the top of the current page
                    }
                } else {
                    if hline.y == end-y + 1 and (
                        (is-header and not header-hlines-have-priority)
                        or (gutter.row != none and hline.gutter-restrict == top)) {
                        continue  // the next row group should draw this
                    }

                    // normally, only draw the bottom hlines
                    draw-hline(hline, pre-gutter: true)

                    // don't draw the post-row gutter hline
                    // if this is the last row in the page
                    // or the last row in the whole table
                    if gutter.row != none and hline.y < rows.len() and not is_last_row {
                        draw-hline(hline, pre-gutter: false)
                    }
                }
            }

            for vline in vlines {
                draw-vline(vline, pre-gutter: true, stop-before-row-gutter: is_last_row)

                // don't draw the post-col gutter vline
                // if this is the last vline
                if gutter.col != none and vline.x < columns.len() {
                    draw-vline(vline, pre-gutter: false, stop-before-row-gutter: is_last_row)
                }
            }
        })
    })
}

// Generates groups of rows.
// By default, 1 row + rows from its rowspan cells = 1 row group.
// The first row group is the header, which is repeated across pages.
#let generate-row-groups(
    grid: none,
    columns: none, rows: none,
    stroke: none, inset: none,
    gutter: none,
    fill: none,
    align: none,
    hlines: none, vlines: none,
    repeat-header: false,
    styles: none,
    header-hlines-have-priority: true,
    min-pos: none,
    max-pos: none,
    header-rows: 1,
    table-loc: none,
    table-id: none,
) = {
    let col_len = columns.len()
    let row_len = rows.len()

    // specialize some functions for the given grid, columns and rows
    let v-and-hline-spans-for-cell = v-and-hline-spans-for-cell.with(vlines: vlines, x_limit: col_len, y_limit: row_len, grid: grid)
    let cell-width = cell-width.with(columns: columns, gutter: gutter)
    let cell-height = cell-height.with(rows: rows, gutter: gutter)
    let width-between = width-between.with(columns: columns, gutter: gutter)
    let height-between = height-between.with(rows: rows, gutter: gutter)

    // each row group is an unbreakable unit of rows.
    // In general, they're just one row. However, they can be multiple rows
    // if one of their cells spans multiple rows.
    let first_row_group = none

    let header_pages = state("tablex_tablex_header_pages__" + repr(table-id), (table-loc.page(),))
    let this_row_group = (rows: ((),), hlines: (), vlines: (), y_span: (0, 0))

    let total_width = width-between(end: none)

    let row_group_add_counter = 1  // how many more rows are going to be added to the latest row group
    let current_row = 0
    let header_rows_count = calc.min(row_len, header-rows)

    for row in range(0, row_len) {
        // maximum cell total rowspan in this row
        let max_rowspan = 0

        for column in range(0, col_len) {
            let cell = grid-at(grid, column, row)
            let lines_dict = v-and-hline-spans-for-cell(cell, hlines: hlines)
            let hlines = lines_dict.hlines
            let vlines = lines_dict.vlines

            if is-tablex-cell(cell) {
                // ensure row-spanned rows are in the same group
                row_group_add_counter = calc.max(row_group_add_counter, cell.rowspan)

                let width = cell-width(cell.x, colspan: cell.colspan)
                let height = cell-height(cell.y, rowspan: cell.rowspan)

                let cell_box = make-cell-box(
                    cell,
                    width: width, height: height, inset: inset,
                    align_default: align,
                    fill_default: fill)

                this_row_group.rows.last().push((cell: cell, box: cell_box))

                let hlines = hlines
                    .filter(h =>
                        this_row_group.hlines
                            .filter(is-same-hline.with(h))
                            .len() == 0)

                let vlines = vlines
                    .filter(v => v not in this_row_group.vlines)

                this_row_group.hlines += hlines
                this_row_group.vlines += vlines
            }
        }

        current_row += 1
        row_group_add_counter = calc.max(0, row_group_add_counter - 1)  // one row added
        header_rows_count = calc.max(0, header_rows_count - 1)  // ensure at least the amount of requested header rows was added

        // added all pertaining rows to the group
        // now we can draw it
        if row_group_add_counter <= 0 and header_rows_count <= 0 {
            row_group_add_counter = 1

            let row_group = this_row_group

            // get where the row starts and where it ends
            let start_y = row_group.y_span.at(0)
            let end_y = row_group.y_span.at(1)

            let next_y = end_y + 1

            this_row_group = (rows: ((),), hlines: (), vlines: (), y_span: (next_y, next_y))

            let is_header = first_row_group == none
            let content = draw-row-group(
                row_group,
                is-header: is_header,
                header-pages-state: header_pages,
                first-row-group: first_row_group,
                columns: columns, rows: rows,
                stroke: stroke,
                gutter: gutter,
                repeat-header: repeat-header,
                total-width: total_width,
                table-loc: table-loc,
                header-hlines-have-priority: header-hlines-have-priority,
                min-pos: min-pos,
                max-pos: max-pos,
                styles: styles,
                global-hlines: hlines,
                global-vlines: vlines,
            )

            if is_header {  // this is now the header group.
                first_row_group = (row_group: row_group, content: content)  // 'content' to repeat later
            }

            (content,)
        } else {
            this_row_group.rows.push(())
            this_row_group.y_span.at(1) += 1
        }
    }
}

// -- end: main functions

// option parsing functions

#let _parse-lines(
    hlines, vlines,
    page-width: none, page-height: none,
    styles: none
) = {
    let parse-func(line, page-size: none) = {
        line.stroke-expand = line.stroke-expand == true
        line.expand = default-if-auto(line.expand, none)
        if type(line.expand) != "array" and line.expand != none {
            line.expand = (line.expand, line.expand)
        }
        line.expand = if line.expand == none {
            none
        } else {
            line.expand.slice(0, 2).map(e => {
                if e == none {
                    e
                } else {
                    e = default-if-auto(e, 0pt)
                    if type(e) not in ("length", "relative length", "ratio") {
                        panic("'expand' argument to lines must be a pair (length, length).")
                    }

                    convert-length-to-pt(e, styles: styles, page_size: page-size)
                }
            })
        }

        line
    }
    (
        hlines: hlines.map(parse-func.with(page-size: page-width)),
        vlines: vlines.map(parse-func.with(page-size: page-height))
    )
}

// Parses 'auto-lines', generating the corresponding lists of
// new hlines and vlines
#let generate-autolines(auto-lines: false, auto-hlines: auto, auto-vlines: auto, hlines: none, vlines: none, col_len: none, row_len: none) = {
    let auto-hlines = default-if-auto(auto-hlines, auto-lines)
    let auto-vlines = default-if-auto(auto-vlines, auto-lines)

    let new_hlines = ()
    let new_vlines = ()

    if auto-hlines {
        new_hlines = range(0, row_len + 1)
            .filter(y => hlines.filter(h => h.y == y).len() == 0)
            .map(y => hlinex(y: y))
    }

    if auto-vlines {
        new_vlines = range(0, col_len + 1)
            .filter(x => vlines.filter(v => v.x == x).len() == 0)
            .map(x => vlinex(x: x))
    }

    (new_hlines: new_hlines, new_vlines: new_vlines)
}

#let parse-gutters(col-gutter: auto, row-gutter: auto, gutter: auto, styles: none, page-width: 0pt, page-height: 0pt) = {
    col-gutter = default-if-auto(col-gutter, gutter)
    row-gutter = default-if-auto(row-gutter, gutter)

    col-gutter = default-if-auto(col-gutter, 0pt)
    row-gutter = default-if-auto(row-gutter, 0pt)

    if type(col-gutter) in ("length", "relative length", "ratio") {
        col-gutter = convert-length-to-pt(col-gutter, styles: styles, page_size: page-width)
    }

    if type(row-gutter) in ("length", "relative length", "ratio") {
        row-gutter = convert-length-to-pt(row-gutter, styles: styles, page_size: page-width)
    }

    (col: col-gutter, row: row-gutter)
}

// Accepts a map-X param, and returns its default, or validates
// it.
#let parse-map-func(map-func, uses-second-param: false) = {
    if map-func in (none, auto) {
        if uses-second-param {
            (a, b) => b  // identity
        } else {
            o => o  // identity
        }
    } else if type(map-func) != "function" {
        panic("Map parameters must be functions.")
    } else {
        map-func
    }
}

#let apply-maps(
    grid: (),
    hlines: (),
    vlines: (),
    map-hlines: none,
    map-vlines: none,
    map-rows: none,
    map-cols: none,
) = {
    vlines = vlines.map(map-vlines)
    if vlines.any(h => not is-tablex-vline(h)) {
        panic("'map-vlines' function returned a non-vline.")
    }

    hlines = hlines.map(map-hlines)
    if hlines.any(h => not is-tablex-hline(h)) {
        panic("'map-hlines' function returned a non-hline.")
    }

    let col_len = grid.width
    let row_len = grid-count-rows(grid)

    for row in range(row_len) {
        let original_cells = grid-get-row(grid, row)

        // occupied cells = none for the outer user
        let cells = map-rows(row, original_cells.map(c => {
            if is-tablex-occupied(c) { none } else { c }
        }))

        if type(cells) != "array" {
            panic("Tablex error: 'map-rows' returned something that isn't an array.")
        }

        // only modify non-occupied cells
        let cells = enumerate(cells).filter(i_c => is-tablex-cell(original_cells.at(i_c.at(0))))

        if cells.any(i_c => not is-tablex-cell(i_c.at(1))) {
            panic("Tablex error: 'map-rows' returned a non-cell.")
        }

        if cells.any(i_c => {
            let c = i_c.at(1)
            let x = c.x
            let y = c.y
            type(x) != "integer" or type(y) != "integer" or x < 0 or y < 0 or x >= col_len or y >= row_len
        }) {
            panic("Tablex error: 'map-rows' returned a cell with invalid coordinates.")
        }

        if cells.any(i_c => i_c.at(1).y != row) {
            panic("Tablex error: 'map-rows' returned a cell in a different row (the 'y' must be kept the same).")
        }

        if cells.any(i_c => {
            let i = i_c.at(0)
            let c = i_c.at(1)
            let orig_c = original_cells.at(i)

            c.colspan != orig_c.colspan or c.rowspan != orig_c.rowspan
        }) {
            panic("Tablex error: Please do not change the colspan or rowspan of a cell in 'map-rows'.")
        }
    
        for i_cell in cells {
            let cell = i_cell.at(1)
            grid.items.at(grid-index-at(cell.x, cell.y, grid: grid)) = cell
        }
    }

    for column in range(col_len) {
        let original_cells = grid-get-column(grid, column)

        // occupied cells = none for the outer user
        let cells = map-cols(column, original_cells.map(c => {
            if is-tablex-occupied(c) { none } else { c }
        }))

        if type(cells) != "array" {
            panic("Tablex error: 'map-cols' returned something that isn't an array.")
        }

        // only modify non-occupied cells
        let cells = enumerate(cells).filter(i_c => is-tablex-cell(original_cells.at(i_c.at(0))))

        if cells.any(i_c => not is-tablex-cell(i_c.at(1))) {
            panic("Tablex error: 'map-cols' returned a non-cell.")
        }

        if cells.any(i_c => {
            let c = i_c.at(1)
            let x = c.x
            let y = c.y
            type(x) != "integer" or type(y) != "integer" or x < 0 or y < 0 or x >= col_len or y >= row_len
        }) {
            panic("Tablex error: 'map-cols' returned a cell with invalid coordinates.")
        }

        if cells.any(i_c => i_c.at(1).x != column) {
            panic("Tablex error: 'map-cols' returned a cell in a different column (the 'x' must be kept the same).")
        }

        if cells.any(i_c => {
            let i = i_c.at(0)
            let c = i_c.at(1)
            let orig_c = original_cells.at(i)

            c.colspan != orig_c.colspan or c.rowspan != orig_c.rowspan
        }) {
            panic("Tablex error: Please do not change the colspan or rowspan of a cell in 'map-cols'.")
        }
    
        for i_cell in cells {
            let cell = i_cell.at(1)
            cell.content = [#cell.content]
            grid.items.at(grid-index-at(cell.x, cell.y, grid: grid)) = cell
        }
    }

    (grid: grid, hlines: hlines, vlines: vlines)
}

#let validate-header-rows(header-rows) = {
    header-rows = default-if-auto(default-if-none(header-rows, 0), 1)

    if type(header-rows) != "integer" or header-rows < 0 {
        panic("Tablex error: 'header-rows' must be a (positive) integer.")
    }

    header-rows
}

#let validate-repeat-header(repeat-header, header-rows: none) = {
    if header-rows == none or header-rows < 0 {
        return false  // cannot repeat an empty header
    }

    repeat-header = default-if-auto(default-if-none(repeat-header, false), false)

    if type(repeat-header) not in ("boolean", "integer", "array") {
        panic("Tablex error: 'repeat-header' must be a boolean (true - always repeat the header, false - never), an integer (amount of pages for which to repeat the header), or an array of integers (relative pages in which the header should repeat).")
    } else if type(repeat-header) == "array" and repeat-header.any(i => type(i) != "integer") {
        panic("Tablex error: 'repeat-header' cannot be an array of anything other than integers!")
    }

    repeat-header
}

#let validate-header-hlines-priority(
    header-hlines-have-priority
) = {
    header-hlines-have-priority = default-if-auto(default-if-none(header-hlines-have-priority, true), true)

    if type(header-hlines-have-priority) != "boolean" {
        panic("Tablex error: 'header-hlines-have-priority' option must be a boolean.")
    }

    header-hlines-have-priority
}

// -- end: option parsing

// Creates a table.
//
// OPTIONS:
// columns: table column sizes (array of sizes,
// or a single size for 1 column)
//
// rows: row sizes (same format as columns)
// align: how to align cells (alignment or 
// a function (col, row) => alignment)
//
// items: The table items, as specified by the columns
// and rows. Can also be cellx, hlinex and vlinex objects.
//
// fill: how to fill cells (color or
// a function (col, row) => color)
//
// stroke: how to draw the table lines (stroke)
// column-gutter: optional separation (length) between columns
// row-gutter: optional separation (length) between rows
// gutter: quickly apply a length to both column- and row-gutter
//
// repeat-header: true = repeat the first row (or rowspan)
// on all pages; integer = repeat for the first n pages;
// array of integers = repeat on exactly those pages
// (where 1 is the first, so ignored); false = do not repeat
// the first row group (default).
//
// header-rows: minimum amount of rows for the repeatable
// header. 1 by default. Automatically increases if
// one of the cells is a rowspan that would go beyond the
// given amount of rows. For example, if 3 is given,
// then at least the first 3 rows will repeat.
//
// header-hlines-have-priority: if true, the horizontal
// lines below the header being repeated take priority
// over the rows they appear atop of on further pages.
// If false, they draw their own horizontal lines.
// Defaults to true.
//
// auto-lines: true = applies true to both auto-hlines and
// auto-vlines; false = applies false to both.
// Their values override this one unless they are 'auto'.
//
// auto-hlines: true = draw a horizontal line on every line
// without a manual horizontal line specified; false = do
// not draw any horizontal line without manual specification.
// Defaults to 'auto' (follows 'auto-lines').
//
// auto-vlines: true = draw a vertical line on every column
// without a manual vertical line specified; false = requires
// manual specification. Defaults to 'auto' (follows
// 'auto-lines')
//
// map-cells: Takes a cellx and returns another cellx (or
// content).
//
// map-hlines: Takes each horizontal line (hlinex) and
// returns another.
//
// map-vlines: Takes each vertical line (vlinex) and
// returns another.
//
// map-rows: Maps each row of cells.
// Takes (row_num, cell_array) and returns
// the modified cell_array. Note that, here, they
// cannot be sent to another row. Also, cells may be
// 'none' if they're a position taken by a cell in a
// colspan/rowspan.
//
// map-cols: Maps each column of cells.
// Takes (col_num, cell_array) and returns
// the modified cell_array. Note that, here, they
// cannot be sent to another row. Also, cells may be
// 'none' if they're a position taken by a cell in a
// colspan/rowspan.
#let tablex(
    columns: auto, rows: auto,
    inset: 5pt,
    align: auto,
    fill: none,
    stroke: auto,
    column-gutter: auto, row-gutter: auto,
    gutter: none,
    repeat-header: false,
    header-rows: 1,
    header-hlines-have-priority: true,
    auto-lines: true,
    auto-hlines: auto,
    auto-vlines: auto,
    map-cells: none,
    map-hlines: none,
    map-vlines: none,
    map-rows: none,
    map-cols: none,
    ..items
) = {
    _tablex-table-counter.step()

    get-page-dim-writer()  // get the current page's dimensions

    let header-rows = validate-header-rows(header-rows)
    let repeat-header = validate-repeat-header(repeat-header, header-rows: header-rows)
    let header-hlines-have-priority = validate-header-hlines-priority(header-hlines-have-priority)
    let map-cells = parse-map-func(map-cells)
    let map-hlines = parse-map-func(map-hlines)
    let map-vlines = parse-map-func(map-vlines)
    let map-rows = parse-map-func(map-rows, uses-second-param: true)
    let map-cols = parse-map-func(map-cols, uses-second-param: true)

    locate(t_loc => style(styles => {
        let table_id = _tablex-table-counter.at(t_loc)
        let page_dimensions = get-page-dim-state(table_id)
        let page_dim_at = page_dimensions.final(t_loc)
        let t_pos = t_loc.position()

        // Subtract the max width/height from current width/height to disregard margin/etc.
        let page_width = page_dim_at.width
        let page_height = page_dim_at.height

        let max_pos = default-if-none(page_dim_at.bottom_right, (x: t_pos.x + page_width, y: t_pos.y + page_height))
        let min_pos = default-if-none(page_dim_at.top_left, t_pos)

        let items = items.pos().map(table-item-convert)

        let gutter = parse-gutters(
            col-gutter: column-gutter, row-gutter: row-gutter,
            gutter: gutter,
            styles: styles,
            page-width: page_width, page-height: page_height
        )

        let validated_cols_rows = validate-cols-rows(
            columns, rows, items: items.filter(is-tablex-cell))

        let columns = validated_cols_rows.columns
        let rows = validated_cols_rows.rows
        items += validated_cols_rows.items

        let col_len = columns.len()
        let row_len = rows.len()

        // generate cell matrix and other things
        let grid_info = generate-grid(
            items,
            x_limit: col_len, y_limit: row_len,
            map-cells: map-cells
        )

        let table_grid = grid_info.grid
        let hlines = grid_info.hlines
        let vlines = grid_info.vlines
        let items = grid_info.items

        for _ in range(grid_info.new_row_count - row_len) {
            rows.push(auto)  // add new rows (due to extra cells)
        }

        let col_len = columns.len()
        let row_len = rows.len()

        let auto_lines_res = generate-autolines(
            auto-lines: auto-lines, auto-hlines: auto-hlines,
            auto-vlines: auto-vlines,
            hlines: hlines,
            vlines: vlines,
            col_len: col_len,
            row_len: row_len
        )

        hlines += auto_lines_res.new_hlines
        vlines += auto_lines_res.new_vlines

        let parsed_lines = _parse-lines(hlines, vlines, styles: styles, page-width: page_width, page-height: page_height)
        hlines = parsed_lines.hlines
        vlines = parsed_lines.vlines

        let mapped_grid = apply-maps(
            grid: table_grid,
            hlines: hlines,
            vlines: vlines,
            map-hlines: map-hlines,
            map-vlines: map-vlines,
            map-rows: map-rows,
            map-cols: map-cols
        )

        table_grid = mapped_grid.grid
        hlines = mapped_grid.hlines
        vlines = mapped_grid.vlines

        // re-parse just in case
        let parsed_lines = _parse-lines(hlines, vlines, styles: styles, page-width: page_width, page-height: page_height)
        hlines = parsed_lines.hlines
        vlines = parsed_lines.vlines

        // convert auto to actual size
        let updated_cols_rows = determine-auto-column-row-sizes(
            grid: table_grid,
            page_width: page_width, page_height: page_height,
            styles: styles,
            columns: columns, rows: rows,
            inset: inset, align: align,
            gutter: gutter
        )

        let columns = updated_cols_rows.columns
        let rows = updated_cols_rows.rows
        let gutter = updated_cols_rows.gutter

        let row_groups = generate-row-groups(
            grid: table_grid,
            columns: columns, rows: rows,
            stroke: stroke, inset: inset,
            gutter: gutter,
            fill: fill, align: align,
            hlines: hlines, vlines: vlines,
            styles: styles,
            repeat-header: repeat-header,
            header-hlines-have-priority: header-hlines-have-priority,
            header-rows: header-rows,
            min-pos: min_pos,
            max-pos: max_pos,
            table-loc: t_loc,
            table-id: table_id
        )

        grid(columns: (auto,), rows: auto, ..row_groups)
    }))
}

// Same as table but defaults to lines off
#let gridx(..options) = {
    tablex(auto-lines: false, ..options)
}
