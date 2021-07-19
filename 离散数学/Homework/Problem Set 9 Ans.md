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

$\therefore A\cup B=A\cup (B-A)=A\cup C, A\cap C=\empty$

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

$\therefore A\preceq\cdot B$

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

$设这些可数集合为C_i, \quad(i=1,2,\cdots,m)$

$令S_1=C_1,S_i=C_j-(C_1\cup \cdots\cup C_{j-1}),\quad (j=2,3,\cdots,m)$
$易知S_i也是可数集, 且互不相同的两个S_i的交集为空$

$不妨假定|S_1|\leq|S_2|\leq\cdots\leq|S_m|, 否则交换它们的位置$

$\therefore C_1\cup C_2\cup\cdots\cup C_i=S_1\cup S_2\cup\cdots\cup S_i, \quad(i=1,2,\cdots,m)$

$由S_i均为可数集可定义f_{S_i}: |S_i|\xrightarrow[onto]{1-1} A$

$定义函数f:|C_1\cup C_2\cup\cdots\cup C_i| \to C_1\cup C_2\cup\cdots\cup C_i$

$当0\leq x<m|S_1|时,$

$
f(x)=
\begin{cases}
f_{S_1}(\displaystyle\frac{x}{m}), &x=mk, k\in \mathbb{N} \\
f_{S_2}(\displaystyle\frac{x-1}{m}), &x=mk+1, k\in \mathbb{N} \\
\cdots \\
f_{S_m}(\displaystyle\frac{x-m+1}{m}), &x=mk+m-1, k\in \mathbb{N} \\
\end{cases}
$

$当\displaystyle\sum_{i=1}^n(m-i+1)|S_i|\leq x<\sum_{i=1}^{n+1}(m-i+1)|S_i|时,$

$
f(x)=
\begin{cases}
f_{S_n}(\displaystyle\frac{x}{m-n}), &x=(m-n)(\displaystyle\sum_{i=1}^n(m-i+1)|S_i|+k), k\in \mathbb{N} \\
f_{S_{n+1}}(\displaystyle\frac{x-1}{m-n}), &x=(m-n)(\displaystyle\sum_{i=1}^n(m-i+1)|S_i|+k)+1, k\in \mathbb{N} \\
\cdots \\
f_{S_m}(\displaystyle\frac{x-m+n+1}{m-n}), &x=(m-n)(\displaystyle\sum_{i=1}^n(m-i+1)|S_i|+k)+m-n-1, k\in \mathbb{N} \\
\end{cases}
$

$其中n=1,2,\cdots,m-1$

$\therefore 易知f为双射函数, |C_1\cup C_2\cup\cdots\cup C_i|\in \mathbb{N}或|C_1\cup C_2\cup\cdots\cup C_i|=\aleph_0$

$\therefore C_1\cup C_2\cup\cdots\cup C_i是可数集$
