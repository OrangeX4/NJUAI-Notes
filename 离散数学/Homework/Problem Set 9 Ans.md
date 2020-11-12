# Problem Set 9

# Problem 1

(1) $|A|=3$

(2) $|B|=\aleph_0$

(3) $|C|=\aleph_0$

(4) $|B\cap C|=\aleph_0$

(5) $|B\cap C|=\aleph_0$

(6) $|D|=\aleph_1$

# Problem 2

## (1)

$令C=B-A, 易知C也是可数集$

$\therefore A\cup B=A\cup (B-A)=A\cup C$

$不妨假设|A|\leq|C|, 否则将A与C对调$

$由A,C均为可数集可定义f_A: |A|\xrightarrow[onto]{1-1} A,f_C: |C|\xrightarrow[onto]{1-1} C$

$定义函数f:|A\cup B| \to A\cup B$

$当x<2|A|时,$

$
f(x)=
\begin{cases}
f_A(\displaystyle\frac{x}{2}), &x=2k, k\in \mathbb{N} \\
f_C(\displaystyle\frac{x-1}{2}), &x=2k+1, k\in \mathbb{N} \\
\end{cases}
$

$当x\geq 2|A|时,$

$
f(x)=f_C(x-|A|)
$

$\therefore 易知f为双射函数, |A\cup B|\in \mathbb{N}或|A\cup B|=\aleph_0$

$\therefore A\cup B是可数集$

## (2)

$不妨定义f_A: \mathbb{N}\xrightarrow{1-1,onto} A, f_B: \mathbb{N}\xrightarrow{1-1,onto} B$

$令f:A\times B\to \mathbb{N}, f((f_A(m),f_B(n)))=\displaystyle\sum_{i=1}^{m+n}i+m=\frac{(m+n)(m+n+1)}{2}+m$

$\because 易知f是双射函数$

$\therefore A\times B是可列集$


# Problem 3

a) $可数无限的, 取f(x)=x+11$

b) $可数无限的, 取f(x)=-2x-1$

c) $有限的$

d) $不可数的$

e)$
可数无限的, 取f(x)=
\begin{cases}
(2,\displaystyle\frac{x}{2}+1), &x=2k,k\in \mathbb{N} \\
(3,\displaystyle\frac{x+1}{2}), &x=2k+1,k\in \mathbb{N} \\
\end{cases}
$

f)$
可数无限的, 取f(x)=
\begin{cases}
5x, &x=2k,k\in \mathbb{N} \\
-5x-5, &x=2k+1,k\in \mathbb{N} \\
\end{cases}
$

# Problem 4

$假设A-B是可数的$

$\because B是可数集合$

$\therefore A\cap B是可数集合$

$\because A-(A\cap B)=A-B也为可数集合$

$\therefore A=A-(A\cap B)+(A\cap B)$

$由\text{Problem 2.(1)可知两个可数集合的并集也是可数集合}$

$\therefore A是可数集合$

$\because A是不可数集合, 产生矛盾, 假设不成立$

$\therefore A-B是不可数的$

# Problem 5

$\because A是可数集合$

$当A是有穷集时, 不妨记A\approx n, 则有g:n\xrightarrow[onto]{1-1}A$

$\because 存在f:A\xrightarrow[onto]{1-1}B$

$\therefore f\circ g:n\xrightarrow[onto]{1-1}B$

$\therefore B\approx n$

$\therefore B是有穷集$

$\therefore B是可数的$

$当A是无穷可列集时, A\approx \mathbb{N}$

$\therefore 同理可知B\approx \mathbb{N}$

$\therefore B是可数的$

# Problem 6

$取f_A:|A|\xrightarrow[onto]{1-1} A, f_B:|B|\xrightarrow[onto]{1-1} B$

$\because A\subset B$

$\therefore |A|<|B|$

$\therefore 令f:A\to B, f(f_A(n))=f_B(n)$

$易知f是单射函数$

$\therefore A\prec\cdot B$

# Problem 7

$\because A=\{a,b,c\}$

$\therefore \mathcal P(A)=\{\empty,\{a\},\{b\},\{c\},\{a,b\},\{b,c\},\{a,c\},\{a,b,c\}\}$

$\therefore B=\{$
$\quad\qquad\qquad\{(a,0),(b,0),(c,0)\},$
$\quad\qquad\qquad\{(a,0),(b,0),(c,1)\},$
$\quad\qquad\qquad\{(a,0),(b,1),(c,0)\},$
$\quad\qquad\qquad\{(a,0),(b,1),(c,1)\},$
$\quad\qquad\qquad\{(a,1),(b,0),(c,0)\},$
$\quad\qquad\qquad\{(a,1),(b,0),(c,1)\},$
$\quad\qquad\qquad\{(a,1),(b,1),(c,0)\},$
$\quad\qquad\qquad\{(a,1),(b,1),(c,1)\}$
$\quad\qquad\}$

$\therefore |\mathcal P(A)|=|B|=8$

$\therefore \mathcal P(A)\approx B$

# Problem 8

(1) $
是, 取f(x)=
\begin{cases}
x, &x=2k,k\in \mathbb{N} \\
-x-1, &x=2k+1,k\in \mathbb{N} \\
\end{cases}
$

(2) $不是, (0,0.5)\approx \mathbb{R}\not\approx \mathbb{N}$

(3) $
是, 取f(x)=
\begin{cases}
\displaystyle\frac{7x}{2}, &x=2k,k\in \mathbb{N} \\
\displaystyle\frac{-7x-7}{2}, &x=2k+1,k\in \mathbb{N} \\
\end{cases}
$

(4) $
是, 取f(x)=
\begin{cases}
\displaystyle\frac{3x}{2}+1, &x=2k,k\in \mathbb{N} \\
\displaystyle\frac{x-1}{2}+2, &x=2k+1,k\in \mathbb{N} \\
\end{cases}
$

# Problem 9

a) $A=\mathbb{R},B=\mathbb{R}$

b) $A=\mathbb{R},B=\mathbb{R}-\mathbb{N}$

c) $A=P(\mathbb{R}),B=\mathbb{R}$

# Problem 10

$设这些可数集合为S_i, i=1,2,\cdots,m$

$不妨定义f_A: |A|\xrightarrow[onto]{1-1} A, f_B: |B|\xrightarrow[onto]{1-1} B, f:\mathbb{N}\to A\cup B$

$$
\begin{matrix}
\mathbb{N}&: &0 &1 &2 &3 &4 &5 &\cdots \\
A\cup B&: &f_A(0) &f_B(0) &f_A(1) &f_A(2) &f_B(2) &f_A(3) &\cdots \\
\end{matrix}
$$

$若f_B(n)与f_A(i)相同,\quad i=1或2或\cdots 或n,$
$ 则跳过f_B(n), 如此处跳过f_B(1)作为示例$

$若f_A(n),f_B(n)无定义则跳过, 直至两者均无定义则停止$

$\therefore 易知f是一个\mathbb{N}或n_0到A\cup B双射函数$
$\quad (其中n_0是小于等于|A|+|B|的自然数)$

$\therefore A\cup B是可列集$