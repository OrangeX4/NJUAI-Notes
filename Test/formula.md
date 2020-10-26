# Formula

Inline formula: $syz$

Line formula displayed in center:

$$ xyz $$

---

$x^4$

$x_1$

$^{16}_{8}O^{2+}_{2}$

---



---


字体控制，符号：\displaystyle，如：$\displaystyle\frac{x+y}{y+z}$

下划线符号，符号：\underline，如：$\underline{x+y}$

上大括号，符号：\overbrace{算式}，如：$\overbrace{a+b+c+d}^{2.0}$

下大括号，符号：\underbrace{算式}，如：$a+\underbrace{b+c}_{1.0}+d$

上位符号，符号：\stacrel{上位符号}{基位符号}，如：$\vec{x}\stackrel{\mathrm{def}}{=}{(x_1,\dots,x_n)}$

---
Some Placeholders:

$x \qquad y$

$x \quad y$

$x \ y$

$x \: y$

$x \, y$

$xy$

$x\!y$

---

$() \big(\big) \Big(\Big) \bigg(\bigg) \Bigg(\Bigg)$

$[x+y]$

$\{x+y\}$

$\left( \displaystyle\frac{x+y}{y+z} \right)$

${n+1 \choose k}={n \choose k}+{n \choose k-1}$

$\displaystyle \sum {k_0, k_1, \ldots >0 \atop k_0 + k_1 + \cdots = n} A_{k_0} A_{k_1} \cdots$

---
四则运算

$x + y = z$

$x - y = z$

$x \pm y = z$

$x \mp y = z$

$x \times y = z$

$x \cdot y = z$

$x \ast y = z$

$x \div y = z$

$x / y = z$

$\frac {x + y}{x - y}$

$\displaystyle \frac {x + y}{x - y}$

${x + y} \over {x - y}$

$|x + y|$

---

$\overline{xyz}$

$\sqrt x$

$\sqrt [3]{x + y}$

$\log {x \atop y}$

$\log ^x_y$

$\lim^{x \to +\infty}_{y \to 0} {\frac x y}$

$\displaystyle \lim^{x \to +\infty}_{y \to 0} \frac x y$

$\sum^{x \to \infty}_{y \to 0} \frac x y$

$\displaystyle \int ^{\infty}_0 {x \ dx}$

$\displaystyle {{\partial x} \over {\partial y}}$

$$
\begin{bmatrix}
1      &2      &\cdots &4      &5  &6  &\cdots &8
\\
\vdots &\vdots &\ddots &\vdots &13 &14 &\cdots &16
\end{bmatrix}
$$

$$
\begin{gathered}
\begin{matrix} 0 & 1 \\ 1 & 0 \end{matrix}
\quad
\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
\quad
\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
\quad
\begin{Bmatrix} 1 & 0 \\ 0 & -1 \end{Bmatrix}
\quad
\begin{vmatrix} a & b \\ c & d \end{vmatrix}
\quad
\begin{Vmatrix} i & 0 \\ 0 & -i \end{Vmatrix}
\end{gathered}
$$

---

$x + y = z$

$x + y > z$

$x + y < z$

$x + y \geq z$

$x + y \leq z$

$x + y \neq z$

$x + y \ngeq z$

$x + y \not \leq z$

$x + y \approx z$

$x + y \equiv z$

---

$x \in y$

$x \not \in y$

$x \notin y$

$x \subset y$

$x \supset y$

$x \subseteq y$

$x \cup y$

$x \cap y$

$x \setminus y$

$x \bigodot y$

$x \bigotimes y$

$\mathbb{R}$

$\mathbb{Z}$

$\empty$

---

$\displaystyle f(x, y) = {{x + y} \over {x - y}}$

$\displaystyle f(x, y) = {{x + y} \over {x - y}}$

---

有了宽和高，把它们乘起来就是矩形的面积。于是，所有矩形的**面积之和S**就可以写成这样：

$$
\begin{aligned}
S &= { {1 \over n} {\left( 1 \over n \right)}^2 +  {1 \over n} {\left( 2 \over n \right)}^2 +  {1 \over n} {\left( 3 \over n \right)}^2 + \cdots { {1 \over n} {\left( n \over n \right)}^2}}\\
&= {1 \over n^3}{(1 + 2^2 + 3^2 + \cdots + n^2)}\\
&= {1 \over n^3}{({{2n^3 + 3n^2 + n} \over 6})}\\
&= \frac{1}{3} + \frac{1}{2n} + \frac{1}{6n^2}
\end{aligned}
$$

这只是一段简单的化简，相信大家只要知道**平方和公式**是下面这样就秒懂了：

$$
1 + 2^2 + 3^2 + \cdots + n^2 = \frac{2n^3 + 3n^2 + n}{6}
$$

---

连续分式：

$$
\displaystyle
x = a_0 + \frac{1}{
    \displaystyle
        a_1 + \frac{1}{
            \displaystyle
            a_2 + \frac{1}{
                \displaystyle
                a_3 + \frac{1}{a_4}
            }
    }}
$$

$\sqrt[n]{1 + x + x^2 + x^3 + \cdots + x^n}$

$\cos (2\theta) = \cos^2 \theta - \sin^2 \theta$

$\displaystyle \lim_{x \to 0} \frac{\sin x}{x} = 1$

$\displaystyle \sum_{k+1}^N k^2$

$\displaystyle \int_{k+1}^N k^2$

$a \xLeftarrow{x + y + z} b$

$a \stackrel{x + y + z}{\leftarrow} b$

---

复杂公式输入：

$$
\begin{aligned}
a & = b + c \\
  & = d + e
\end{aligned}
$$

$$
\begin{aligned}
a & = 1 & b & = 2 & c & = 3 \\
d & = -1 & e & = -2 & f & = -5
\end{aligned}
$$

$$
\begin{matrix}
x & y \\
z & v
\end{matrix}
$$

$$
A_{m, n} =
\begin{pmatrix}
a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m,1} & a_{m,2} & \cdots & a_{m,n} \\
\end{pmatrix}
$$

---
Array:

$$
\begin{array}{|c|c||c|}
a & b & S \\
\hline
0 & 0 & 1 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 0
\end{array}
$$

$$
f(n) =
\begin{cases}
n/2, & \text{if } n \text{ is even} \\
3n+1, & \text{if } n \text{ is odd}
\end{cases}

\begin{cases}
3x + 5y + z = 1 \\
7x - 2y + 4z = 2 \\
-6x + 3y + 2z = 3
\end{cases}
$$

$\displaystyle \left < \frac{a}{b} \right >$

$$
\land \qquad \lor \qquad \lnot \qquad \forall \qquad \exist \qquad \cup \qquad \cap \qquad \in \qquad \ni
$$

$$
\ln X \qquad \log_2 X 
\Box \qquad \Diamond \qquad \triangle \qquad \perp \qquad \angle BAC = 45^\circ \qquad \propto \qquad \sim \qquad \cong
$$

$^1_2X^3_4$

$^1_2\!X^3_4$

$\overset{\to}{x}$

$\vec x$

$$\sum_{k = 1}^N k^2$$

$$\prod_{i = 1}^N x_i$$



$$\coprod_{i = 1}^N x_i$$

$$\lim_{n \to \infty} x_n$$

$$\int_{-N}^N e^x \ dx$$

$$\iint_{D}^W dx \ dy$$

$$\iiint_{E}^V dx \ dy \ dz$$

$$\oint_{C} x^3 \ dx + 4y^2 \ dy$$

---

$$
\begin{aligned}
\Gamma \ \gamma \\
\Delta \ \delta \\
\Theta \ \theta \\
\Lambda \ \lambda \\
\Xi \ \xi \\
\Pi \ \pi \\
\Sigma \ \sigma \\
\Upsilon \ \upsilon \\
\Phi \ \phi \\
\Psi \ \psi \\
\Omega \ \omega \\
\Alpha \ \alpha \\
\Beta \ \beta \\
\Zeta \ \zeta \\
\Eta \ \eta \\
\Iota \ \iota \\
\Kappa \ \kappa \\
\Mu \ \mu \\
\Nu \ \nu \\
\Xi \ \xi \\
\end{aligned}
$$

$$
\bar{z}_{i}=-\bar{a}_{i} \cdot \operatorname{sgn}\left(\sum_{j=1}^{n} s_{j} Y_{j i}\right) \quad i=1, \cdots, m
$$