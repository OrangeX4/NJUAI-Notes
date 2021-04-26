# 向量与行列式的几何意义

### 向量几何意义

令向量 $\alpha=\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}$

**向量 $\alpha$ 是从原点 $(0,0,\cdots ,0)$ 指向另一点 $(a_1,a_2,\cdots,a_n)$ 的有向线段**

### 行列式几何意义

对于二阶行列式 $\begin{vmatrix}a_{11}&a_{21}\\a_{12}&a_{22}\end{vmatrix}=a_{11}a_{22}-a_{12}a_{21}$

向量 $\alpha_1=\begin{pmatrix}a_{11}\\a_{12}\end{pmatrix}$ 和 $\alpha_2=\begin{pmatrix}a_{21}\\a_{22}\end{pmatrix}$ 所形成的一个平行四边形面积

$S=2\times\frac{1}{2}|\alpha_1||\alpha_2|\sin\langle \alpha_1,\alpha_2\rangle=|\alpha_1||\alpha_2|\sqrt{1-(\frac{\alpha_1\cdot\alpha_2}{|\alpha_1||\alpha_2|})^2}$
$\quad=\sqrt{(|\alpha_1||\alpha_2|)^2-(\alpha_1\cdot\alpha_2)^2}$
$\quad=\sqrt{(a_{11}^2+a_{12}^2)(a_{21}^2+a_{22}^2)-(a_{11}a_{21}+a_{12}a_{22})^2}$
$\quad=\sqrt{a_{12}^2a_{21}^2+a_{11}^2a_{22}^2-2a_{11}a_{21}a_{12}a_{22}}$
$\quad=|a_{11}a_{22}-a_{12}a_{21}|$

我们可知,

* **二阶行列式是两个二维向量所围成的平行四边形的面积**

依次类推, 我们同样有

* **三阶行列式是三个三维向量所围成的平行六面体的体积**
* **$n$ 阶行列式是 $n$ 个 $n$ 维向量所围成的平行超多面体的超体积**

### 线性相关性

我们可以在多维空间中形象地想象,

行列式等于零 $\Leftrightarrow$ 超多面体体积为 $0\Leftrightarrow$ 超多面体坍缩 $\Leftrightarrow$ 向量线性相关

**对于二阶行列式, $\alpha_1$ 与 $\alpha_2$ 线性相关, 说明$\alpha_1\parallel\alpha_2$, 即行列式|A|=0**

**对于三阶行列式,**

**$\alpha_1,\alpha_2,\alpha_3$ 线性相关, 说明 $\alpha_3\parallel \alpha_1$ 与 $\alpha_2$ 形成的平面, 即行列式 $|A|=0$**

# 齐次线性方程组方阵与线性相关性

对于齐次线性方程组(*)

$
\begin{cases}
a_{11}x_1+a_{12}x_2+\cdots +a_{1n}x_n=0 \\
a_{21}x_1+a_{22}x_2+\cdots +a_{2n}x_n=0 \\
\cdots \\
a_{n1}x_1+a_{n2}x_2+\cdots +a_{nn}x_n=0 \\
\end{cases}
$

方程组(*)必定有零解, 即 $\vec{x}=\begin{pmatrix}0\\0\\\vdots\\0\end{pmatrix}$, 那么有没有非零解呢?

令 $\alpha_i=\begin{pmatrix}a_{i1}\\a_{i2}\\\vdots \\a_{in}\end{pmatrix}, 则|A|=|A^T|=\begin{vmatrix}a_{11}&a_{12}&\cdots &a_{1n}\\a_{21}&a_{22}&\cdots &a_{2n}\\\vdots &\vdots & &\vdots \\a_{n1}&a_{n2}&\cdots &a_{nn}\end{vmatrix}$

由Cramer法则可知,

**方程组(*)仅有零解 $\Leftrightarrow |A|\neq 0\Leftrightarrow \{\alpha_1,\alpha_2,\cdots,\alpha_n\}$ 线性无关**
**方程组(*)有非零解 $\Leftrightarrow |A|= 0\Leftrightarrow \{\alpha_1,\alpha_2,\cdots,\alpha_n\}$ 线性相关**

要注意到:

* 此时向量维度与向量个数相等
* 方程组参数或者说行列式是否转置与方程组是否仅有零解无关$

### Cramer法则

$
\begin{cases}
a_{11}x_1+a_{21}x_2+\cdots +a_{n1}x_n=b_1 \\
a_{12}x_1+a_{22}x_2+\cdots +a_{n2}x_n=b_2 \\
\cdots \\
a_{1n}x_1+a_{2n}x_2+\cdots +a_{nn}x_n=b_n \\
\end{cases}
$

令 $\alpha_i=\begin{pmatrix}a_{i1}\\a_{i2}\\\vdots \\a_{in}\end{pmatrix},\beta=\begin{pmatrix}b_{1}\\b_{2}\\\vdots \\b_{n}\end{pmatrix}, D=|\alpha_1\quad\alpha_2\quad\cdots \quad\alpha_n|$

将 $D$ 中的 $\alpha_i$ 替换成 $\beta$, 就得到 $D_i$

Cramer法则: $x_i=\displaystyle\frac{D_i}{D}$

**证明:**

将 $x_i=\displaystyle\frac{D_i}{D}$ 带入方程组里, 并将 $D_i$ 按 $i$ 列展开, 整理, 使用不同行展开为 $0$ 便可证.

### 线性相关性

线性相关 $\Leftrightarrow$ 存在不全为 $0$ 的 $k_i$ 使得 $k_1\alpha_1+k_2\alpha_2+\cdots +k_n\alpha_n=0$

线性无关 $\Leftrightarrow k_1\alpha_1+k_2\alpha_2+\cdots +k_n\alpha_n=0$ 只有零解.


# 非方阵形式的齐次方程组

$
\begin{cases}
a_{11}x_1+a_{21}x_2+\cdots +a_{n1}x_n=0 \\
a_{12}x_1+a_{22}x_2+\cdots +a_{n2}x_n=0 \\
\cdots \\
a_{1s}x_1+a_{2s}x_2+\cdots +a_{ns}x_n=0 \\
\end{cases}
$

齐次方程组(*)必定有零解, 即 $\vec{x}=\begin{pmatrix}0\\0\\\vdots\\0\end{pmatrix}_n$

令 $\alpha_i=\begin{pmatrix}a_{i1}\\a_{i2}\\\vdots \\a_{is}\end{pmatrix}, 则A=\begin{bmatrix}a_{11}&a_{21}&\cdots &a_{n1}\\a_{12}&a_{22}&\cdots &a_{n2}\\\vdots &\vdots & &\vdots \\a_{1s}&a_{2s}&\cdots &a_{ns}\end{bmatrix}_{n\times s}$

**当 $s<n$ 时, 即向量维度小于向量个数, 矩阵的宽度小于长度**

由解方程组的理论可知, 此时一定会有自由变量 $x_{s+1},\cdots ,x_n$

或者说给向量增加n-s个维度, 就形成了一个 $n\times n$ 的行列式 $|A|$,
每个维度上的数为 $0$, 则易知行列式 $|A|=0$

理论依据: 添加一些系数全为零的方程相当于加入 $0=0$, 是恒成立的

**方程组(*)一定有非零解, 说明向量一定线性相关**

**当 $s>n$ 时, 即向量维度大于向量个数, 矩阵的宽度大于长度**

有三种选择,

**一是减少维度, 最为常用**
运用解方程理论必定可以让所有向量 $s-n$ 个维度变为 $0$
进而降维到 $n\times n$, 采用方阵相关理论即可解

**二是增加线性无关向量,**
增加 $s-n$ 个与前面向量线性无关的向量, 解 $x_i$ 的个数不会变
进而升维到 $s\times s$, 采用方阵相关理论即可解

**这两种方式均不会改变 $|A|$ 的零性, 也就不会影响前 $n$ 个向量的线性相关性**

**三是使用子式**
一矩阵的秩是 $r⇔$ 矩阵中有一个 $r$ 级子式不为零, 同时所有的 $r+1$ 级子式 (如果有的话) 全为零.



# 求和运算法则

* **$\displaystyle\sum_{i=1}^nx_i=x_1+x_2+\cdots +x_n$**
* **$\displaystyle\sum_{i=1}^nkx_i=k\sum_{i=1}^nx_i$**
* **$\displaystyle\sum_{i=1}^n(x_i+y_i)=\sum_{i=1}^nx_i+\sum_{i=1}^ny_i$**
* **$\displaystyle\sum_{i=1}^nx_i\sum_{j=1}^my_j=\sum_{j=1}^my_j\sum_{i=1}^nx_i=\sum_{i=1}^n\sum_{j=1}^mx_iy_j=\sum_{j=1}^m\sum_{i=1}^nx_iy_j$**
* **$\displaystyle\sum_{i=1}^nx_i\sum_{j=1}^my_jz_{ij}=\sum_{j=1}^my_j\sum_{i=1}^nx_iz_{ij}=\sum_{i=1}^n\sum_{j=1}^mx_iy_jz_{ij}=\sum_{j=1}^m\sum_{i=1}^nx_iy_jz_{ij}$**

常见的向量求和运算:

定义符号 $\displaystyle\bigcap_{i=1}^nf_i(\vec{x})=b_i$ 为方程组 $\begin{cases}
f_1(\vec{x})=b_1 \\
f_2(\vec{x})=b_2 \\
\cdots \\
f_n(\vec{x})=b_n \\
\end{cases}, 设\alpha_i=\begin{pmatrix}a_{i1}\\a_{i2}\\\vdots \\a_{im}\end{pmatrix}
$

**线性相关性: $\displaystyle\bigcap_{p=1}^m\sum_{i=1}^na_{ip}k_i=0\rightarrow$ 是否 $\forall k_i=0$**

**若 $n=m$, 通过转置则有**

**$\displaystyle\bigcap_{p=1}^n\sum_{i=1}^na_{ip}k_i=0\rightarrow$ 是否 $\forall k_i=0$**
**$\Leftrightarrow$**
**$\displaystyle\bigcap_{p=1}^n\sum_{i=1}^na_{pi}k_i=0\rightarrow$ 是否 $\forall k_i=0$**


# 分块矩阵和初等矩阵

### 广义三角矩阵行列式

$\begin{vmatrix}A_1&\cdots &\cdots &\cdots \\O&A_2&\cdots &\cdots \\\vdots &\vdots &\ddots &\vdots \\O&O&\cdots &A_n\end{vmatrix}=|A_1||A_2|\cdots |A_n|$

### 分块对角矩阵逆矩阵

$\begin{bmatrix}A_1&O &\cdots  &O \\O&A_2&\cdots &O \\\vdots &\vdots &\ddots &\vdots \\O&O&\cdots &A_n\end{bmatrix}^{-1}=\begin{bmatrix}A_1^{-1}&O &\cdots  &O \\O&A_2^{-1}&\cdots &O \\\vdots &\vdots &\ddots &\vdots \\O&O&\cdots &A_n^{-1}\end{bmatrix}$

### 初等矩阵

对一个矩阵 $A$ 实施了初等行变换 $P$ 和初等列变换 $Q$ 即为矩阵乘法 $PAQ$

其中 $P$ 和 $Q$ 均为对单位矩阵 $E$ 进行了初等行列变换的结果

#### 初等行变换矩阵

* 互换 $E$ 的 $i,j$ 两行, 记作 $P(i,j)$
  * $|P(i,j)|=-1$
  * $P(i,j)^{-1}=P(i,j)$
* $E$ 的第 $i$ 行乘以不等于零的数 $k$, 记作 $P(i(k))$
  * $|P(i(k))|=k$
  * $P(i(k))^{-1}=P(i(\displaystyle\frac{1}{k}))$
* $E$ 的第 $j$ 行的 $k$ 倍加到第 $i$ 行上, 记作 $P(i,j(k))$
  * $|P(i,j(k))|=1$
  * $P(i,j(k))^{-1}=P(i,j(-k))$

$(A\quad E)\xrightarrow{\text{初等行变换}}(E\quad A^{-1})$

$(A\quad B)\xrightarrow{\text{初等行变换}}(E\quad A^{-1}B)$

#### 初等行变换矩阵

* $P(i,j)=Q(i,j)$
* $P(i(k))=Q(i(k))$
* **$P(i,j(k))=Q(j,i(k))$**

$\begin{pmatrix}A\\E\end{pmatrix}\xrightarrow{初等列变换}\begin{pmatrix}E\\A^{-1}\end{pmatrix}$

$\begin{pmatrix}A\\B\end{pmatrix}\xrightarrow{初等列变换}\begin{pmatrix}E\\BA^{-1}\end{pmatrix}$

### 分块矩阵运算

若A可逆

$\begin{bmatrix}E_m&O\\-CA^{-1}&E_n\end{bmatrix}\begin{bmatrix}A&B\\C&D\end{bmatrix}=\begin{bmatrix}A&B\\O&D-CA^{-1}B\end{bmatrix}$
