import io

def match_a(inp):
    return inp.read(1) == 'a'

def match_end(inp):
    return inp.read(1) == ''

def match_S(inp):
    fallback = inp.tell()
    if match_a(inp) and match_S(inp) and match_a(inp):
        return True
    inp.seek(fallback)
    if match_a(inp) and match_a(inp):
        return True
    return False

def match(inp):
    return match_S(inp) and match_end(inp)

print(match(io.StringIO(6 * 'a')))