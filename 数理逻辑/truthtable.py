def imply(p, q):
    return not p or q


def onlyif(p, q):
    return not p ^ q


def bool_to_string(p, true_value, false_value):
    return true_value if p else false_value


def eight(input, s):
    return input[4 * s[0] + 2 * s[1] + s[2]]


def four(input, s):
    return input[2 * s[0] + s[1]]


def selector(input, s):
    return input[s]


def truthtable(*expressions, names=['Ans'], true_value='T', false_value='F'):
    # Initiate arguments
    arguments = {}
    # Get arguments of the first expression
    arguments_names = list(expressions[0].__code__.co_varnames)

    def block(begin, end):
        if begin < end:
            current_argument = arguments_names[begin]
            arguments[current_argument] = False
            block(begin + 1, end)

            arguments[current_argument] = True
            block(begin + 1, end)
        else:
            # Arguments
            out = ''
            for i in range(0, end):
                out += '| ' + bool_to_string(arguments[arguments_names[i]], true_value, false_value) + ' '

            # Expressions' values
            for expression in expressions:
                value = expression(*tuple(arguments.values()))
                out += '| ' + bool_to_string(value, true_value, false_value) + ' '
            out += '|'

            print(out)
            return

    # First line
    out = ''
    for arguments_name in arguments_names:
        out += '| ' + arguments_name + ' '
    for name in names:
        out += '| ' + name + ' '
    out += '|'
    print(out)

    # Second line
    out = ''
    for arguments_name in arguments_names:
        out += '|' + '-' * (len(arguments_name) + 2)
    for name in names:
        out += '|' + '-' * (len(name) + 2)
    out += '|'
    print(out)

    # Main values
    block(0, len(arguments_names))


truthtable(lambda A, B, C: selector([B, C], A), true_value='1', false_value='0')
