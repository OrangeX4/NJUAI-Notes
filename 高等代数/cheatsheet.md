# 线性代数

## 求和运算法则

* $\displaystyle\sum_{i=1}^nx_i=x_1+x_2+\cdots +x_n$
* $\displaystyle\sum_{i=1}^nkx_i=k\sum_{i=1}^nx_i$
* $\displaystyle\sum_{i=1}^n(x_i+y_i)=\sum_{i=1}^nx_i+\sum_{i=1}^ny_i$
* $\displaystyle\sum_{i=1}^nx_i\sum_{j=1}^my_j=\sum_{j=1}^my_j\sum_{i=1}^nx_i=\sum_{i=1}^n\sum_{j=1}^mx_iy_j=\sum_{j=1}^m\sum_{i=1}^nx_iy_j$
* $\displaystyle\sum_{i=1}^nx_i\sum_{j=1}^my_jz_{ij}=\sum_{j=1}^my_j\sum_{i=1}^nx_iz_{ij}=\sum_{i=1}^n\sum_{j=1}^mx_iy_jz_{ij}=\sum_{j=1}^m\sum_{i=1}^nx_iy_jz_{ij}$

## 值域和零空间

$A \in \mathbb{R}^{m \times n}$ 的列向量的线性组合的所有向量的集合 $\mathcal{R}(A)$ 称为 $A$ 的 **值域**.

$\mathcal{R}(A) = \{ Ax | x \in \mathbb{R}^{n} \}$

$\mathcal{R}(A)$ 是 $\mathbb{R}^{m}$ 的子空间, 它的维数是 $A$ 的 **秩**.

被 $A$ 映射成零的所有向量 $x$ 的集合 $\mathcal{N}(A)$ 称为 $A$ 的 **零空间** 或 **核**.

$\mathcal{N}(A) = \{ x | Ax = 0 \}$

它们之间的关系是

$\mathcal{N}(A) = \mathcal{R}(A^{\top})^{\bot}$

## 秩的性质

- 初等行变换不改变矩阵的秩
- 对于 $A \in \mathbb{R}^{m\times n}, B \in \mathbb{R}^{n\times r}$ 有
  - $\operatorname{rank}(A)+\operatorname{rank}(B)-n\le \operatorname{rank}(AB)\le \min \{ \operatorname{rank}(A), \operatorname{rank}(B) \}$
  - $\operatorname{rank}(A + B) \le \operatorname{rank}(A) + \operatorname{rank}(B)$
- 对于任意矩阵 $A$ 有
  - $\operatorname{rank}(A) = \operatorname{rank}(A^{\top}) = \operatorname{rank}(A A^{\top}) = \operatorname{rank}(A^{\top}A)$

## 合同与相似

设 $A,B\in P^{n\times n}$, 若存在可逆矩阵 $C\in P^{n\times n}$, 使得 $B=C^{\top} AC$, 则称 $A$ 与 $B$ **合同**.

实对称矩阵 $A$ 正定 $\Leftrightarrow$ $A$ 与单位矩阵 $E$ 合同, 即存在可逆矩阵 $C$, 使 $A=C^TC$

设 $A,B\in P^{n\times n}$, 若存在可逆矩阵 $C\in P^{n\times n}$, 使得 $B=C^{-1} AC$, 则称 $A$ 与 $B$ **相似**.

这里的 $C$ 可以看作一个基 $B$ 到 $A$ 的过渡矩阵 (即 $\alpha_{A} = C\alpha_{B}$).

## 特征值分解

若方阵 $A$ 可以使用相似矩阵分解为 $A = Q\Lambda Q^{-1}$, 其中 $\Lambda$ 是对角矩阵, 且对角线上是它的特征值, $Q$ 是它的特征向量矩阵, 则称 $A$ 可以特征值分解.

## 实对称矩阵

- 所有特征值都为实数;
- 不同特征值对应的特征向量互相正交;
- $k$ 重特征值对应的线性无关的特征向量恰有 $k$ 个;
- $n$ 阶实对称矩阵 $A$ 必可相似对角化，且对角阵上的元素即为特征值;
- 任意矩阵 $A$, 都有 $A^{\top}A$ 是一个实对称矩阵.

## 实对称特征值分解

若实对称矩阵 $A$ 可以使用相似矩阵分解为 $A = Q\Lambda Q^{\top}$, 其中 $\Lambda$ 是对角矩阵, 且对角线上是它的特征值, $Q$ 是它的特征向量矩阵.

我们还可以知道 $Q$ 是正交矩阵, 即满足 $Q^{\top}Q = I$.

其中 $\Lambda = \operatorname{diag}(\lambda_1,\cdots ,\lambda_{n}), \lambda_1 \ge \cdots \ge \lambda_{n}$, 且 $\lambda_{i}$ 是特征多项式 $\det (\lambda I-A)$ 的根.

从几何意义上来说, 可以看成是先用 $Q^{\top}$ 进行旋转, 然后用 $\Lambda$ 进行各个基向量方向的拉伸, 最后再使用 $Q$ 旋转恢复原样.

## 奇异值分解

对于 $A \in \mathbb{R}^{m \times n}, \operatorname{rank}A=r$, 则 $A$ 可以因式分解为 $A = U\Sigma V^{\top}$

其中 $U \in \mathbb{R}^{m \times r}$ 满足 $U^{\top}U = I$, $V \in \mathbb{R}^{n \times r}$ 满足 $V^{\top}V = I$.

而 $\Sigma = \operatorname{diag}(\sigma_1,\cdots ,\sigma_{r})$ 满足 $\sigma_1 \ge \cdots \ge \sigma_{r}$

则称为 $A$ 的奇异值分解.

$U$ 的列向量称为左奇异向量, $V$ 的列向量称为右奇异向量, $\sigma_{i}$ 称为奇异值.

$A$ 的奇异值分解和实对称矩阵 $A^{\top}A$ 的特征值分解密切相关

$A^{\top}A = V\Sigma^{2}V^{\top} = \begin{bmatrix} V & \tilde{V} \end{bmatrix} \begin{bmatrix} \Sigma^{2} & 0 \\ 0 & 0 \\\end{bmatrix} \begin{bmatrix} V & \tilde{V} \end{bmatrix}^{\top}$

同理可以用 $AA^{\top}$ 算出左奇异向量 $U$

并且我们还可以知道 $A^{\top}A$ 或 $AA^{\top}$ 的 特征值就是奇异值 $\sigma_{i}$ 的平方.

对于满秩实对称矩阵 $A$, 我们可以知道 $n = m = r$, 并且 $A = Q\Lambda Q^{\top}$, 则有

$A^{\top}A = Q\Lambda Q^{\top}Q\Lambda Q^{\top} = Q\Lambda^{2}Q$

所以我们可知此时 $Q = \Sigma$ 与 $U = V = Q$, 即满秩实对称矩阵的奇异值分解就是特征值分解.

## 伪逆

令 $A = U\Sigma V^{\top}$ 为 $A$ 的奇异值分解, 则我们有 $A^{\dagger} = V\Sigma^{-1}U^{\top}$, 称为 $A$ 的 **伪逆**. 

## 协方差矩阵

假定我们现在有 $n$ 个样本, 其中每个样本 $x$ 都是一个 $d$ 维的随机变量, 每个分量分别是 $x_{k}, k=1,2,\cdots,d$.

那么协方差计算公式为

$\displaystyle \sigma(x_{m}, x_{k}) = \frac{1}{n-1}\sum_{i=1}^{n}(x_{mi}-\bar{x}_{m})(x_{ki}-\bar{x}_{k})$

相同随机变量的协方差即为方差.

所以有协方差矩阵为

$\Sigma = \begin{bmatrix} \sigma(x_1,x_1) & \cdots  & \sigma(x_1,x_{d}) \\ \vdots & \ddots & \vdots \\ \sigma(x_{d},x_1) & \cdots  & \sigma(x_{d},x_{d}) \\\end{bmatrix} \in \mathbb{R}^{d \times d}$

经过中心化之后的 $X$, 可以通过一种方式很快得算出协方差

$\displaystyle \Sigma = \frac{1}{n-1}X^{\top}X$

因此协方差矩阵是一个标准的实对称矩阵, 可以使用特征值分解等方式进行分析.

## 多元正态分布

假设向量 $x$ 服从均值向量为 $\mu$, 协方差矩阵为 $\Sigma$ 的多元正态随机分布, 则有

$\displaystyle p(x) = |2\pi\Sigma|^{-\frac{1}{2}}\exp (-\frac{1}{2}(x-\mu)^{\top}\Sigma^{-1}(x-\mu))$

我们知道协方差矩阵可以分解为 $\Sigma = U\Lambda U^{\top} = (U\Lambda^{\frac{1}{2}})(U\Lambda^{\frac{1}{2}})^{\top}$

所以可以认为, 特征向量矩阵 $U$ 控制概率密度 **旋转** (rotation), 特征值矩阵 $\Lambda$ 控制 **缩放** (scale), 均值向量 $\mu$ 控制 **中心位置**.

实际上, 由于 $\Sigma = U\Lambda U^{\top}$, 我们可以知道 $\Sigma^{-1} = U\Lambda^{-1}U^{\top} = (U\Lambda^{-\frac{1}{2}})(U\Lambda^{-\frac{1}{2}})^{\top}$

即 $\Sigma^{-\frac{1}{2}} = U\Lambda^{-\frac{1}{2}}$, 则有 $U\Lambda^{-\frac{1}{2}}$

所以实际上 $\Sigma^{-\frac{1}{2}}(x-\mu)$ 就是转为了标准多元正态分布的形式.
