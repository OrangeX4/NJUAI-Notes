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

$不妨定义f_A: \mathbb{N}\xrightarrow[onto]{1-1} A, f_B: \mathbb{N}\xrightarrow[onto]{1-1} B, f:\mathbb{N}\to A\cup B$

$①对于x=0时,$

$若f_A(0)=f_B(0), 则定义f(0)=f_A(0), 令n_1=1$

$若f_A(0)\neq f_B(0), 则定义f(0)=f_A(0), f(1)=f_B(0), 令n_1=1$

$②对于x=k时,$

$假设f(k)已有定义, f(k+1)暂无定义$

$对于x=k+1时,$

$若f_A(n_{k+1})=f_B(n_{k+1}),$
$则定义f(k+1)=f_A(n_{k+1}), 令n_{k+2}=n_{k+1}+1$

$若f_A(n_{k+1})\neq f_B(n_{k+1}),$
$则定义f(k+1)=f_A(n_{k+1}), f(k+2)=f_B(n_{k+1}), 令n_{k+2}=n_{k+1}+1$

$即若f_A,f_B是一样的, 则只取f_A, 若f_A,f_B不同, 则以前后顺序给予f定义$

$\therefore 易知f是\mathbb{N}到A\cup B的双射函数$

$\therefore A\cup B是可列集$

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

