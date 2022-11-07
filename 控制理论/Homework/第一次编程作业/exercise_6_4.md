反馈系统传递函数:

$
\displaystyle 
\begin{aligned}
T(s)
& = \frac{G(s)}{1+G(s)H(s)}  \\
& = \frac{\frac{5}{s(s+10)}}{1+\frac{5}{s(s+10)} \cdot (2+\frac{K_1}{s})}  \\
& = \frac{5 s}{s^{3} + 10 s^{2} + 10 s + 5 K_{1}}  \\
\end{aligned}
$

可得劳斯判定表:

$
\begin{array}{c|cc}
s^{3} & 1 & 10  \\
s^{2} & 10 & 5K_1  \\
s^{1} & 10 - \frac{1}{2}K_{1} & 0  \\
s^{0} & 5K_1 & 0  \\
\end{array}
$

因此有 $5K_1 > 0$ 与 $10 - \frac{1}{2}K_{1} > 0$,

即有 $0 < K_1 < 20$.