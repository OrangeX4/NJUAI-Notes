# %%
def P1(w):
    if w > 0:
        P1(w - 1)
        print(w)

P1(3)

# %%
def P2(w):
    stack = []
    while w > 0 or len(stack) != 0:
        while w > 0:
            print(w)
            stack.append(w)
            w = w - 1
        if len(stack) != 0:
            w = stack.pop()
            w = w - 1

P2(3)

# %%
def P2(w):
    stack = [(w, 'l0')]
    while len(stack) != 0:
        w, label = stack.pop()
        if w > 0:
            if label == 'l1':
                print(w)
            stack.append((w - 1, 'l1'))
            stack.append((w - 1, 'l2'))

P2(3)

# %%
