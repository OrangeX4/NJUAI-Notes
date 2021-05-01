from math import sin, exp
from scipy import optimize
import numpy as np
print('1. [python, scipy] 最⼤值')


def f(x):
    return sin(x - 2) ** 2 * exp(-x ** 2)


result = optimize.minimize_scalar(lambda x: -f(x))
print('x = ', result.x)
print('f(x) = ', -result.fun)


# ---------------------------
print('----------------------')
print('2. [python, scipy] 数组距离')

r, c = [int(v) for v in input().split()]
matrix = []
for i in range(r):
    matrix.append([int(v) for v in input().split()])


def distance(vec1, vec2):
    return sum([(vec1[i] - vec2[i]) ** 2 for i in range(min(len(vec1), len(vec2)))]) ** 0.5


result = []
for vec1 in matrix:
    array = []
    for vec2 in matrix:
        array.append(distance(vec1, vec2))
    result.append(array)
print(np.array(result))