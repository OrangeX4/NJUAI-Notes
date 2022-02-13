<style>
.title-box {
    border-style: solid;
    border-width: 1px;
    padding: 16px;
    padding-bottom: 32px;
}
</style>

<div class="title-box">
    <div>
        <b style="float: left;">Optimization Methods</b>
        <b style="float: right;">Fall 2021</b>
    </div>
    <h1 style="text-align: center;">Homework 3</h1>
    <div>
        <span style="float: left;"><i>Instructor:</i> Lijun Zhang</span>
        <span style="float: right;"><i>Name:</i> 方盛俊, <i>StudentId:</i> 201300035</span>
    </div>
</div>

## Notice

- The submission email is: **zhangzhenyao@lamda.nju.edu.cn**.
- Please use the provided Latex file as a template.
- If you are not familiar with LaTeX, you can also use Word to generate a **PDF** file.


## Problem 1: One inequality constraint

对于

$$
\begin{aligned}
\min \quad & c^{T}x \\
\mathrm{s.t.} \quad & f(x)\leqslant 0
\end{aligned}
$$

我们有其 Lagrange 函数为 $L(x, \lambda)=c^{T}x+\lambda f(x)$, 其中 $\lambda\geqslant 0$

则其对偶函数为 $\displaystyle g(\lambda)=\inf_{x}(c^{T}x+\lambda f(x))=-\lambda\sup_{x}(-\frac{c^{T}}{\lambda} x-f(x))$

由 $\displaystyle f^{*}(y)=\sup_{x}(y^{T}x-f(x))$ 可知

我们有 $\displaystyle g(\lambda)=-\lambda f^{*}(-\frac{c}{\lambda})$

即可转化为对偶问题

$$
\begin{aligned}
\max \quad & g(\lambda)=-\lambda f^{*}(-\frac{c}{\lambda}) \\
\mathrm{s.t.} \quad & \lambda \geqslant 0
\end{aligned}
$$


## Problem 2: KKT conditions

**(1)**

Lagrange 函数为:

$\displaystyle L(x_1, x_2, \lambda_1, \lambda_2)=x_1^{2}+x_2^{2}+\lambda_1(x_1-1)^{2}+\lambda_1(x_2-1)^{2}-2\lambda_1+\lambda_2(x_1-1)^{2}+\lambda_2(x_2+1)^{2}-2\lambda_2$

**(2)**

有强对偶性, 我们可以找到点 $x=(1, 0)$, 即 $x_1=1, x_2=0$ 满足

$(x_1-1)^{2}+(x_2-1)^{2}=1<2$ 和 $(x_1-1)^{2}+(x_2+1)^{2}=1<2$ 成立

并且原问题是一个凸问题

即我们有 Slater 条件成立, 则这个问题保持强对偶性.

**(3)**

KKT 条件为:

$$
\begin{aligned}
(x_1^{*}-1)^{2}+(x_2^{*}-1)^{2}\leqslant 2 \\
(x_1^{*}-1)^{2}+(x_2^{*}+1)^{2}\leqslant 2 \\
\lambda_1^{*}\geqslant 0 \\ 
\lambda_2^{*}\geqslant 0 \\
x_1^{*2}+\lambda_1^{*}(x_1^{*}-1)+\lambda_2^{*}(x_1^{*}-1)=0 \\
x_2^{*2}+\lambda_1^{*}(x_2^{*}-1)+\lambda_2^{*}(x_2^{*}+1)=0 \\
\end{aligned}
$$


## Problem 3: Equality Constrained Least-squares

**(1)**

对应的 Lagrange 函数为

$\displaystyle L(x, v)=\frac{1}{2}\|Ax-b\|_{2}^{2}+v^{T}(Gx-h)=\frac{1}{2}x^{T}A^{T}Ax+(v^{T}G-b^{T}A)x-v^{T}h+\frac{1}{2}b^{T}b$

因为 $L(x,v)$ 是二次凸函数, 则求解

$\nabla_{x} L(x,v)=A^{T}Ax-A^{T}b+G^{T}v=0$ 即有 $A^{T}Ax=A^{T}b-G^{T}v$

再由 $A$ 的 rank 为 $n$ 可知 $A^{T}A$ 的 rank 也为 $n$, 则可以求逆, 则 $x=(A^{T}A)^{-1}(A^{T}b-G^{T}v)$

代入可知对偶函数为 $\displaystyle g(v)=\frac{1}{2}(v^{T}G-b^{T}A)(A^{T}A)^{-1}(A^{T}b-G^{T}v)-v^{T}h+\frac{1}{2}b^{T}b$

则转化为对偶问题

$$
\begin{aligned}
\max \quad & g(v)=\frac{1}{2}(v^{T}G-b^{T}A)(A^{T}A)^{-1}(A^{T}b-G^{T}v)-v^{T}h+\frac{1}{2}b^{T}b \\
\end{aligned}
$$

**(2)**

使用 Lagrange 函数再对 $v$ 求偏导得 $Gx-h=0$ 即 $Gx=h$

那么我们有 $\displaystyle Gx=G(A^{T}A)^{-1}(b-G^{T}v)=G(A^{T}A)^{-1}b-G(A^{T}A)^{-1}G^{T}v=h$

即有 $G(A^{T}A)^{-1}G^{T}v=G(A^{T}A)^{-1}b-h$

由于 $(A^{T}A)^{-1}$ 为 $n\times n$ 的满秩矩阵, 因此 $G(A^{T}A)^{-1}G^{T}$ 也为 $p\times p$ 的满秩矩阵, 存在逆

因此 $v=[G(A^{T}A)^{-1}G^{T}]^{-1}[G(A^{T}A)^{-1}b-h]$

再代入式子可得 $x^{*}=(A^{T}A)^{-1}(b-G^{T}[G(A^{T}A)^{-1}G^{T}]^{-1}[G(A^{T}A)^{-1}b-h])$

对于对偶问题, 我们对 $g(v)$ 求偏导, 有

$\displaystyle \nabla_{v}g(v)=-G(A^{T}A)^{-1}(G^{T}v-A^{T}b)-h=0$

则我们有 $\displaystyle G(A^{T}A)^{-1}(G^{T}v-A^{T}b)=-h$

则最后 $\displaystyle v^{*}=[G(A^{T}A)^{-1}G^{T}]^{-1}[G(A^{T}A)^{-1}b-h]$


## Problem 4: Negative-entropy Regularization

对于 $\displaystyle x\in \Delta^{n}=\{x|\sum_{i=1}^{n}x_{i}=1, x_{i}\geqslant 0, i=1,2,\cdots,n\}$

则问题可以表达为

$$
\begin{aligned}
\argmin \quad & b^{T}x+c\cdot \sum_{i=1}^{n}x_{i}\ln x_{i} \\
\mathrm{s.t.} \quad & -x_{i}\leqslant 0 \\
& \sum_{i=1}^{n}x_{i}-1=0 \\
\end{aligned}
$$

对应的 Lagrange 函数为

$\displaystyle L(x, \lambda, v)=b^{T}x+c\cdot \sum_{i=1}^{n}x_{i}\ln x_{i}-\sum_{i=1}^{n}\lambda_{i} x_{i}+v\sum_{i=1}^{n}x_{i}-v$

对应的对偶函数为

$
\begin{aligned}
g(\lambda, v)
&=\inf_{x}(b^{T}x+c\cdot \sum_{i=1}^{n}x_{i}\ln x_{i}-\sum_{i=1}^{n}\lambda_{i} x_{i}+v\sum_{i=1}^{n}x_{i}-v) \\
&=-c\sum_{i=1}^{n}\sup_{x}(\frac{1}{c}(\lambda_{i}-b_{i}-v)x_{i}-x_{i}\ln x_{i})-v \\
&=-ce^{-\frac{v}{c}-1}\sum_{i=1}^{n}e^{\frac{1}{c}(\lambda_{i}-b_{i})}-v
\end{aligned}
$

则我们转化为对偶问题

$$
\begin{aligned}
\argmax \quad & -ce^{-\frac{v}{c}-1}\sum_{i=1}^{n}e^{\frac{1}{c}(\lambda_{i}-b_{i})}-v \\
\mathrm{s.t.} \quad & \lambda_{i}\geqslant 0, \quad i=1,2,\cdots,n
\end{aligned}
$$

因为我们很容易找到点 $\displaystyle x_{i}=\frac{1}{n}, i=1,2,\cdots,n$ 满足 $\displaystyle -x_{i}< 0, \sum_{i=1}^{n}x_{i}-1=0$

因此有强对偶性, 最优对偶间隙为零.

我们固定 $\lambda$, 对 $v$ 求导数并等于零有

$\displaystyle e^{-\frac{v}{c}-1}\sum_{i=1}^{n}e^{\frac{1}{c}(\lambda_{i}-b_{i})}-1=0$ 即 $\displaystyle v^{*}=c\ln(\sum_{i=1}^{n}e^{\frac{1}{c}(\lambda_{i}-b_{i})})-c$

将 $v$ 的最优值代入对偶问题可得

$$
\begin{aligned}
\argmax \quad & -c\ln(\sum_{i=1}^{n}e^{\frac{1}{c}(\lambda_{i}-b_{i})}) \\
\mathrm{s.t.} \quad & \lambda_{i}\geqslant 0, \quad i=1,2,\cdots,n
\end{aligned}
$$

这是一个非负约束的几何规划问题 (凸优化问题)

则我们求导可知该函数总是递减的,

因此我们可以求解出 $\lambda_{i}^{*}=0, i=1,2,\cdots,n$

可得 $\displaystyle v^{*}=c\ln(\sum_{i=1}^{n}e^{\frac{1}{c}(\lambda_{i}-b_{i})})-c=c\ln(\sum_{i=1}^{n}e^{-\frac{b_{i}}{c}})-c$

进而根据 KKT 条件:

$$
\begin{aligned}
\sum_{i=1}^{n}x_{i}^{*}-1=0 \\
x_{i}^{*}\geqslant 0 &, \quad i=1,2,\cdots,n \\
\lambda_{i}^{*}\geqslant 0 &, \quad i=1,2,\cdots,n \\
\lambda_{i}^{*}x_{i}^{*}= 0 &, \quad i=1,2,\cdots,n \\
b_{i}+c\ln x_{i}^{*}+c-\lambda_{i}^{*}+v^{*}= 0 &, \quad i=1,2,\cdots,n \\
\end{aligned}
$$

即有 $\displaystyle \frac{b_{i}}{c}+\ln x_{i}^{*}+\ln(\sum_{i=1}^{n}e^{-\frac{b_{i}}{c}})=0$

最后有 $\displaystyle x_{i}=\frac{e^{-\frac{b_{i}}{c}}}{\sum_{i=1}^{n}e^{-\frac{b_{i}}{c}}}, i=1,2,\cdots,n$


## Problem 5: Support Vector Machines

**(1)**

引入 $u_{i}$ 后变为

$$
\begin{aligned}
\min \quad & \sum_{i=1}^{n}l(u_{i})+\frac{\lambda}{2}\|w\|_{2}^{2} \\
\mathrm{s.t.} \quad & u_{i}=y_{i}(w^{T}x_{i}+b) & i=1,2,\cdots,n
\end{aligned}
$$

**(2)**

其 Lagrange 函数为

$
\begin{aligned}
L(u, w, b, v)
&=\sum_{i=1}^{n}l(u_{i})+\frac{\lambda}{2}\|w\|_{2}^{2}+\sum_{i=1}^{n}v_{i}(u_{i}-y_{i}(w^{T}x_{i}+b)) \\
&=\sum_{i=1}^{n}l(u_{i})+\sum_{i=1}^{n}\frac{\lambda}{2}w_{i}^{2}+\sum_{i=1}^{n}v_{i}(u_{i}-y_{i}(w^{T}x_{i}+b)) \\
&=\sum_{i=1}^{n}[l(u_{i})+\frac{\lambda}{2}w_{i}^{2}+v_{i}u_{i}-v_{i}y_{i}w^{T}x_{i}-v_{i}y_{i}b] \\
&=\sum_{i=1}^{n}[l(u_{i})+v_{i}u_{i}]+\frac{\lambda}{2}\|w\|_{2}^{2}-\sum_{i=1}^{n}v_{i}y_{i}x_{i}^{T}w-by^{T}v \\
\end{aligned}
$

因此有对偶函数

$
\begin{aligned}
g(v)
&=\inf_{u, w, b}[\sum_{i=1}^{n}[l(u_{i})+v_{i}u_{i}]+\frac{\lambda}{2}\|w\|_{2}^{2}-\sum_{i=1}^{n}v_{i}y_{i}x_{i}^{T}w-by^{T}v] \\
&=-\sum_{i=1}^{n}\sup_{u_{i}}[-v_{i}u_{i}-l(u_{i})]+\inf_{w}[\frac{\lambda}{2}\|w\|_{2}^{2}-\sum_{i=1}^{n}v_{i}y_{i}x_{i}^{T}w]-\sup_{b}by^{T}v \\
&=-\sum_{i=1}^{n}l^{*}(-v_{i})+\inf_{w}[\frac{\lambda}{2}\|w\|_{2}^{2}-\sum_{i=1}^{n}v_{i}y_{i}x_{i}^{T}w]-\sup_{b}by^{T}v \\
&=\sum_{i=1}^{n}v_{i}+\frac{1}{2\lambda}\sum_{i=1}^{n}\sum_{j=1}^{n}v_{i}v_{j}y_{i}y_{j}x_{i}^{T}x_{j} \\
\end{aligned}
$

其中要满足 $0\leqslant v_{i}\leqslant 1, y^{T}v=0$

因此可以转化为对偶问题:

$$
\begin{aligned}
\max \quad & g(v)=\sum_{i=1}^{n}v_{i}+\frac{1}{2\lambda}\sum_{i=1}^{n}\sum_{j=1}^{n}v_{i}v_{j}y_{i}y_{j}x_{i}^{T}x_{j} \\
\mathrm{s.t.} \quad & y^{T}v=0 \\
& 0\leqslant v_{i}\leqslant 1 & i=1,2,\cdots,n \\
\end{aligned}
$$

**(3)**

对应的 KKT 条件为:

$$
\begin{aligned}
u_{i}=y_{i}(w^{T}x_{i}+b) &, \quad i=1,2,\cdots,n \\
\sum_{i=1}^{n}\nabla_{u}l(u_{i})+\sum_{i=1}^{n}v_{i}=0 \\
\lambda w-\sum_{i=1}^{n}v_{i}y_{i}x_{i}=0 \\
\sum_{i=1}^{n}v_{i}y_{i}=0 \\
\sum_{i=1}^{n}(u_{i}-y_{i}(w^{T}x_{i}+b))=0 \\
\end{aligned}
$$

其中 $\nabla_{u}l(u_{i})=\begin{cases} -1, & u_{i}< 1 \\ 0, & u_{i}>1 \end{cases}$

