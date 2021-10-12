from latex2sympy2 import *
from sympy import *

for k in range(1, 5):
    print(latex2sympy(r"\frac{\displaystyle \sum_{i=1}^{3}\binom{3}{i}(4-k)^{3-i}}{4^{3}}").subs({Symbol("k"): k}).doit())