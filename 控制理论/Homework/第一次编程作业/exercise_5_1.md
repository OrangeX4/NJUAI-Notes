# 5.1

由于脉冲信号的拉普拉斯变换为 $R(s) = 1$, 因此有

$
\displaystyle
Y(s) = \frac{15}{s^{2}+8s+15}R(s) = \frac{15}{(s+3)(s+5)} = \frac{15}{2 (s + 3)} - \frac{15}{2 (s + 5)}
$

因此, 进行逆拉普拉斯变换可得

$
\displaystyle 
y(t) = \frac{15}{2}e^{-3t} - \frac{15}{2}e^{-5t}
$

此为解析方法的结果.