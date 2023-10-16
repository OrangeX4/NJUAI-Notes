# 矩阵微积分

## 导数

假定 $f: \mathbb{R}^{n} \to \mathbb{R}^{m}, x \in \text{intdom } f$, 存在矩阵 $Df(x) \in \mathbb{R}^{m \times n}$ 满足

$$
\lim_{z\in \text{dom }f, z\neq x, z \to x} \frac{\left\| f(z)-f(x)-Df(x)(z-x) \right\|_{2}}{\left\| z-x \right\|_{2}} = 0
$$

则称 $Df(x)$ 为 $f$ 在 $x$ 处的 **导数** 或 **Jacobian 矩阵**.

我们将 $z$ 的仿射函数

$$
f(x) + Df(x)(z-x)
$$

称为 $f$ 在 $x$ 处的一次逼近.

可以通过计算偏导数

$$
Df(x)_{ij} = \frac{\partial f_{i}(x)}{\partial x_j}, i = 1, \cdots, m, j = 1,\cdots ,n
$$

来计算导数矩阵.


## 梯度

对于实函数 $f: \mathbb{R}^{n} \to \mathbb{R}$ 来说, 导数 $Df(x)$ 是 $1\times n$ 矩阵, 即行向量, 它的转置是一个列向量, 称为 **梯度**

$$
\nabla f(x) = Df(x)^{\top}
$$

所以求梯度的话, 可以先求出导数, 再转置成为梯度.

## 链式法则

对于 $h(z)=g(f(z))$ 有

$$
Dh(x) = Dg(f(x))Df(x)
$$




