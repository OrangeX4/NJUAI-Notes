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
        <b style="float: left;">矩阵计算</b>
        <b style="float: right;">人工智能学院</b>
    </div>
    <h1 style="text-align: center;">Homework 2</h1>
    <div>
        <span style="float: left;"><i>Instructor:</i> 李宇峰</span>
        <span style="float: right;"><i>Name:</i> 方盛俊, <i>StudentId:</i> 201300035</span>
    </div>
</div>


## 1.

对于 $\forall \alpha, \beta \in R, \forall x, y \in R^{2}$ 有

$
\begin{aligned}
&\quad\ \alpha \otimes (x \oplus y)  \\
& = (\alpha (x_1 + y_1), \alpha (x_2 + y_2 + x_1y_1) + \frac{\alpha(\alpha-1)}{2}(x_1 + y_1)^{2})  \\
& = (\alpha (x_1 + y_1), \alpha (x_2 + y_2) + \frac{\alpha(\alpha-1)}{2}(x_{1}^{2} + y_{1}^{2}) + \alpha x_1y_1 + \alpha(\alpha-1) x_{1} y_{1})  \\
& = (\alpha x_1 + \alpha y_1, \alpha x_2 + \frac{\alpha(\alpha-1)}{2}x_1^{2} + \alpha y_2 + \frac{\alpha(\alpha-1)}{2}y_1^{2} + \alpha^{2} x_1 y_1)  \\
& = (\alpha x_1, \alpha x_2 + \frac{\alpha(\alpha-1)}{2}x_1^{2}) \oplus (\alpha y_1, \alpha y_2 + \frac{\alpha(\alpha-1)}{2}y_1^{2})  \\
& = (\alpha \otimes x) \oplus (\alpha \otimes y)
\end{aligned}
$

$
\begin{aligned}
&\quad\ (\alpha + \beta) \otimes x  \\
& = ((\alpha+\beta)x_1, (\alpha+\beta)x_2 + \frac{(\alpha+\beta)((\alpha+\beta)-1)}{2}x_1^{2})  \\
& = ((\alpha+\beta)x_1, \alpha x_{2} + \beta x_{2} + \frac{\alpha (\alpha - 1) + \beta (\beta - 1) + 2 \alpha \beta}{2}x_1^{2})  \\
& = (\alpha x_1 + \beta x_1, \alpha x_2 + \frac{\alpha(\alpha-1)}{2}x_1^{2} + \beta x_2 + \frac{\beta(\beta-1)}{2}x_1^{2} + \alpha \beta x_1^{2})  \\
& = (\alpha x_1, \alpha x_2 + \frac{\alpha(\alpha-1)}{2}x_1^{2}) \oplus (\beta x_1, \beta x_2 + \frac{\beta(\beta-1)}{2}x_1^{2})  \\
& = (\alpha \otimes x) \oplus (\beta \otimes x)  \\
\end{aligned}
$

$
\begin{aligned}
&\quad\ \alpha \otimes (\beta \otimes x)  \\
& = \alpha \otimes (\beta x_1, \beta x_2 + \frac{\beta(\beta - 1)}{2}x_1^{2})  \\
& = (\alpha \beta x_1, \alpha (\beta x_2 + \frac{\beta(\beta - 1)}{2}x_1^{2}) + \frac{\alpha (\alpha - 1)}{2}(\beta x_1)^{2})  \\
& = (\alpha \beta x_1, \alpha \beta x_2 + \frac{\alpha \beta^{2} - \alpha \beta}{2}x_1^{2} + \frac{\alpha^{2} \beta^{2} - \alpha \beta^{2}}{2} x_1^{2})  \\
& = (\alpha \beta x_1, \alpha \beta x_2 + \frac{\alpha^{2} \beta^{2} - \alpha \beta}{2}x_1^{2})  \\
& = (\alpha \beta x_1, \alpha \beta x_2 + \frac{\alpha \beta(\alpha \beta - 1)}{2}x_1^{2})  \\
& = (\alpha \beta) \otimes x  \\
\end{aligned}
$

综上, 对于上述定义的加法和数乘运算的集合 $R^{2}$, 构成线性空间.



## 2.

#### (1)

由 $T$ 是 $R^{3} \to R^{3}$ 的线性映射可知

$$
T(i) = T((i+j+k) - (j+k)) = T(i+j+k) - T(j+k) =  - i + j - k
$$

$$
T(j) = T((j+k) - k) = T(j+k) - T(k) = i - (2i + 3j + 5k) = -i - 3j - 5k
$$

由于 $T$ 在基 $\{ i, j, k \}$ 下的矩阵 $A$ 满足

$$
\begin{bmatrix} T(i) & T(j) & T(k) \\\end{bmatrix} = \begin{bmatrix} i & j & k \\\end{bmatrix}A
$$

因此我们有

$$
\begin{bmatrix} - i + j - k & -i - 3j - 5k & 2i + 3j + 5k \\\end{bmatrix} = \begin{bmatrix} i & j & k \\\end{bmatrix}A
$$

不妨令 $i = \begin{bmatrix} 1 & 0 & 0 \\\end{bmatrix}^{\mathrm{T}}, j = \begin{bmatrix} 0 & 1 & 0 \\\end{bmatrix}^{\mathrm{T}}, k = \begin{bmatrix} 0 & 0 & 1 \\\end{bmatrix}$, 则有

$$
A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\\end{bmatrix}A = \begin{bmatrix} -1 & -1 & 2 \\ 1 & -3 & 3 \\ -1 & -5 & 5 \\\end{bmatrix}
$$

#### (2)

由于矩阵 $A$ 的行列式不为零

$$
\det(\begin{bmatrix} -1 & -1 & 2 \\ 1 & -3 & 3 \\ -1 & -5 & 5 \\\end{bmatrix}) = -8 \neq 0
$$

因此 $A$ 是一个满秩矩阵, 则该矩阵的零空间为 $\{ \bm{0} \}$, 零空间维度是 $0$; 像空间为 $R^{3}$, 像空间维度为 3.



## 3.

由于 $uv^{\mathrm{T}}$ 与 $u^{\mathrm{T}}v$ 有相同的非零特征值, 且 $1 \times 1$ 的矩阵 $u^{\mathrm{T}}v$ 的特征值就是它自身, 所不同的是零特征值的重数不同.

因此 $uv^{\mathrm{T}}$ 的一个特征值是是 $u^{\mathrm{T}}v$, 重数为 $1$, 剩下的特征值为 $0$, 且重数为 $n-1$.

将 $uv^{\mathrm{T}}$ 的特征值带入特征多项式有

$$
\det(\lambda I - uv^{\mathrm{T}}) = \prod_{i=1}^{n} (\lambda - \lambda_i) = \lambda^{n-1}(\lambda - u^{\mathrm{T}}v)
$$

带入 $\lambda = -1$ 有

$$
\det(-I -uv^{\mathrm{T}}) = (-1)^{n-1}(-1-u^{\mathrm{T}}v) = (-1)^{n}(1 + u^{\mathrm{T}}v)
$$

因此有

$$
\det(I + uv^{\mathrm{T}}) = (-1)^{n}\det(-I -uv^{\mathrm{T}}) = 1 + u^{\mathrm{T}}v
$$



## 4.

我们先证明 $\operatorname{tr}(AB) = \operatorname{tr}(BA)$, 由迹的定义可得

$$
\operatorname{tr}(AB) = \sum_{i=1}^{m}(AB)_{ii} = \sum_{i=1}^{m}(\sum_{j=1}^{n}a_{ij}b_{ji})
$$

$$
\operatorname{tr}(BA) = \sum_{j=1}^{n}(BA)_{jj} = \sum_{j=1}^{n}(\sum_{i=1}^{m}b_{ji}a_{ij})
$$

交换求和顺序即可得 $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.

因此我们有

$$
\operatorname{tr}(ABC) = \operatorname{tr}((AB)C) = \operatorname{tr}(C(AB)) = \operatorname{tr}(CAB)
$$

$$
\operatorname{tr}(CAB) = \operatorname{tr}((CA)B) = \operatorname{tr}(B(CA)) = \operatorname{tr}(BCA)
$$

因此 $\operatorname{tr}(ABC) = \operatorname{tr}(BCA) = \operatorname{tr}(CAB)$.



## 5.

#### (1)

设 $A$ 特征值 $\lambda_i$ 对应的特征向量为 $u_i$, 则有

$$
A u_i = \lambda_i u_i
$$

并且我们有

$$
I u_i = u_i
$$

则有

$$
I u_i + cA u_i = (I + cA) u_i = u_i + c\lambda_i u_i = (1 + c\lambda_i) u_i
$$

因此有

$$
\operatorname{eig}(I + cA) = 1 + c\lambda_i
$$


#### (2)

同理我们有

$$
A u_i - c I u_i = (A - c I) u_i = \lambda_i u_i - c u_i = (\lambda_i - c) u_i
$$

因此有

$$
\operatorname{eig}(A - cI) = \lambda_i - c
$$



## 6.

#### (1)

可控性矩阵 $P_c = [B, AB, A^{2}B, \cdots, A^{n-1}B]$. 由于

$$
AB = \begin{bmatrix} 0.9 & 1 & 0 \\ 0 & -0.9 & 0 \\ 0 & 0 & 0.5 \\\end{bmatrix} \begin{bmatrix} 0 \\ 1 \\ 1 \\\end{bmatrix} = \begin{bmatrix} 1 \\ -0.9 \\ 0.5 \end{bmatrix}
$$

$$
A^{2}B = \begin{bmatrix} 0.9 & 1 & 0 \\ 0 & -0.9 & 0 \\ 0 & 0 & 0.5 \\\end{bmatrix}\begin{bmatrix} 1 \\ -0.9 \\ 0.5 \end{bmatrix} = \begin{bmatrix} 0 \\ 0.81 \\ 0.25 \end{bmatrix}
$$

则有

$$
P_c = \begin{bmatrix} 0 & 1 & 0 \\ 1 & -0.9 & 0.81 \\ 1 & 0.5 & 0.25 \\\end{bmatrix}
$$

由于

$$
\det(P_c) = \det(\begin{bmatrix} 0 & 1 & 0 \\ 1 & -0.9 & 0.81 \\ 1 & 0.5 & 0.25 \\\end{bmatrix}) = \frac{14}{25} \neq 0
$$

因此 $\operatorname{rank}(P_c) = 3$, 则 $(A, B)$ 是可控的.


#### (2)

可控性矩阵 $P_c = [B, AB, A^{2}B, \cdots, A^{n-1}B]$. 由于

$$
AB = \begin{bmatrix} 0.8 & -0.3 & 0 \\ 0.2 & 0.5 & 1 \\ 0 & 0 & -0.5 \\\end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 0 \\\end{bmatrix} = \begin{bmatrix} 0.5 \\ 0.7 \\ 0 \end{bmatrix}
$$

$$
A^{2}B = \begin{bmatrix} 0.8 & -0.3 & 0 \\ 0.2 & 0.5 & 1 \\ 0 & 0 & -0.5 \\\end{bmatrix} \begin{bmatrix} 0.5 \\ 0.7 \\ 0 \end{bmatrix} = \begin{bmatrix} 0.19 \\ 0.45 \\ 0 \end{bmatrix}
$$

则有

$$
P_c = \begin{bmatrix} 1 & 0.5 & 0.19 \\ 1 & 0.7 & 0.45 \\ 0 & 0 & 0 \\\end{bmatrix}
$$

由于

$$
\det(P_c) = \det(\begin{bmatrix} 1 & 0.5 & 0.19 \\ 1 & 0.7 & 0.45 \\ 0 & 0 & 0 \\\end{bmatrix}) = 0
$$

因此 $\operatorname{rank}(P_c) \neq 3$, 则 $(A, B)$ 是不可控的.



## 7.

矩阵 $A$ 的特征多项式为

$$
\det(\lambda I - A) = \det(\begin{bmatrix}\lambda - 3 & -2 & 2\\c & \lambda + 1 & - c\\-4 & -2 & \lambda + 3\end{bmatrix}) = (\lambda - 1) (\lambda + 1)^{2}
$$

因此矩阵 $A$ 的特征值为 $-1$ 和 $1$, 其中特征值 $-1$ 的代数重数为 $2$, 特征值 $1$ 的代数重数为 $1$.

要使得 $A$ 可对角化, 则需要特征值 $-1$ 的几何重数为 $2$.

我们带入 $\lambda = -1$ 可得

$$
\lambda I - A = \begin{bmatrix}-4 & -2 & 2\\c & 0 & - c\\-4 & -2 & 2\end{bmatrix}
$$

想要让其几何重数为 $2$, 则要让矩阵 $\lambda I - A$ 的基础解系的向量个数为 $2$ (即解空间维度为 $2$), 即矩阵 $\lambda I - A$ 的秩为 $3 - 2 = 1$, 由此可得 $c = 0$.

因此矩阵 $A$ 为

$$
A = \begin{bmatrix} 3 & 2 & -2 \\ 0 & -1 & 0 \\ 4 & 2 & -3 \\\end{bmatrix}
$$

对其进行特征值分解可得

带入 $\lambda = -1$ 可得 $\lambda I - A$ 基础解系 $\begin{bmatrix}- \frac{1}{2}\\1\\0\end{bmatrix}$ 和 $\begin{bmatrix}\frac{1}{2}\\0\\1\end{bmatrix}$, 也就是 $-1$ 对应的特征向量.

带入 $\lambda = 1$ 可得 $\lambda I - A$ 基础解系 $\begin{bmatrix}1\\0\\1\end{bmatrix}$, 也就是 $1$ 对应的特征向量.

因此借助特征值分解可得

$$
B = P^{-1}AP = \begin{bmatrix} 1 & -\frac{1}{2} & \frac{1}{2} \\ 0 & 1 & 0 \\ 1 & 0 & 1 \\\end{bmatrix}^{-1}\begin{bmatrix} 3 & 2 & -2 \\ 0 & -1 & 0 \\ 4 & 2 & -3 \\\end{bmatrix}\begin{bmatrix} 1 & -\frac{1}{2} & \frac{1}{2} \\ 0 & 1 & 0 \\ 1 & 0 & 1 \\\end{bmatrix} = \begin{bmatrix}1 & 0 & 0\\0 & -1 & 0\\0 & 0 & -1\end{bmatrix}
$$

也即 $P = \begin{bmatrix} 1 & -\frac{1}{2} & \frac{1}{2} \\ 0 & 1 & 0 \\ 1 & 0 & 1 \\\end{bmatrix}$ 与 $B = \begin{bmatrix}1 & 0 & 0\\0 & -1 & 0\\0 & 0 & -1\end{bmatrix}$.



## 8.

该二次曲面方程改写成二次型形式为

$$
\begin{bmatrix} x \\ y \\ z \\\end{bmatrix}^{\mathrm{T}}\begin{bmatrix} 1 & b & 1 \\ b & a & 1 \\ 1 & 1 & 1 \\\end{bmatrix}\begin{bmatrix} x \\ y \\ z \\\end{bmatrix} = 4
$$

而椭圆柱面方程的二次型形式为

$$
\begin{bmatrix} \xi \\ \eta \\ \psi \\\end{bmatrix}^{\mathrm{T}}\begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 4 \\\end{bmatrix}\begin{bmatrix} \xi \\ \eta \\ \psi \\\end{bmatrix} = 4
$$

由于正交变换 $P$ 满足

$$
\begin{bmatrix} x \\ y \\ z \\\end{bmatrix} = P\begin{bmatrix} \xi \\ \eta \\ \psi \\\end{bmatrix}
$$

因此带入有

$$
\begin{bmatrix} \xi \\ \eta \\ \psi \\\end{bmatrix}^{\mathrm{T}}\left(P^{\mathrm{T}}\begin{bmatrix} 1 & b & 1 \\ b & a & 1 \\ 1 & 1 & 1 \\\end{bmatrix}P\right)\begin{bmatrix} \xi \\ \eta \\ \psi \\\end{bmatrix} = 4
$$

即有

$$
P^{\mathrm{T}}\begin{bmatrix} 1 & b & 1 \\ b & a & 1 \\ 1 & 1 & 1 \\\end{bmatrix}P = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 4 \\\end{bmatrix}
$$

令 $A = \begin{bmatrix} 1 & b & 1 \\ b & a & 1 \\ 1 & 1 & 1 \\\end{bmatrix}$ 与 $\Sigma = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 4 \\\end{bmatrix}$, 则由上式与对称矩阵的性质我们可知 $\Sigma$ 是 $A$ 进行特征值分解后得到的对角阵, 而 $0, 1, 4$ 分别为 $A$ 的三个不同的特征值.

对 $A$ 进行特征值分解有特征多项式

$$
\det(\lambda I - A) = - a \lambda^{2} + 2 a \lambda - b^{2} \lambda + b^{2} - 2 b + \lambda^{3} - 2 \lambda^{2} - \lambda + 1 = 0
$$

将 $0, 1, 4$ 分别带入 $\lambda$ 可得

$$
\begin{cases}
b^{2} - 2 b + 1 = 0  \\
a - 2 b - 1 = 0  \\
-8 a - 3 b^{2} - 2 b + 29 = 0  \\
\end{cases}
\Rightarrow
\begin{cases}
a = 3  \\
b = 1  \\
\end{cases}
$$

即有 $a = 3$ 与 $b = 1$ 以及原二次曲面方程

$$
x^{2} + 3y^{2} + z^{2} + 2xy + 2xz + 2yz = 4
$$


带入 $\lambda_1 = 0$ 解 $(\lambda_1 I - A)u_1 = 0$ 可得特征向量 $u_1 = \begin{bmatrix} \frac{\sqrt{2}}{2} & 0 & -\frac{\sqrt{2}}{2} \\\end{bmatrix}^{\mathrm{T}}$.


带入 $\lambda_2 = 1$ 解 $(\lambda_2 I - A)u_2 = 0$ 可得特征向量 $u_2 = \begin{bmatrix} \frac{\sqrt{3}}{3} & -\frac{\sqrt{3}}{3} & \frac{\sqrt{3}}{3} \\\end{bmatrix}^{\mathrm{T}}$.

带入 $\lambda_3 = 4$ 解 $(\lambda_3 I - A)u_3 = 0$ 可得特征向量 $u_3 = \begin{bmatrix} \frac{\sqrt{6}}{6} & \frac{2\sqrt{6}}{6} & \frac{\sqrt{6}}{6} \\\end{bmatrix}^{\mathrm{T}}$.

因此可得正交矩阵 $P$ 为

$$
P = \begin{bmatrix} \frac{\sqrt{2}}{2} & \frac{\sqrt{3}}{3} & \frac{\sqrt{6}}{6} \\ 0 & -\frac{\sqrt{3}}{3} & \frac{\sqrt{6}}{3} \\ -\frac{\sqrt{2}}{2} & \frac{\sqrt{3}}{3} & \frac{\sqrt{6}}{6} \\\end{bmatrix}
$$



## 9.

#### (1)

要证 $HH^{\mathrm{T}} = I_n$, 即证 $H$ 是一个正交矩阵.

首先证明 $H$ 的相同行向量的内积为 $1$:

$h^{\mathrm{T}}h = n^{-\frac{1}{2}} \cdot n^{-\frac{1}{2}} \cdot 1_{n}^{\mathrm{T}}1_{n} = n^{-1}\cdot n = 1$

$\displaystyle K_{i}K_{i}^{\mathrm{T}} = \frac{1}{\sqrt{\lambda_i}}\cdot \frac{1}{\sqrt{\lambda_i}}(1_{i}^{\mathrm{T}}1_{i} + (-i)^{2}) = 1$

其次证明 $H$ 的不同行向量的内积为 $0$:

$\displaystyle h^{\mathrm{T}}K_{i}^{\mathrm{T}} = n^{-\frac{1}{2}}\cdot \frac{1}{\sqrt{\lambda_i}} \cdot 1_{i}^{\mathrm{T}}1_{i} + n^{-\frac{1}{2}}\cdot \frac{1}{\sqrt{\lambda_i}}\cdot (-i) = 0$

不妨令 $j > i$, 则有

$\displaystyle K_i^{\mathrm{T}}K_j = \frac{1}{\sqrt{\lambda_i}} \cdot \frac{1}{\sqrt{\lambda_i}} (1_{i}^{\mathrm{T}}1_{i} + (-i) \cdot 1 + 0) = 0$

因此我们有 $HH^{\mathrm{T}} = I_n$.


#### (2)

首先证明

$$
n \bar{x}_{n}^{2} = x^{\mathrm{T}}hh^{\mathrm{T}}x = (n^{-\frac{1}{2}}1_{n}^{\mathrm{T}}x)^{\mathrm{T}}n^{-\frac{1}{2}}1_{n}^{\mathrm{T}}x = \frac{1}{n}(\sum_{i=1}^{n}x_{i})^{2} = n (\frac{1}{n}\sum_{i=1}^{n}x_{i})^{2}
$$

其次证明 $S_n = x^{\mathrm{T}}K^{\mathrm{T}}Kx$.

由于 $H$ 是正交矩阵, 因此也有

$$
H^{\mathrm{T}}H = \begin{bmatrix} h & K^{\mathrm{T}} \\\end{bmatrix}\begin{bmatrix} h^{\mathrm{T}} \\ K \\\end{bmatrix} = h h^{\mathrm{T}}+ K^{\mathrm{T}}K = I_n
$$

则有

$$
K^{\mathrm{T}}K = I_n - hh^{\mathrm{T}}
$$

因此我们有

$$
\begin{aligned}
x^{\mathrm{T}}K^{\mathrm{T}}K x & = x^{\mathrm{T}}(I_n - hh^{\mathrm{T}})x  \\
& = x^{\mathrm{T}}I_nx - x^{\mathrm{T}}hh^{\mathrm{T}}x  \\
& = (\sum_{i=1}^{n}x_i^{2}) - n \bar{x}_n^{2}  \\
& = \sum_{i=1}^{n}(x_i - \bar{x}_n)^{2}  \\
& = S_n
\end{aligned}
$$


#### (3)

根据 $K_{n}$ 和 $K_{n-1}$ 的关系

$$
K_n = \begin{bmatrix} K_{n-1} & 0 \\ \frac{1}{\sqrt{\lambda_{n-1}}}1_{n-1} & \frac{-(n-1)}{\sqrt{\lambda_{n-1}}} \\\end{bmatrix}
$$

我们令 $\displaystyle u = \frac{1}{\sqrt{\lambda_{n-1}}}\begin{bmatrix} 1_{n-1} & -(n-1) \\\end{bmatrix}^{\mathrm{T}}$ 且 $K = K_n$, 则可知

$$
\begin{aligned}
S_{n-1} & = x^{\mathrm{T}}K^{\mathrm{T}}Kx - x^{\mathrm{T}}uu^{\mathrm{T}}x  \\
& = S_n - (\sum_{i=1}^{n-1}\frac{1}{\sqrt{\lambda_{n-1}}}x_{i} - \frac{n-1}{\sqrt{\lambda_{n-1}}}x_n)^{2}  \\
& = S_n - (\frac{n-1}{n})(\frac{1}{n-1}\sum_{i=1}^{n-1}x_{i} - x_n)^{2}  \\
& = S_n - (1-\frac{1}{n})(\bar{x}_{n-1} - x_n)^{2}  \\
\end{aligned}
$$

因此我们有

$$
S_n = S_{n-1} + (1-\frac{1}{n})(\bar{x}_{n-1} - x_n)^{2}
$$


## 10.

#### (1)

由于 $A$ 为实反对称矩阵, 则有 $A^{\mathrm{T}} = -A$.

因此有对于任意 $x$ 有

$$
x^{\mathrm{T}}Ax = (x^{\mathrm{T}}Ax)^{\mathrm{T}} = x^{\mathrm{T}}A^{\mathrm{T}}x = -x^{\mathrm{T}}Ax
$$

因此有

$$
x^{\mathrm{T}}Ax = 0
$$

要证明 $A + I$ 非奇异, 即证明 $(A + I)x = 0$ 只有零解, 由于 $(A + I)x = 0$ 我们有

$$
x^{\mathrm{T}}(A + I)x = 0
$$

且我们有

$$
x^{\mathrm{T}}(A + I)x = x^{\mathrm{T}}Ax + x^{\mathrm{T}}Ix = x^{\mathrm{T}}x
$$

因此可得 $x^{\mathrm{T}}x = 0$, 即有 $x = 0$.

因此可以说明 $A + I$ 非奇异.


#### (2)

要证 $T = (I - A)(I + A)^{-1}$ 为正交矩阵, 即证 $T^{\mathrm{T}}T = I$ 与 $TT^{\mathrm{T}} = I$.

首先我们证明 $(I + A)(I - A) = (I - A)(I + A)$

$$
(I + A)(I - A) = I - AA = (I - A)(I + A)
$$

然后我们有

$$
\begin{aligned}
T^{\mathrm{T}}T & = ((I - A)(I + A)^{-1})^{\mathrm{T}}(I - A)(I + A)^{-1}  \\
& = ((I + A)^{\mathrm{T}})^{-1}(I - A)^{\mathrm{T}}(I - A)(I + A)^{-1}  \\
& = (I - A)^{-1}(I + A)(I - A)(I + A)^{-1}  \\
& = (I - A)^{-1}(I - A)(I + A)(I + A)^{-1}  \\
& = I  \\
\end{aligned}
$$

由于 $T$ 是方阵, 且 $T^{\mathrm{T}}T$ 说明 $T$ 的列向量两两正交, 则有 $T$ 满秩, 一定有 $T$ 可逆, 设逆矩阵为 $B$, 且满足 $BT = TB = I$, 则有 $B = T^{\mathrm{T}}$, 带入可得

$$
TT^{\mathrm{T}} = I
$$

因此 $T$ 为正交矩阵.


#### (3)

对 $A = (I - S)(I + S)^{-1}$ 转换以求解 $S$ 可得

$$
A(I+S) = I-S \Rightarrow A+AS = I-S \Rightarrow (A + I)S= I - A
$$

因此有

$$
S= (I + A)^{-1}(I - A)
$$

下面证明 $S$ 是实反对称矩阵

$$
\begin{aligned}
S^{\mathrm{T}} & = (I - A^{\mathrm{T}})(I + A^{\mathrm{T}})^{-1}  \\
& = (I + A^{\mathrm{T}})^{-1} - A^{\mathrm{T}}(I + A^{\mathrm{T}})^{-1}  \\
& = (I + A^{\mathrm{T}})^{-1}A^{-1}A - A^{-1}(I + A^{\mathrm{T}})^{-1}  \\
& = (A(I + A^{\mathrm{T}}))^{-1}A - ((I + A^{\mathrm{T}})A)^{-1}  \\
& = (A + I)^{-1}A - (A + I)^{-1}  \\
& = -(A + I)^{-1}(I - A)  \\
& = -S  \\
\end{aligned}
$$



## 11.

由题意可知

$$
\begin{cases} Ax = ax \\ A^{\mathrm{T}}y = by \\ a - b \neq 0 \end{cases}
$$

因此我们有

$$
x^{\mathrm{T}}A^{\mathrm{T}}y = (Ax)^{\mathrm{T}}y = ax^{\mathrm{T}}y
$$

以及

$$
x^{\mathrm{T}}A^{\mathrm{T}}y = x^{\mathrm{T}}(A^{\mathrm{T}}y) = bx^{\mathrm{T}}y
$$

两式相减则有

$$
ax^{\mathrm{T}}y - bx^{\mathrm{T}}y = (a - b)x^{\mathrm{T}}y = 0
$$

由于 $a - b \neq 0$, 则有 $x$ 和 $y$ 的内积

$$
x^{\mathrm{T}}y = 0
$$

因此 $x$ 和 $y$ 正交.
