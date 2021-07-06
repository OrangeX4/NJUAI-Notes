# 大一下数分期中考试范围

* 简单的空间解析几何
* 多元函数微分学 
  * 重极限, 累次极限, 偏导数, 重积分, 隐函数...
* 多元微分在几何上的应用 
  * 切平面和法线
  * 切线和法平面
* 泰勒展开求函数极值
  * (二元函数的许多性质是由一元函数泰勒展开带出来的)
  * 普通极值
  * 约束极值
  * 连续函数在闭区域上的最值问题
* 方向导数和梯度
* 二重积分和三重积分
  * 二重积分和次序关系较大
  * 要注意对称性
* 含参积分
* 第Ⅰ形曲线曲面积分

## 例一

设 $z=z(x,y)$ 二次可微, 取 $u,v$ 为新的自变量, $w=w(u,v)$ 为新的因变量.

满足 $\displaystyle w=xz-y, u=\frac{x}{y}, v=x$. 

把 $\displaystyle y\frac{\partial^2 z}{\partial y^2}+2\frac{\partial z}{\partial y}=\frac{2}{x}$ 变换成新变量 $w, u, v$ 的方程.

**解:**

我们先将 $w$ 改写一下, $\displaystyle z=\frac{w+y}{x}=\frac{w}{x}+\frac{y}{x}$

$
\begin{aligned}
\therefore \frac{\partial z}{\partial y}
&=\frac{1}{x}+\frac{1}{x}(\frac{\partial w}{\partial u}\cdot \frac{\partial u}{\partial y}+\frac{\partial w}{\partial v}\cdot \frac{\partial v}{\partial y}) \\
&=\frac{1}{x}+\frac{1}{x}(-\frac{x}{y^2}\cdot \frac{\partial w}{\partial u}+0) \\&
=\frac{1}{x}-\frac{1}{y^2}\cdot \frac{\partial w}{\partial u} \\
\end{aligned}
$

$
\begin{aligned}
\therefore \frac{\partial^2z}{\partial y^2}
&=0+2\frac{1}{y^3}\frac{\partial w}{\partial u}-\frac{1}{y^2}(\frac{\partial^2 w}{\partial u^2}\cdot \frac{\partial u}{\partial y}+\frac{\partial^2 w}{\partial v^2}\cdot \frac{\partial v}{\partial y}) \\
&=\frac{2}{y^3}\frac{\partial w}{\partial u}+\frac{x}{y^4}\cdot \frac{\partial^2 w}{\partial u^2} \\
\end{aligned}
$

将两式带入可得

$\displaystyle \frac{2}{y^2}\cdot \frac{\partial w}{\partial u}+\frac{x}{y^3}\cdot \frac{\partial^2 w}{\partial u^2}+\frac{2}{x}-\frac{2}{y^2}\cdot \frac{\partial w}{\partial u}=\frac{2}{x}$

结果是 $\displaystyle \frac{\partial^2 w}{\partial u^2}=0$

**类似的:**

$\displaystyle z=z(x,y), 
\begin{cases}
x=r\cos\theta \\
y=r\sin\theta \\
\end{cases}
$

将 $\displaystyle\frac{\partial^2 z}{\partial x^2}+\frac{\partial^2 z}{\partial y^2}=0$ 转化为关于 $r, \theta$ 的方程.