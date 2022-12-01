from math import log2
from random import shuffle

def para_sum(n: int):
    d = [[i] for i in range(n + 1)]
    P = [[i] for i in range(n + 1)]
    for j in range(int(log2(n))):
        d_prime = d.copy()
        i_range = list(range(2 ** j + 1, n + 1))
        # shuffle(i_range)
        for i in i_range:
            P[i] = d[i - 2 ** j]
            d_prime[i] = d[i] + d[i - 2 ** j]
        d = d_prime
        print(i_range[0], d)

n = 8
para_sum(n)