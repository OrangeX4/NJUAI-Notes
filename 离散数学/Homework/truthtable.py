def imply(p, q):
    if not p:
        return True
    elif q:
        return True
    else:
        return False


def onlyif(p, q):
    if p and q:
        return True
    elif not p and not q:
        return True
    else:
        return False


def xor(p, q):
    return not onlyif(p, q)


def boolToString(p):
    if p:
        return 'T'
    else:
        return 'F'


def truthtable(func, *set):
    # Init input
    input = {}
    for i in range(0, len(set)):
        input[set[i]] = False

    def block(begin, end):

        if begin < end - 1:
            current = set[begin]
            input[current] = False
            block(begin + 1, end)

            input[current] = True
            block(begin + 1, end)
        else:
            def printOut():

                out = ''
                for i in range(0, end):
                    out = out + '|' + boolToString(input[set[i]]) + ' '
                out = out + '|'+ boolToString(func(tuple(input.values()))) +' |'

                print(out)
            
            current = set[begin]
            input[current] = False
            printOut()

            input[current] = True
            printOut()

            return

    out = ''
    for i in range(0, len(set)):
        out = out + '|' + set[i] + ' '
    out = out + '|'
    print(out)

    out = ''
    for i in range(0, len(set)):
        out = out + '|--'
    out = out + '|'
    print(out)

    block(0, len(set) - 1)


truthtable(lambda p: (not onlyif(p[0], not onlyif(p[1], p[2]))), 'x', 'y', 'z', 'Ans')
