# %%
from latex2sympy2 import latex2sympy
import sympy

s = latex2sympy(r'\frac{10 K_{p} s + 9}{5 s (s + 1) (s + 2)}=-1')
print(s)

#%%
import numpy as np
import matplotlib.pyplot as plt

def get_real(p):
    return p.args[0]

def get_imag(p):
    return p.args[1].args[0]

# %%
s1 = s[2]
# get the right part of Eq
s2 = s1.rhs
p = {}
real = []
imag = []
for K in np.arange(0, 2, 0.01):
    p[K] = s2.evalf(subs={list(s2.free_symbols)[0]: K})
    real.append(get_real(p[K]))
    imag.append(get_imag(p[K]))
real = np.array(real)
imag = np.array(imag)
# plot
plt.plot(real, imag, 'x', real, -real, 'x')
# 取出 real 和 imag 最相近时的 K
i = np.argmin(np.abs(real + imag))
K = np.arange(0, 2, 0.01)[i]
print(K)
print(p[K])