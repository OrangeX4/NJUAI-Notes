# Problem Set 10

# Problem 1

(1) $Basis: 3^7=2187<7!=5040$

(2) $I.H.: 假设3^k<k!, k>6$

(3) $I.S.: 3^{k+1}=3\times 3^k<3\times k! < (k+1)\times k!=(k+1)!成立$

$由数学归纳法, 命题得证$


# Problem 2

$对于n<10的情况,$

$0和0^5=0最后一位相同$
$1和1^5=1最后一位相同$
$2和2^5=32最后一位相同$
$3和3^5=243最后一位相同$
$4和4^5=1024最后一位相同$
$5和5^5=3125最后一位相同$
$6和6^5=7776最后一位相同$
$7和7^5=16807最后一位相同$
$8和8^5=32768最后一位相同$
$9和9^5=59049最后一位相同$

$对于n\geq 10的情况, n=10a+b, 其中a\geq 10, b< 10$

$\therefore n^5=(10a+b)^5=100000a^5+50000a^4b+10000a^3b^2+1000a^2b^3+50ab^4+b^5$

$\therefore n^5 \mod 10= b^5 \mod 10$

$\because n \mod 10 = b$

$\because 由n<10的情况可知, b^5 \mod 10=b$

$\therefore 可知正整数n和n^5最后一位必相同$


# Problem 3

(1) $Basis: 当n=4时, 四边凸多边形的对角线数目为\frac{1}{2}n(n-3)=2成立$

(2) $I.H.: 假设当n=k时, k边凸多边形的对角线数目为\frac{1}{2}k(k-3)$

(3) $I.S.:$

$当n=k+1时,$

$易知k+1边形的对角线与k边形对角线的数目相差k-1条$

$\therefore 对角线数目=\frac{1}{2}k(k-3)+k-1=\frac{1}{2}(k+1)(k-2)$

$由数学归纳法, 命题得证$


# Problem 4

(1) $Basis: 当n=1时, 1=2^0$

(2) $I.H.: 假设当n\leq k时, n可以写成2的不同幂次之和$

(3) $I.S.:$

$对于n=k+1,$

$当k+1是偶数时,$

$\displaystyle\frac{k+1}{2}是小于等于k的整数, 可以写成2的不同幂次之和$

$给\displaystyle\frac{k+1}{2}乘上2后得k+1, 易知也可以写成2的不同幂次之和$

$当k+1是奇数时,$

$k是偶数, 可以写成无2^0项的2的不同幂次之和$

$给k加上2^0得k+1, 易知k+1可以写成2的不同幂次之和$

$由数学归纳法, 命题得证$


# Problem 5

## a)

(1) $奠基: ones(\lambda)=0$

(2) $递归步骤:$

$ones(\omega 1)=ones(\omega)+1, \omega\in\sum^*$
$ones(\omega x)=ones(\omega), \omega\in\sum^*\land x\in\sum-\{1\}$

## b)

(1) $Basis: 对s\in\sum^*, 显然有ones(s\cdot \lambda)=ones(s)+ones(\lambda)$

(2) $I.H.:$

$令P(t)表示: 每当s\in\sum^*, 就有ones(s\cdot t)=ones(s)+ones(t)$
$假设P(t)成立$

(3) $I.S.:$

$由I.H.可知P(t)成立, 即ones(s\cdot t)=ones(s)+ones(t)$

$
\begin{aligned}
\therefore ones(s\cdot (t1))&=ones((s\cdot t)1) \\
&=ones(s\cdot t)+1 \\
&=ones(s)+ones(t)+1 \\
&=ones(s)+ones(t1)
\end{aligned}
$

$
\begin{aligned}
\quad ones(s\cdot (tx))&=ones((s\cdot t)x) \\
&=ones(s\cdot t) \\
&=ones(s)+ones(t) \\
&=ones(s)+ones(tx)
\end{aligned}
$
$其中x\in\sum-\{1\}$

$由结构归纳法, 命题得证$


# Problem 6

## a)

(1) $奠基: m(x)=x, x\in N, 其中N=\{0,1,2,3,4,5,6,7,8,9\}$

(2) $递归步骤:$

$m(sx)=\min(m(s),m(x))$

$其中s\in N^*, x\in N$

## b)

(1) $Basis:$

$对s\in N^*, 显然有m(s\cdot x)=m(sx)=\min(m(s),m(x)), x\in N$

(2) $I.H.:$

$令P(t)表示: 每当s\in N^*, 就有m(s\cdot t)=\min(m(s),m(t))$
$假设P(t)成立$

(3) $I.S.:$

$由I.H.可知P(t)成立, 即m(s\cdot t)=\min(m(s),m(x))$

$
\begin{aligned}
m(s\cdot (tx))&=m((s\cdot t)x) \\
&=\min(m(s\cdot t),m(x)) \\
&=\min(\min(m(s),m(t)),m(x)) \\
&=\min(m(s),m(t),m(x)) \\
&=\min(m(s),\min(m(t),m(x))) \\
&=\min(m(s),m(t\cdot x)) \\
&=\min(m(s),m(tx)) \\
\end{aligned}
$

$其中x\in N$

$由结构归纳法, 命题得证$


# Problem 7

## a)

$假设P_{m,m}\neq P_m$

$由P_m和P_{m,m}的定义易知 P_{m,m}\subseteq P_m$

$\therefore P_{m,m}\subset P_m$

$\therefore \exist x_0> m, 使得m=x_0$

$\therefore 产生矛盾$

$\therefore P_{m,m}=P_m$

## b)

(1) $奠基: P_{m,1}=1易知成立$

(2) $归纳步骤:$

$当m<n时,$

$同理于(a), 易证明P_{m,n}=P_m=P_{m,m}$

$当m=1时$

$\therefore P_{1,n}=P_{1,1}=1$

$当m=n>1时$

$\because P_{m,m}仅仅比P_{m,m-1}多了m=m这种分拆方式$

$\therefore P_{m,m}=1+P_{m,m-1}$

$当m>n>1时$

$此时P_{m,n}有两类拆分方式,$
$一种是有n这一项的, 一种是没有n这一项的$

$对于没有n这一项的分拆方式数目, 可以直接用P_{m,n-1}表示$

$对于有n这一项的分拆方式, 可以写成 m = n + \overbrace{\cdots\cdots}^{m-n的拆分}$
$即有n这一项的分拆方式数目可以记作P_{m-n,n}$

$\therefore P_{m,m}=P_{m,n-1}+P_{m-n,n}$

$由广义归纳法, 命题得证$

## c)

$
\begin{aligned}
P_5 &=P_{5,5}=1+P_{5,4}=1+P_{5,3}+P_{1,4}=2+P_{5,2}+P_{2,3} \\
&=2+P_{5,1}+P_{3,2}+P_{2,2}=4+P_{3,1}+P_{1,2}+P_{2,1} \\
&=7
\end{aligned}
$

$
\begin{aligned}
P_6 &=P_{6,6}=1+P_{6,5}=1+P_{6,4}+P_{1,5}=2+P_{6,3}+P_{2,4} \\
&=2+P_{6,2}+P_{3,3}+P_{2,2}=4+P_{6,1}+P_{4,2}+P_{3,2}+P_{2,1} \\
&=6+P_{4,2}+P_{3,2}=6+P_{4,1}+P_{2,2}+P_{3,1}+P_{1,2}=10+P_{2,1} \\
&=11
\end{aligned}
$


# Problem 8

(1) $Basis:$

$对(3,2)\in M, 可以表示为(2^1+1,2^0+1)的形式$

(2) $I.H.:$

$假设(x,y)\in M, 且(x,y)可以表示成(2^{k+1}+1,2^k+1)$

(3) $I.S.:$

$由I.H.可知(x,y)\in M, 且(x,y)可以表示成(2^{k+1}+1,2^k+1)$

$
\begin{aligned}
\therefore (3x-2y,x)&=(3(2^{k+1}+1)-2(2^{k}+1),2^{k+1}+1) \\
&=(3\times 2^{k+1}+3-2\times 2^{k}-2,2^{k+1}+1) \\
&=(6\times 2^{k}-2\times 2^{k}+1,2^{k+1}+1) \\
&=(2^{k+2}+1,2^{k+1}+1) \\
\end{aligned}
$

$由结构归纳法, 命题得证$


# Problem 9

> **procdure** reverse(str: 字符串)
> **if** str只有一个字符 **then return** str 
> **else return** str的最后一个字符 + reverse(去掉最后一个字符的str)
> {输出是str的倒置字符串}