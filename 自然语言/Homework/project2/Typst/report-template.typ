#import "./tablex.typ": *

#let indent() = {
    box(width: 2em)
}

#let indent_par(body) = {
    box(width: 1.8em)
    body
}

#let empty_par() = {
    v(-1em)
    box()
}

// Answer box
#let answer(body) = rect(width: 100%, stroke: 0.5pt, inset: 10pt, body)

// Heading Numbering
#let Numbering(base: 1, first-level: none, second-level: none, third-level: none, format, ..args) = {
    if (first-level != none and args.pos().len() == 1) {
        numbering(first-level, ..args)
        return
    }
    if (second-level != none and args.pos().len() == 2) {
        numbering(second-level, ..args)
        return
    }
    if (third-level != none and args.pos().len() == 3) {
        numbering(third-level, ..args)
        return
    }
    // default
    if (args.pos().len() >= base) {
        numbering(format, ..(args.pos().slice(base - 1)))
        return
    }
}

// three-line-table
#let three-line-table(columns: 1, ..options) = tablex(
    columns: columns,
    align: center + horizon,
    auto-lines: false,
    ..options.named(),
    hlinex(),
    ..options.pos().slice(0, columns),
    hlinex(),
    ..options.pos().slice(columns),
    hlinex(),
)


#let report(size: 12pt, subject: "", title: "", date: "", author: "", show-outline: false, par-indent: true, body) = {
    // Set the document's basic properties.
    set document(author: author, title: subject + title + author)
    set page(numbering: "1", number-align: center)
    
    // Save heading and body font families in variables.
    let font = (
        title: ("IBM Plex Serif", "Source Han Serif SC"),
        body: ("IBM Plex Serif", "Source Han Serif SC"),
        mono: ("IBM Plex Mono", "Source Han Sans"),
    )

    // Set body font family.
    set text(size, font: font.body, lang: "zh")
    show heading: it => {
        set block(below: 1em)
        it
    } + if (par-indent) { empty_par() }

    set par(justify: true, first-line-indent: if (par-indent) {2em} else {0em})
    show par: set block(spacing: 1.5em) // spacing between paragraphs

    // Image
    set image(width: 80%)
    show image: align.with(center)

    // Code Block
    show raw: set text(font: font.mono)
    show raw: set par(justify: false)
    show raw.where(block: false): box.with(
        fill: luma(240),
        inset: (x: 3pt, y: 0pt),
        outset: (x: 0pt, y: 3pt),
        radius: 2pt,
    )
    show raw.where(block: true): block.with(
        width: 100%,
        fill: luma(240),
        inset: 10pt,
        radius: 4pt,
    )

    // Title page
    align(center + top)[
        #v(20%)
        #text(font: font.title, 2em, weight: 500, subject)
        #v(2em, weak: true)
        #text(font: font.title, 2em, weight: 500, title)
        #v(2em, weak: true)
        #text(author)
    ]
    pagebreak()

    // Page Header
    set page(
        header: {
            set text(font: font.body, 0.9em, baseline: 0.8em)
            grid(
                columns: (1fr, auto, 1fr),
                align(left, date),
                align(center, subject),
                align(right, title),
            )
            stack(
                spacing: 0.2em,
                line(length: 100%, stroke: 1pt),
                line(length: 100%, stroke: 0.5pt)
            )
        }
    )

    if (show-outline) {
        set par(first-line-indent: 0em)

        align(center)[
          #heading(level: 1, numbering: none, outlined: false)[
            目录
          ]
        ]
        
        show outline: set box(height: 1.2em, baseline: 0.5em)
        
        outline(depth: 2, indent: true, title: none)
        
        pagebreak()
    }

    body
}