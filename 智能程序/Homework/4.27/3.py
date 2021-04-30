from scipy.optimize import fsolve
import numpy as np
from math import cos

def f(x):
    x0, x1, x2 = [float(v) for v in x]
    return [
        3 * x1 + 1,
        4 * x0 - 2 * cos(x1 * x2),
        x1 * x2 - 3.5
    ]

result = fsolve(f, [0.0, 0.0, 0.0])


print(result)
print(f(result))
print(np.isclose(f(result), [0.0, 0.0, 0.0]))