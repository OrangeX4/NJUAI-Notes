# Cheat Sheet for Physics

## 向量

$A\cdot B=||A||\cdot ||B||\cos\theta$

$A\times (B\times C) = B(A\cdot C)-C(A\cdot B)$

$(A\times B)\cdot C=(C\times A)\cdot B=(B\times C)\cdot A$

$\boldsymbol{F}, \boldsymbol{v}, \boldsymbol{v}=\boldsymbol{\omega}\times\boldsymbol{r}, \boldsymbol{\omega}=\boldsymbol{r}\times\boldsymbol{F}$

$\displaystyle\frac{{\rm d}}{{\rm d}t}[\boldsymbol{u}(t)\cdot\boldsymbol{v}(t)]=\frac{{\rm d}}{{\rm d}t}\boldsymbol{u}(t)\cdot \boldsymbol{v}(t)+\boldsymbol{u}(t)\cdot \frac{{\rm d}}{{\rm d}t}\boldsymbol{v}(t)$

$\displaystyle\frac{{\rm d}}{{\rm d}t}[\boldsymbol{u}(t)\times\boldsymbol{v}(t)]=\frac{{\rm d}}{{\rm d}t}\boldsymbol{u}(t)\times \boldsymbol{v}(t)+\boldsymbol{u}(t)\times \frac{{\rm d}}{{\rm d}t}\boldsymbol{v}(t)$

## 极坐标

![](./image/2021-03-15-22-47-21.png)

任意矢量 $A=A_{\rho}\boldsymbol{e}_{\rho}+A_{\phi}\boldsymbol{e}_{\phi}$

位置矢量 $\boldsymbol{\rho}=\rho\boldsymbol{e}_{\rho}$, 分量和端点坐标分别为 $(\rho,0), (\rho,\phi)$, 并不一致

假设有 $\rho=\rho(t), \phi=\phi(t)$

对单位向量的定义如下, 分别为径向和横向, 本质是对直角坐标做了一个旋转变换

$\because \boldsymbol{e}_{\rho}=\cos\phi i+\sin\phi j$
$\quad\boldsymbol{e}_{\phi}=-\sin\phi i+\cos\phi j$

$\therefore\displaystyle\frac{{\rm d}\boldsymbol{e}_{\rho}}{{\rm d}t}=(-\sin\phi i+\cos\phi j)\dot{\phi}=\dot{\phi}\boldsymbol{e}_{\phi}$
$\quad\displaystyle\frac{{\rm d}\boldsymbol{e}_{\rho}}{{\rm d}t}=(-\cos\phi i-\sin\phi j)\dot{\phi}=-\dot{\phi}\boldsymbol{e}_{\rho}$

$\therefore\displaystyle\dot{\boldsymbol{\rho}}=\frac{{\rm d}}{{\rm d}t}(\rho\boldsymbol{e}_{\rho})=\dot{\rho}\boldsymbol{e}_{\rho}+\rho\dot{\phi}\boldsymbol{e}_{\phi}\quad$ (常常代表速度)
$\quad\displaystyle\ddot{\boldsymbol{\rho}}=(\ddot{\rho}-\rho\dot{\phi^2})\boldsymbol{e}_{\rho}+(\rho\ddot{\phi}+2\dot{\rho}\dot{\phi})\boldsymbol{e}_{\phi}\quad$ (常常代表加速度)

应用于圆周运动, 得

$\dot{\rho}=\rho\dot{\varphi}\boldsymbol{e}_{\varphi}$
$\ddot{\rho}=-\dot{\varphi}^2\rho\boldsymbol{e}_{\rho}+\rho\ddot{\varphi}\boldsymbol{e}_{\varphi}$

角速度大小 $\omega=\dot{\varphi}$

角速度方向使 $\boldsymbol{e}_{\rho}, \boldsymbol{e}_{\varphi}, \boldsymbol{\omega}$ 三者满足右手螺旋关系, 即沿旋转轴方向

那么就有圆周运动速度 $\dot{\boldsymbol{\rho}}=\boldsymbol{\omega}\times\boldsymbol{\rho}$, 且方向为 $\boldsymbol{e}_{\varphi}$ 方向


## Simple Harmonic Oscillation

$
\begin{cases}
\theta=\theta_0\cos\omega t \\
\dot{\theta}=-\omega\theta_0\sin\omega t \\
\end{cases}
$

$x=A\sin\omega t+B\cos\omega t$

$x=A\sin(\omega t+\varphi)$

$x=Ae^{i\omega t}+Be^{-i\omega t}$

$
\begin{aligned}
x(t)
&=x_1(t)+x_2(t)\\
&=A[\cos(\omega_1t+\varphi)+\cos(\omega_2t+\varphi)] \\
&=2A|\cos\frac{\omega_2-\omega_1}{2}t|\cos(\frac{\omega_1+\omega_2}{2}t+\varphi) \\
\end{aligned}
$


## Coriolis

![](./image/2021-03-15-23-39-52.png)

有相对桌面参考系 $S$ 和匀速圆周运动参考系 $S'$

对于固定在 $S'$ 上的一点:

$\because\displaystyle\frac{{\rm d}}{{\rm d}t}\boldsymbol{A}=\boldsymbol{\omega}\times\boldsymbol{A}$

$\therefore{\rm d}\boldsymbol{A}=(\boldsymbol{\omega}\times\boldsymbol{A}){\rm d}t$

若 $\boldsymbol{A}$ 相对 $S'$ 运动, 增量为 ${\rm d}\boldsymbol{A}'$

那么我们有一般关系式

$\displaystyle(\frac{{\rm d}\boldsymbol{A}}{{\rm d}t})_S=(\frac{{\rm d}\boldsymbol{A}}{{\rm d}t})_{S'}+\boldsymbol{\omega}\times\boldsymbol{A}$

或写作符号, $t$ 旁边的一撇只是用来说明参考系的选取

$\displaystyle\frac{{\rm d}}{{\rm d}t}=\frac{{\rm d}}{{\rm d}t'}+\boldsymbol{\omega}\times$

将位置矢量带入得速度

$\displaystyle\frac{{\rm d}\boldsymbol{r}}{{\rm d}t}=\frac{{\rm d}\boldsymbol{r}}{{\rm d}t'}+\boldsymbol{\omega}\times\boldsymbol{r}$

再带入得加速度

$
\begin{aligned}
\displaystyle\frac{{\rm d}\dot{\boldsymbol{r}}}{{\rm d}t}
&=\frac{{\rm d}\dot{\boldsymbol{r}}}{{\rm d}t'}+\boldsymbol{\omega}\times\dot{\boldsymbol{r}} \\
&=\frac{{\rm d}}{{\rm d}t'}(\frac{{\rm d}\boldsymbol{r}}{{\rm d}t'}+\boldsymbol{\omega}\times\boldsymbol{r})+\boldsymbol{\omega}\times(\frac{{\rm d}\boldsymbol{r}}{{\rm d}t'}+\boldsymbol{\omega}\times\boldsymbol{r}) \\
&=\frac{{\rm d}^2\boldsymbol{r}}{{\rm d}t'^2}+2\boldsymbol{\omega}\times\frac{{\rm d}\boldsymbol{r}}{{\rm d}t}+\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r})
\end{aligned}
$

可以看出, 分为三项, 第一项是 $S'$ 中的加速度, 第三项为向心加速度,
而多出来的第二项, 称为科里奥利加速度.

在地球上, 由于重力加速度是相对 $S$ 而言的, 所以有

$\boldsymbol{g}=\boldsymbol{g}_0-2\boldsymbol{\omega}\times\boldsymbol{v}'-\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r})$

科里奥利加速度指向运动方向的右手边


## 伯努利方程

伯努利方程为 $\displaystyle p+\frac{1}{2}\rho v^2+\rho gz=C$, 其中 $C$ 为常量.

可以用于求流体力学里的压强. 同时可以解释伯努利现象.


## 转动惯量

在旋转坐标系中:

* 角速度 $\dot\theta$ 的地位等同于惯性系的速度;
* 角加速度 $\ddot\theta$ 的地位等同于惯性系的加速度; 
* 转动惯量 $\displaystyle I=\int\rho^2{\rm d}m$ 的地位等同于惯性系的质量;
* 力矩 $\boldsymbol{F}\times\boldsymbol{r}$ 的地位等同于惯性系里的力.

转动动能: $\displaystyle E=\frac{1}{2}I\dot\theta^2$

类似牛顿第二定律: $\displaystyle\boldsymbol{F}\times\boldsymbol{r}=I\ddot\theta=\int\rho{\rm d}m \ddot\theta$

圆环以直径为轴旋转时的转动惯量为

$\displaystyle I=2\int_0^\pi\frac{m}{2\pi R}(R\sin\theta)^2{\rm d}\theta=\frac{1}{2}mR^2$

圆球的转动惯量为:

$\displaystyle I=\int{\rm d}m(r\sin\theta)^2=\int\frac{m}{\frac{4}{3}\pi R^3}[2\pi(r\sin\theta)r{\rm d}r{\rm d}\theta](r\sin\theta)^2=\frac{2}{5}mR^2$

木棍沿着中心的转动惯量为:

$\displaystyle I=\int_{-\frac{l}{2}}^{\frac{l}{2}}\frac{m}{l}{\rm d}xx^2=\frac{1}{12}ml^2$

平行轴定理, 可以实现两个不同的平行轴之间转动惯量的转换, 其中 $I_C$ 为经过质心的转轴的转动惯量, $d$ 为两个轴之间的距离:

$I=I_C+md^2$

使用平行轴定理可知, 木棍沿着端点的轴为:

$\displaystyle I=\frac{1}{12}ml^2+m(\frac{l}{2})^2=\frac{1}{3}ml^2$



