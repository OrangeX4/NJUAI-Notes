# Cheat Sheet

## 常见不定积分

* $\displaystyle\int a^x{\rm d}x=\frac{a^x}{\ln a}+C$
* $\displaystyle\int \frac{1}{x}{\rm d}x=\ln|x|+C$
* $\displaystyle\int \ln x{\rm d}x=x\ln x-x+C$
* $\displaystyle\int \frac{1}{1+x^2}{\rm d}x=\arctan x+C$
* $\displaystyle\int \frac{1}{\sqrt{1-x^2}}{\rm d}x=\arcsin x+C$
* $\displaystyle\int -\frac{1}{\sqrt{1-x^2}}{\rm d}x=\arccos x+C$
* $\displaystyle\int \tan x{\rm d}x=-\ln|\cos x|+C$
* $\displaystyle\int \cot x{\rm d}x=-\ln|\sin x|+C$
* $\displaystyle\int \sec x{\rm d}x=-\ln|\sec x+\tan x|+C=\frac{1}{2}\ln\left| \frac{1+\sin x}{1-\sin x} \right|+C$
* $\displaystyle\int \csc x{\rm d}x=-\ln|\csc x-\cot x|+C=\ln\left| \tan \frac{x}{2} \right|+C$

## 华里兹公式

由区间再现公式 $\displaystyle I_n=\int_0^{\frac{\pi}{2}}\sin^nx{\rm d}x=\int_0^\frac{\pi}{2}\cos^nx{\rm d}x, \int_a^bf(x){\rm d}x=\int_a^bf(x){\rm d}x=\int_a^bf(a+b-x){\rm d}x$

$\because\displaystyle I_n'=\int\sin^nx{\rm d}x=\frac{1}{n}\cos x\sin^{n-1}x+\frac{n-1}{n}I_{n-2}', \quad n\geq 2$

$\therefore\displaystyle I_n=\frac{n-1}{n}I_{n-2}, I_0=\frac{\pi}{2}, I_1=1$

华里兹公式

$
\therefore I_n=
\begin{cases}
\displaystyle\frac{(n-1)!!}{n!!}=\frac{(n-1)(n-3)\times 2}{n(n-2)\times 1}, &n \text{ is odd} \\
\displaystyle\frac{(n-1)!!}{n!!}\times\frac{\pi}{2}=\frac{(n-1)(n-3)\times 1}{n(n-2)\times 2}\times\frac{\pi}{2}, &n \text{ is even} \\
\end{cases}
$

当 $n$ 为奇数时:

$\therefore \displaystyle \int_{0}^{\pi}\sin^{n}x\mathrm{d}x=2I_{n}, \int_{0}^{\pi}\cos^{n}x\mathrm{d}x=0$

$\therefore \displaystyle \int_{0}^{2\pi}\sin^{n}x\mathrm{d}x=0, \int_{0}^{2\pi}\cos^{n}x\mathrm{d}x=0$

当 $n$ 为偶数时:

$\therefore \displaystyle \int_{0}^{\pi}\sin^{n}x\mathrm{d}x=2I_{n}, \int_{0}^{\pi}\cos^{n}x\mathrm{d}x=2I_{n}$

$\therefore \displaystyle \int_{0}^{2\pi}\sin^{n}x\mathrm{d}x=4I_{n}, \int_{0}^{2\pi}\cos^{n}x\mathrm{d}x=4I_{n}$


## 欧拉积分

$\Gamma$ 函数: $\displaystyle\Gamma(s)=\int_0^{+\infty}x^se^{-x}{\rm d}x$

1. $\Gamma(s+1)=s\cdot \Gamma(s)$
2. $\Gamma(1)=1$
3. $\Gamma(n)=n!$
4. $\displaystyle x=t^2, \Gamma(s)=2\int_0^{+\infty}t^{2s-1}\cdot e^{-t^2}{\rm d}t, \Gamma(\frac{1}{2})=\frac{\pi}{2}$
5. $\displaystyle x=p\cdot t, \Gamma(s)=p^s\cdot \int_0^{+\infty}t^{s-1}e^{-pt}{\rm d}t$

$\displaystyle \int x^4e^{-x^2}{\rm d}x$

$B$ 函数: $\displaystyle B(p,q)=\int_0^1x^{p-1}\cdot (1-x)^{q-1}{\rm d}x$

1. $B(p,q)=B(q,p)$
2. $\displaystyle B(p,q)=\frac{p-1}{p+q-1}\cdot B(p-1,q)$

$\displaystyle B(p,q)=\frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$

或者说

令 $x=\cos\theta$, 则 $\displaystyle B(p,q)=2\int_0^{\frac{\pi}{2}}\cos^{2p-1}\theta\cdot\sin^{2q-1}\theta\mathrm{d}\theta$


## 二重积分换元公式

$\displaystyle \iint_{(\sigma)}f(x,y)\mathrm{d}x\mathrm{d}y=\iint_{(\sigma')}f(x(u,v),y(u,v))\left| \frac{\partial (x,y)}{\partial (u,v)} \right|\mathrm{d}u\mathrm{d}v$

其中 $\displaystyle J=\frac{\partial (x,y)}{\partial (u,v)}=\begin{vmatrix} x_{u} &x_{v} \\ y_{u} &y_{v} \\\end{vmatrix}=\frac{1}{\displaystyle \frac{\partial (u,v)}{\partial (x,y)}}=\frac{1}{\begin{vmatrix} u_{x} &u_{y} \\ v_{x} &v_{y} \\\end{vmatrix}}$

即使 $J=0$ 在某些点或某条直线上为零, 此式依然成立.

其中, 对于极坐标 $\begin{cases} x=\rho\cos\theta \\ y=\rho\sin\theta \end{cases}$ 有 $|J|=\rho$

其中, 对于广义极坐标 $\begin{cases} x=a\rho\cos\theta \\ y=b\rho\sin\theta \end{cases}$ 有 $|J|=ab\rho$


## 三重积分换元公式

同理有

$\displaystyle \iiint_{(V)}f(x,y,z)\mathrm{d}x\mathrm{d}y\mathrm{d}z=\iiint_{(V')}f(x(u,v,w),y(u,v,w),z(u,v,w))\left| \frac{\partial (x,y,z)}{\partial (u,v,w)} \right|\mathrm{d}u\mathrm{d}v\mathrm{d}w$

其中 $\displaystyle J=\frac{\partial (x,y,z)}{\partial (u,v,w)}=\begin{vmatrix} x_{u} &x_{v} &x_{w} \\ y_{u} &y_{v} &y_{w} \\ z_{u} &z_{v} &z_{w} \\\end{vmatrix}=\frac{1}{\displaystyle \frac{\partial (u,v,w)}{\partial (x,y,z)}}=\frac{1}{\begin{vmatrix} u_{x} &u_{y} &u_{z} \\ v_{x} &v_{y} &v_{z} \\ w_{x} &w_{y} &w_{z} \\\end{vmatrix}}$

对于柱面坐标 $\begin{cases} x=\rho\cos\theta \\ y=\rho\sin\theta \\ z=z \end{cases}$

有 $\displaystyle J=\frac{\partial (x,y,z)}{\partial (\rho,\theta,z)}=\begin{vmatrix} \cos\theta &-\rho\sin\theta &0 \\ \sin\theta &\rho\cos\theta &0 \\ 0 &0 &1 \\\end{vmatrix}=\rho$

对于球面坐标 $\begin{cases} x=r\sin\varphi\cos\theta \\ y=r\sin\varphi\sin\theta \\ z=r\cos\varphi \end{cases}, (0\leqslant \varphi\leqslant \pi, 0\leqslant \theta\leqslant 2\pi)$

有 $\displaystyle J=\frac{\partial (x,y,z)}{\partial (r,\varphi,\theta)}=\begin{vmatrix} \sin\varphi\cos\theta &r\cos\varphi\cos\theta &-r\sin\varphi\cos\theta \\ \sin\varphi\sin\theta &r\cos\varphi\sin\theta &r\sin\varphi\cos\theta \\ \cos\varphi &-r\sin\varphi &0 \\\end{vmatrix}=r^{2}\sin\varphi$


## 变限积分

我们可以用变限积分来表示函数 $f(x)$ 的其中一个父函数

$\varphi(x)=\displaystyle\int_a^xf(t){\rm d}t=F(x)-F(a)$

**变限积分求导:**

$(\displaystyle\int_a^xf(t){\rm d}t)'=f(x)$

$(\displaystyle\int_x^af(t){\rm d}t)'=-f(x)$

**复合变限积分求导:**

$(\displaystyle\int_a^{g(x)}f(t){\rm d}t)'=g'(x)f(g(x))$

证明:

$\displaystyle\int_a^{g(x)}f(t){\rm d}t=\frac{\displaystyle {\rm d}\int_a^{u}f(t){\rm d}t}{{\rm d}u}\cdot \frac{{\rm d}u}{{\rm d}x}=g'(x)f(g(x))$, 其中 $u=g(x)$

**双复合变限积分求导:**

$(\displaystyle\int_{h(x)}^{g(x)}f(t){\rm d}t)'=g'(x)f(g(x))-h'(x)f(h(x))$

**更广泛的变限积分求导:**

对于 $(\displaystyle\int_{f(x)}^{g(x)}f(x,t){\rm d}t)'$,  要把 $x$ 提出去, 对 $t$ 求积分, 可以把 $x$ 看做一个常数.

即 $(\displaystyle\int_{f(x)}^{g(x)}xf(t){\rm d}t)'=(x\int_{f(x)}^{g(x)}f(t){\rm d}t)'$


## 含参积分

$\displaystyle F(y)=\int_a^bf(x,y){\rm d}x$, 记 $D=[a,b]\times [c,d]$

为含参积分, 含有参数 $y$.

**连续性:** 若 $f\in C(D)$, 则 $F\in C[c,d]$

$\displaystyle \lim_{y \to y_0}F(y)=F(y_0)$

$\displaystyle \lim_{y \to y_0}\int_{a}^{b}f(x,y)\mathrm{d}x=\int_{a}^{b}[\lim_{y \to y_0}f(x,y)]\mathrm{d}x$

**可导性:** 若 $f\in C(D), f_{y}\in C(D)$, 则有可导性, 并且导数是连续的

$\displaystyle \frac{{\rm d}\displaystyle\int_a^bf(x,y){\rm d}x}{{\rm d}y}=\int_a^b\frac{\partial f(x,y)}{\partial y}{\rm d}x$

$\displaystyle \frac{{\rm d}\displaystyle\int_{a(y)}^{b(y)}f(x,y){\rm d}x}{{\rm d}y}=\int_{a(y)}^{b(y)}\frac{\partial f(x,y)}{\partial y}{\rm d}x+b'(y)f(b(y), y)-a'(y)f(a(y), y)$

可以和变限积分类比.

**可积性:**

$\displaystyle \int_c^d(\int_a^bf(x,y){\rm d}x){\rm d}y=\int_a^b(\int_c^d f(x,y){\rm d}y){\rm d}x$

对应有两种题型:

1. $\displaystyle \int_{0}^{1}\frac{x^{b}-x^{a}}{\ln x}\mathrm{d}x=\int_{0}^{1}\mathrm{d}x\int_{a}^{b}x^{y}\mathrm{d}y$
2. $\displaystyle \int_{0}^{+\infty}e^{-\frac{x^{2}}{2}}\mathrm{d}x=\sqrt{\int_{0}^{+\infty}e^{-\frac{x^{2}}{2}}\mathrm{d}x\int_{0}^{+\infty}e^{-\frac{y^{2}}{2}}\mathrm{d}y}=\sqrt{\int_{0}^{+\infty}e^{-\frac{x^{2}+y^{2}}{2}}\mathrm{d}x\mathrm{d}y}$


## 第Ⅰ型曲线积分

标量函数的曲线积分, 对应物理中的不均匀密度绳子的质量问题.

对于 $\Gamma:\begin{cases} x=x(t) \\ y=y(t) \\ z=z(t) \\\end{cases}, t\in [\alpha,\beta]$

$\displaystyle\int_\Gamma f(x,y,z){\rm d}s=\int_\alpha^\beta f(x(t),y(t),z(t))\sqrt{x'(t)^2+y'(t)^2+z'(t)^2}{\rm d}t$

要注意应该保证 $\alpha<\beta$. 其中, $\sqrt{x'(t)^2+y'(t)^2+z'(t)^2}{\rm d}t$ 代表着曲线长度的微分.

对于极坐标变换来说, $\displaystyle \sqrt{x'(t)^2+y'(t)^2}=\sqrt{\rho(\theta)^{2}+\rho'(\theta)^{2}}$

与重积分不同的是, 这里的 $\Gamma$ 可以直接带入, 用于简化计算.


## 第Ⅰ型曲面积分

标量函数的曲面积分, 对应物理中的不均匀密度曲面的质量问题.

对于 $\Gamma:\begin{cases} x=x(t) \\ y=y(t) \\ z=z(t) \\\end{cases}, t\in [\alpha,\beta]$

因为 $\displaystyle \vec{r}_u=(\frac{\partial x}{\partial u}, \frac{\partial y}{\partial u}, \frac{\partial z}{\partial u}), \vec{r}_v=(\frac{\partial x}{\partial v}, \frac{\partial y}{\partial v}, \frac{\partial z}{\partial v}), \vec{r}_u\times\vec{r}_v=\begin{vmatrix}i&j&k\\\frac{\partial x}{\partial u}&\frac{\partial y}{\partial u}&\frac{\partial z}{\partial u}\\\frac{\partial x}{\partial v}&\frac{\partial y}{\partial v}&\frac{\partial z}{\partial v}\end{vmatrix}$

记 $\displaystyle J_1=\frac{\partial (y, z)}{\partial (u, v)}, J_2=\frac{\partial (z, x)}{\partial (u, v)}, J_3=\frac{\partial (x, y)}{\partial (u, v)}$

由叉乘定义可知微元面积为 $\displaystyle \mathrm{d}S=|\vec{r}_u\times\vec{r}_v|\Delta u\Delta v=\sqrt{J_1^2+J_2^2+J_3^2}\Delta u\Delta v$

$\displaystyle \iint_{\Sigma}f(x,y,z){\rm d}S=\iint_{D_{uv}}f(x(u,v),y(u,v),z(u,v))\sqrt{J_1^2+J_2^2+J_3^2}{\rm d}u{\rm d}v$

对于 $z=z(x,y)$ 的情况,

$\displaystyle \iint_{\Sigma}f(x,y,z){\rm d}S=\iint_{D_{xy}}f(x,y,z(x,y))\sqrt{1+z_x^2+z_y^2}{\rm d}x{\rm d}y$

对于球面坐标系中半径为 $a$ 的球面,

$\displaystyle \iint_{\Sigma}f(x,y,z){\rm d}S=\iint_{D_{xy}}f(x(\varphi,\theta),y(\varphi,\theta),z(\varphi,\theta))a^{2}\sin\varphi{\rm d}\varphi{\rm d}\theta$


## 第Ⅱ型曲线积分

向量函数的曲线积分, 对应物理中的变力做功问题.

因为有

$\displaystyle\vec{\tau}=\frac{\{x'(t),y'(t),z'(t)\}}{\sqrt{x'(t)^2+y'(t)^2+z'(t)^2}}=\{\cos\alpha,\cos\beta,\cos\gamma\}$

$\displaystyle\vec{\tau}\cdot {\rm d}s=\{\cos\alpha,\cos\beta,\cos\gamma\}{\rm d}s=\{{\rm d}x,{\rm d}y,{\rm d}z\}$ 

其中 $\mathrm{d}s=\sqrt{(\mathrm{d}x)^{2}+(\mathrm{d}y)^{2}+(\mathrm{d}z)^{2}}=\sqrt{x'(t)^2+y'(t)^2+z'(t)^2}{\rm d}t$

所以

$\displaystyle\int\vec{F}\cdot \vec{\tau}{\rm d}s=\int_\alpha^\beta [P(x,y,z){\rm d}x+Q(x,y,z){\rm d}x+R(x,y,z){\rm d}z]$

可以经过换元, 以 $\vec{F}=\{P,0,0\}$ 为例子

$\displaystyle\int_{(C)} P(x,y,z){\rm d}x=\int_\alpha^\beta P(x(t),y(t),z(t))x'(t){\rm d}t$

它和第Ⅰ型曲线积分的联系:

$\displaystyle \int_{(C)}\vec{F}\cdot \mathrm{d}\vec{s}$ 是第二型曲线积分, 可以转化为 $\displaystyle \int_{(C)}\vec{F}\cdot \vec{\tau}{\rm d}s$ 这样的第一型曲线积分.

即 $\displaystyle \int_{(C)}\vec{F}\cdot \vec{\tau}{\rm d}s=\int_{(C)}(P\cos\alpha+Q\cos\beta+R\cos\gamma)\mathrm{d}s$


## 第Ⅱ型曲面积分

向量函数的曲线积分, 对应物理中的矢量场通量问题.

我们已经有

$\displaystyle \vec{n}=\frac{\vec{r}_u\times\vec{r_v}}{|\vec{r}_u\times\vec{r_v}|}=\frac{1}{\sqrt{EG-F^2}}\{\frac{\partial (y,z)}{\partial (u,v)},\frac{\partial (z,x)}{\partial (u,v)},\frac{\partial (x,y)}{\partial (u,v)}\}$

${\rm d}S=\sqrt{J_1^2+J_2^2+J_3^2}{\rm d}u{\rm d}v=\sqrt{EG-F^2}{\rm d}u{\rm d}v$

将第Ⅱ型曲面积分记作

$\displaystyle \iint_{\Sigma}\vec{F}\cdot {\rm d}\vec{S}=\iint_{(S)}P(x,y,z)\mathrm{d}y\land \mathrm{d}z+P(x,y,z)\mathrm{d}z\land \mathrm{d}x+P(x,y,z)\mathrm{d}x\land \mathrm{d}y$

其中, $\mathrm{d}x\land \mathrm{d}y$ 这类写法代表其是有向的, 当法向量 $\vec{n}$ 与 $z$ 轴成锐角时, $\mathrm{d}x\land \mathrm{d}y=\mathrm{d}x\mathrm{d}y$; 当法向量 $\vec{n}$ 与 $z$ 轴成钝角时, $\mathrm{d}x\land \mathrm{d}y=-\mathrm{d}x\mathrm{d}y$; 当法向量 $\vec{n}$ 与 $z$ 轴成直角时, $\mathrm{d}x\land \mathrm{d}y=0$.

那么我们就可以将第Ⅱ型曲面积分化为二重积分

$\displaystyle \iint_{\Sigma}\vec{F}\cdot {\rm d}\vec{S}=\iint_{\Sigma}\vec{F}\cdot \vec{n}{\rm d}S=\iint_{D_{uv}}[P(x(u,v),y(u,v),z(u,v))\frac{\partial (y,z)}{\partial (u,v)}+Q(x(u,v),y(u,v),z(u,v))\frac{\partial (z,x)}{\partial (u,v)}+R(x(u,v),y(u,v),z(u,v))\frac{\partial (x,y)}{\partial (u,v)}]{\rm d}u{\rm d}v$

这里依然要注意方向问题, 因为 $\displaystyle \vec{n}=\frac{1}{\sqrt{EG-F^2}}\{\frac{\partial (y,z)}{\partial (u,v)},\frac{\partial (z,x)}{\partial (u,v)},\frac{\partial (x,y)}{\partial (u,v)}\}$ 或 $\displaystyle \vec{n}=\frac{1}{\sqrt{EG-F^2}}\{-\frac{\partial (y,z)}{\partial (u,v)},-\frac{\partial (z,x)}{\partial (u,v)},-\frac{\partial (x,y)}{\partial (u,v)}\}$ 

或者化为第Ⅰ型曲面积分

$\displaystyle \iint_{\Sigma}\vec{F}\cdot {\rm d}\vec{S}=\iint_{\Sigma}\vec{F}\cdot \vec{n}{\rm d}S=\iint_{(S)}\frac{1}{\sqrt{J_1^2+J_2^2+J_3^2}}[P(x(u,v),y(u,v),z(u,v))\frac{\partial (y,z)}{\partial (u,v)}+Q(x(u,v),y(u,v),z(u,v))\frac{\partial (z,x)}{\partial (u,v)}+R(x(u,v),y(u,v),z(u,v))\frac{\partial (x,y)}{\partial (u,v)}]{\rm d}S$

注意一些常用的转换, 如 $\mathrm{d}x\mathrm{d}y=\cos\gamma\mathrm{d}S$


## 三大积分公式

三大积分公式: Green公式, Gauss 公式, 斯托克斯公式

* Green公式 $\displaystyle \oint_\Gamma P\mathrm{d}x+Q\mathrm{d}y=\iint_{D_{xy}}\left( \frac{\partial Q}{\partial x} -\frac{\partial P}{\partial y}  \right)\mathrm{d}x\mathrm{d}y$
* Gauss 公式 $\displaystyle \iiint \left( \frac{\partial P}{\partial x} +\frac{\partial Q}{\partial y} +\frac{\partial R}{\partial z}  \right)\mathrm{d}V=\oiint_\Sigma P\mathrm{d}y\mathrm{d}z+Q\mathrm{d}z\mathrm{d}x+R\mathrm{d}x\mathrm{d}y$
* 斯托克斯公式 $\displaystyle \oint_\Gamma P\mathrm{d}x+Q\mathrm{d}y+R\mathrm{d}z=\iint_\Sigma \begin{vmatrix}	\cos\alpha &\cos\beta &\cos\gamma \\\frac{\partial }{\partial x}  &\frac{\partial }{\partial y}  &\frac{\partial }{\partial z}  \\	P &Q &R \end{vmatrix}\mathrm{d}S$

Green 公式和 Stokes 公式本质上是一样的, 只不过一个是二维情况一个是三维情况. 令 $\cos\gamma=1$, 则 Stokes 公式退化为 Green 公式.


## Green公式

$\displaystyle \oint_\Gamma P\mathrm{d}x+Q\mathrm{d}y=\iint_{D_{xy}}\left( \frac{\partial Q}{\partial x} -\frac{\partial P}{\partial y}  \right)\mathrm{d}x\mathrm{d}y$

1. $D_{xy}$ 是连通的.
2. $P(x,y), Q(x,y)$ 在 $D_{xy}$ 上连续可导.
3. $\Gamma$ 取正向, 即封闭区域始终在左边.

**路径无关性质:**

1. $\displaystyle \frac{\partial Q}{\partial x}=\frac{\partial P}{\partial y}$
2. $\displaystyle \oint_{\Gamma}P\mathrm{d}x+Q\mathrm{d}y=0$
3. $\displaystyle \int_{\Gamma}P\mathrm{d}x+Q\mathrm{d}y$ 只与 $\Gamma$ 的起点和终点有关 (与路径无关)
4. $P\mathrm{d}x+Q\mathrm{d}y$ 是一个恰当微分, 即 $\exist u=u(x,y)$ 使 $\mathrm{d}u=P\mathrm{d}x+Q\mathrm{d}y$ 即 $\displaystyle P=\frac{\partial u}{\partial x}, Q=\frac{\partial u}{\partial y}$


## Gauss 公式

$\displaystyle \oiint_\Sigma P\mathrm{d}y\land\mathrm{d}z+Q\mathrm{d}z\land\mathrm{d}x+R\mathrm{d}x\land\mathrm{d}y=\iiint_{\Omega} \left( \frac{\partial P}{\partial x} +\frac{\partial Q}{\partial y} +\frac{\partial R}{\partial z}  \right)\mathrm{d}V$

方向为封闭曲面向外.

用 nabla 算子表示:

$\displaystyle \iiint_{(V)}\nabla \cdot \vec{A}\mathrm{d}V=\oiint_{(S)}\vec{A}\cdot \mathrm{d}\vec{S}$

其中 $\displaystyle \text{div}\vec{A}=\nabla \cdot \vec{A}=\frac{\partial P}{\partial x} +\frac{\partial Q}{\partial y} +\frac{\partial R}{\partial z}$ 又称为散度.

散度 $\displaystyle \text{div}\vec{A}=\lim_{(\Delta V) \to M}\frac{1}{\Delta V}\oiint_{(\Delta S)}\vec{A}(M)\cdot \mathrm{d}\vec{S}$

可用中值定理和连续性证明它们相等.

性质:

- $\text{div}(C\vec{A})=C\text{div}(\vec{A})$
- $\text{div}(\vec{A}+\vec{B})=\text{div}(\vec{A})+\text{div}(\vec{B})$
- $\text{div}(u \vec{A})=u\text{div}\vec{A}+\nabla u\cdot \vec{A}$


## Stokes 公式

$\displaystyle \iint_\Sigma \begin{vmatrix}	\cos\alpha &\cos\beta &\cos\gamma \\\frac{\partial }{\partial x}  &\frac{\partial }{\partial y}  &\frac{\partial }{\partial z}  \\	P &Q &R \end{vmatrix}\mathrm{d}S=\oint_\Gamma P\mathrm{d}x+Q\mathrm{d}y+R\mathrm{d}z$

如果 $\cos\alpha, \cos\beta, \cos\gamma$ 取确定值, 就变成了第Ⅰ型曲面积分, 如果不取确定值, 就是第Ⅱ型曲面积分.

方向为右手螺旋法则.

用 nabla 算子表示:

$\displaystyle \oint_{(C)}\vec{A}\cdot \mathrm{d}\vec{s}=\iint_{(S)}(\nabla \times \vec{A})\cdot \mathrm{d}\vec{S}=\iint_{(S)}(\nabla \times \vec{A})\cdot \vec{\tau}\mathrm{d}S$

其中 $\text{rot}\vec{A}=\nabla \times \vec{A}$ 称为旋度

证明的关键在于, 把空间曲线积分转化为平面曲线积分, 再用 Green 公式.



