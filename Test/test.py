import re
HatSequence = r"\overline \bar \hat \tilde \widetilde \widehat".split()
LeftArrows = r"\leftarrow|\longleftarrow|\Leftarrow|\Longleftarrow".split("|")
RightArrows = r"\rightarrow|\longrightarrow|\Rightarrow|\Longrightarrow".split(
    "|")
LeftrightArrows = [
    "\\" + x for x in "leftrightarrow|longleftrightarrow|Leftrightarrow|Longleftrightarrow|iff".split("|")]



def extract_operator(line):
    line = line.strip()
    if line[0] in ["=", "<", ">"]:
        return line[0]
    elif line[0] != "\\":
        return ""
    else:
        if not line[1].isalpha():
            return ""
        rv = "\\" + re.fullmatch("([a-zA-Z]+)([^a-zA-Z].*)", line[1:]).group(1)
        remain = re.fullmatch("([a-zA-Z]+)([^a-zA-Z].*)", line[1:]).group(2)
        if remain and remain[0] == "{":
            index = 0
            depth = 0
            while index < len(remain):
                if remain[index] == "{":
                    depth += 1
                    index += 1
                    continue
                elif remain[index] == "}":
                    depth -= 1
                    index += 1
                    if depth == 0:
                        rv += remain[:index]
                        break
                    continue
                elif remain[index] == "\\":
                    index += 2
                    continue
                else:
                    index += 1
                    continue
        return rv


def findfirstoperator(line):
    index = 0
    depth = 0
    while index < len(line):
        if line[index] == '\s':
            index += 1
            continue
        elif line[index] in ['{', '(']:
            depth += 1
            index += 1
            continue
        elif line[index] in ['}', ')']:
            depth -= 1
            index += 1
            continue
        elif depth <= 0 and line[index] == '=':
            return index
        elif depth <= 0 and all(line[index:].startswith(x) for x in ["\\le", "\\ge", ">", "<", "\\succ", "\\prec", "\\sim", "\\ne", "\\not"]):
            return index
        else:
            index += 1
            continue
    else:
        return len(line) - len(line.lstrip())


def findmatched_parentheses(line, lindex):
    depth = 0
    matched = {"(": ")", ")": "(", "[": "]", "]": "[", "{": "}", "}": "{"}
    c = line[lindex]
    d = matched[c]
    if line[lindex] in ["(", "[", "{"]:
        for index in range(lindex, len(line)):
            if line[index] == c:
                depth += 1
            elif line[index] == d:
                depth -= 1
            if depth == 0:
                return index
    elif line[lindex] in [")", "]", "}"]:
        for index in range(lindex, -1, -1):
            if line[index] == c:
                depth += 1
            elif line[index] == d:
                depth -= 1
            if depth == 0:
                return index
    return -1



def add_placeholder(snip):
    info = snip.buffer[snip.line]
    snip.buffer[snip.line] = ''
    # print(info)
    snip.expand_anon(info)


def generate_matrix(prefix, snip):
    info = snip.buffer[snip.line]
    spacelen = len(info) - len(info.lstrip())
    linfo = info[:snip.snippet_start[1]]
    rinfo = info[snip.snippet_end[1]:]
    info = info[snip.snippet_start[1]:snip.snippet_end[1]]
    # print([linfo, rinfo, info])
    if len(info) > 1 and info[1].isnumeric():
        real_shape = info[:2]
        virtual_shape = info[2:]
    else:
        real_shape = info[0]
        virtual_shape = info[1:]
    if len(real_shape) == 1:
        row_amount = int(real_shape)
        column_amount = int(real_shape)
    else:
        row_amount = int(real_shape[0])
        column_amount = int(real_shape[1])
    if len(virtual_shape) == 0:
        virtual_row_amount = "0"
        virtual_column_amount = "0"
    elif len(virtual_shape) == 1:
        virtual_row_amount = virtual_shape[0]
        virtual_column_amount = virtual_shape[0]
    else:
        virtual_row_amount = virtual_shape[0]
        virtual_column_amount = virtual_shape[1]
    snip.buffer[snip.line] = ''
    displayed = re.sub(r"\\", r"\\\\", linfo) + "\\begin{%cmatrix}\n" % prefix

    def generate_code(i, j, row, column, virtual_row, virtual_column):
        if i == 1 and j == 1:
            return ""
        else:
            code = """`!p
from snippet_helpers import generate_matrix_element
snip.rv = generate_matrix_element(%d, %d, %d, %d, '%c', '%c', [%s], [%s])
`""" % (i, j, row, column, virtual_row, virtual_column, "''," + ",".join("t[%d]" % x for x in range(1, j+1)), "''," + ",".join("t[%d]" % (1 + column * (x-1)) for x in range(1, i+1)))
        return code
    if row_amount > 0 and column_amount > 0:
        displayed += " " * (4 + len(linfo)) + "$1\t" + \
            ("& " if column_amount > 1 else "\\" * 4)
        index = 2
        for i in range(2, column_amount + 1):
            displayed += "${" + "{}".format(index) + ":" + generate_code(1, i, row_amount, column_amount,
                                                                         virtual_row_amount, virtual_column_amount) + "}\t" + ("& " if i < column_amount else "\\" * 4)
            index += 1
        displayed += "\n"
        for j in range(2, row_amount + 1):
            displayed += " " * (4 + len(linfo))
            for i in range(1, column_amount + 1):
                displayed += "${" + "{}".format(index) + ":" + generate_code(j, i, row_amount, column_amount,
                                                                             virtual_row_amount, virtual_column_amount) + "}\t" + ("& " if i < column_amount else "\\" * 4)
                index += 1
            displayed += "\n"
    displayed += " " * len(linfo) + "\\end{%cmatrix}$0" % prefix + (
        " " + re.sub(r"\\", r"\\\\", rinfo) if rinfo else "")
    snip.expand_anon(displayed)


def complete(input_str, candidate):
    candidate = [x[len(input_str):]
                 for x in candidate if x.startswith(input_str)]
    if len(candidate) == 1:
        return candidate[0]
    elif "" in candidate:
        return ""
    elif candidate:
        return "(" + "|".join(candidate) + ")"
    else:
        return ""

generate_matrix('', '')