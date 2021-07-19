# 例题

## 1.

$\displaystyle\lim_{x\to \infty}(\frac{a_1^{\frac{1}{x}}+a_2^{\frac{1}{x}}+\cdots +a_n^{\frac{1}{x}}}{n})^{nx}=\lim_{x\to \infty}(1+\frac{\displaystyle\sum_{i=1}^n(a_i^\frac{1}{x}-1)}{n})^{\frac{n}{\sum}\cdot\frac{\sum}{n}\cdot nx}$

$相当于求\displaystyle\frac{\displaystyle\sum_{i=1}^n(a_i^\frac{1}{x}-1)}{\frac{1}{x}}$

$\because\displaystyle\frac{a_i^{\frac{1}{x}}-1}{\frac{1}{x}}=\frac{e^{\frac{1}{x}\ln a_i}-1}{\frac{1}{x}}\sim \frac{\frac{1}{x}\ln a_i}{\frac{1}{x}}=\ln a_i$

$\therefore\displaystyle\frac{\displaystyle\sum_{i=1}^n(a_i^\frac{1}{x}-1)}{\frac{1}{x}}=\ln\prod_{i=1}^na_i$


## 2.

$用有限覆盖定理证明Cauchy收敛准则$

#### 知识点:

$Cauchy收敛准则: \forall\varepsilon>0,\exist N, 当m,n>N时, |a_m-a_n|<\varepsilon$

$本质是实数的完备性, 对有理数不一定成立,$
$例如取一个逼近\pi的数列, \{3, 3.1, 3.14, 3.141, \cdots \}$

#### 证明:

$柯西数列一定是有界的, 先证明有界, 再用有界覆盖定理$


## 3.

$\quad\varphi(t)在[m,M]上严格凸$
$\Leftrightarrow 对\forall t_1,t_2\in[m,M],t_1\neq t_2,\varphi(\displaystyle\frac{t_1+t_2}{2})<\frac{\varphi(t_1)+\varphi(t_2)}{2}$

$若\varphi(t)在[m,M]上有定义, \varphi''(t)>0, 则\varphi(t)严格凸$

#### 知识点:

$\varphi''(t)>0\Rightarrow\varphi(t)在[m,M]上严格凸$

$满足f(\lambda t_1+(1-\lambda)t_2)\leq \lambda f(t_1)+(1-\lambda)f(t_2)为凸函数$

#### 证明:

$考虑是否能应用泰勒展开$

$f(x)=f(x_0)+f'(x_0)(x-x_0)+\displaystyle\frac{f''(\xi)}{2}(x-x_0)^2$

$\therefore \displaystyle \varphi(t)=\varphi(\frac{t_1+t_2}{2})+\varphi'(\frac{t_1+t_2}{2})(t-\frac{t_1+t_2}{2})+\frac{\varphi''(\xi)}{2}(t-\frac{t_1+t_2}{2})^2$

$\displaystyle\therefore\varphi(t_1)=\varphi(\frac{t_1+t_2}{2})+\frac{t_1-t_2}{2}\varphi'(\frac{t_1+t_2}{2})+\frac{\varphi''(\xi_1)}{2}(\frac{t_1-t_2}{2})^2$
$\displaystyle\quad\varphi(t_2)=\varphi(\frac{t_1+t_2}{2})+\frac{t_2-t_1}{2}\varphi'(\frac{t_1+t_2}{2})+\frac{\varphi''(\xi_2)}{2}(\frac{t_2-t_1}{2})^2$

$\displaystyle\therefore\varphi(t_1)+\varphi(t_2)=2\varphi(\frac{t_1+t_2}{2})+\frac{\varphi''(\xi_1)+\varphi''(\xi_2)}{2}(\frac{t_1-t_2}{2})^2$

$\therefore \varphi(\displaystyle\frac{t_1+t_2}{2})<\frac{\varphi(t_1)+\varphi(t_2)}{2}$


## 4.

$若f(x)在(a,+\infty)上一致连续, 能否推断\displaystyle\lim_{x\to a^+}f(x),\lim_{x\to +\infty}f(x)存在$

#### 证明:

$f(x)=x是一致连续的, 但是\displaystyle\lim_{x\to +\infty}f(x)\to+\infty, 不存在$

$但是\displaystyle\lim_{x\to a^+}f(x)是存在的$

$\because\forall\varepsilon>0,\exist\delta>0,|x'-x''|<\delta时, |f(x')-f(x'')|<\varepsilon$

$\therefore 对于(a,a+2\delta)区间上, 满足Cauchy收敛$


## 5.

$直径和高等长的圆柱叫正圆柱.$
$两个正圆柱, 一个竖着放, 一个横着放, 求围成的体积.$

