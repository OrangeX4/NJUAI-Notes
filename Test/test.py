from latex2sympy2 import *
from sympy import *

for k in range(0, 3):
    print(latex2sympy(r"\frac{\binom{2}{k}\binom{13}{3-k}}{\binom{15}{3}}").subs({Symbol("k"): k}).doit())