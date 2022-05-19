# PS4

## 一、

**(1)**

$
\begin{aligned}
\frac{\partial \ell(y, \hat{y}_1)}{\partial \beta_1}
& = \frac{\partial \ell(y, \hat{y}_1)}{\partial \hat{y}_1}\frac{\partial \hat{y}_1}{\partial \beta_1}  \\
& = (\frac{1-y}{1-\hat{y}_1} - \frac{y}{\hat{y}_1}) \cdot f'(\beta_1 - \theta_1)  \\
& = \hat{y}_1(1-\hat{y}_1)(\frac{1-y}{1-\hat{y}_1} - \frac{y}{\hat{y}_1})  \\
& = \hat{y}_1 - y  \\
\end{aligned}
$

**(2)**

令 $\displaystyle f(x) = \frac{e^{x}}{e^{x} + \theta}$, 对其求导得 $\displaystyle f'(x) = \frac{e^{x}}{\theta + e^{x}}(1 - \frac{e^{x}}{\theta + e^{x}}) = f(x)(1-f(x))$

令 $\displaystyle f(x) = \frac{\varphi}{e^{x} + \theta}$, 对其求导得 $\displaystyle f'(x) = - \frac{\varphi}{\theta + e^{x}}(1 - \frac{\theta}{\theta + e^{x}}) = -f(x)(1 - \frac{\theta}{\varphi}f(x))$

$
\begin{aligned}
\frac{\partial \ell(\bm{y}, \hat{\bm{y}})}{\partial \beta_j}
& = \frac{\partial \ell(\bm{y}, \hat{\bm{y}})}{\partial \hat{y}_j}\frac{\partial \hat{y}_j}{\partial \beta_j} + \sum_{k \neq j}\frac{\partial \ell(\bm{y}, \hat{\bm{y}})}{\partial \hat{y}_k}\frac{\partial \hat{y}_k}{\partial \beta_j} \\
& = -\frac{y_j}{\hat{y}_j} \cdot \hat{y}_j(1 - \hat{y}_j) + \sum_{k \neq j} \frac{y_k}{\hat{y}_k} \cdot \hat{y}_k(1 - \frac{\sum_{i \neq k}e^{\beta_i}}{e^{\beta_j}}\hat{y}_k) \\
& = -y_{j} (1 - \hat{y}_j) + \sum_{k \neq j} y_{k}(1 - \frac{\sum_{i \neq k}e^{\beta_i}}{e^{\beta_j}}\hat{y}_k) \\
\end{aligned}
$

**(3)**

二分类, 即 $l = 1$.

对于 (2) 中的结果带入 $j = 1$ 即有

$
\begin{aligned}
\frac{\partial \ell(\bm{y}, \hat{\bm{y}})}{\partial \beta_1}
& = y_1(\hat{y}_1 - 1) + y_0(1 - \frac{\beta_1}{\beta_1}\hat{y}_0) \\
& = y_1(\hat{y}_1 - 1) + (1 - y_1)\hat{y}_1 \\
& = \hat{y}_1 - y_{1} \\
\end{aligned}
$

和 (1) 中的结果相同, 因为 (1) 中的 $y$ 即为 $y_1$, 他们的计算结果均为 $\hat{y}_1 - y_1$.

而 Sigmoid 函数 $\displaystyle \operatorname{sigmoid}(x) = \frac{1}{1 + e^{-x}}$ 也与 Softmax 函数 $\displaystyle \operatorname{softmax}(x_1, x_2) = \frac{e^{x_1}}{e^{x_1} + e^{x_2}} = \frac{1}{1 + e^{-(x_1-x_2)}}$ 完全相同 (在 $x = x_1 - x_2$ 的定义的基础上).

虽然说在理论上对于二分类问题 Sigmoid 函数与 Softmax 函数完全相同, 但是对于建模之后的实际模型还是有所不同的.

Softmax 对两个类别均输出对应的概率, 并且两个类别概率的和为 $1$; Sigmoid 只输出一个类别的概率, 另一个类别使用 $1$ 减去前一类别的概率取得, 因此两个类别概率和仍为 $1$. 但是 Softmax 输出两类的概率, 而 Sigmoid 只输出一个类别的概率. 因此在实际模型构建和计算中, 肯定也还是会有所不同.

**(4)**

$
\begin{aligned}
\displaystyle D_{\mathrm{KL}}(P || Q) & = \sum_{x \in \mathcal{X}}P(x)\log(\frac{P(x)}{Q(x)})  \\
& = \sum_{x \in \mathcal{X}}P(x)\log P(x) - \sum_{x \in \mathcal{X}}P(x)\log Q(x)  \\
& = b - \sum_{x \in \mathcal{X}}P(x)\log Q(x)  \\
& = b + \ell(\bm{y}, \hat{\bm{y}})  \\
\end{aligned}
$

其中 $x$ 为第几个类别 (也即是 $j$), $\mathcal{X}$ 是类别的取值空间, $P(x) = P(j) = y_j, Q(x) = Q(j) = \hat{y}_j$,

则我们有 $D_{\mathrm{KL}}(P || Q) = b + \ell(\bm{y}, \hat{\bm{y}})$, 其中 $b$ 只与 $P(x)$ 有关, 因此在 $P(x)$ 即 $y_j$ 分布不变的情况下可以视为一个常数.

所以我们可知, $D_{\mathrm{KL}}(P || Q)$ 与 $\ell(\bm{y}, \hat{\bm{y}})$ 只在所加的常数上有所区别. 我们最小化 $D_{\mathrm{KL}}(P || Q)$ 等价于最小化 $\ell(\bm{y}, \hat{\bm{y}})$.


## 二、

**(1)**

使用 numpy 可以有两种方式将向量距离矩阵计算出来.

一种是使用 numpy 的张量功能 (这里即为 3 阶张量, 即三维数组), 通过生成新的维度即可保证不互相冲突. 然后一句简洁的 `np.sqrt(((X[:, np.newaxis, :] - X[np.newaxis, :, :])**2).sum(axis=-1))` 即可计算出结果. 我们记这种方法为 `tensor_distance_function()`.

另一种是将 $\sum_{i=1}^{d}(x_i-y_i)^{2}$ 拆分成 $\sum_{i=1}^{d}x_i^{2} + \sum_{i=1}^{d}y_i^{2} - 2\sum_{i=1}^{d}x_iy_i$, 即拆分成三个不同的矩阵分别计算. 我们记这种方法为 `matrix_distance_function()`.

为了计算第一个矩阵 $\sum_{i=1}^{d}x_i^{2}$, 即 $\bm{X}$ 的所有行向量逐元素平方后与 $\bm{1}$ 向量点乘. 我们首先要定义一个 $d \times m$ 的全一矩阵 $\bm{1}$, 然后就可以通过 $\bm{M}_1 = \operatorname{square}(X) \cdot \bm{1}$ 计算出第一个矩阵; 第二个矩阵 $\sum_{i=1}^{d}y_i^{2}$ 可以通过 $\bm{M}_1$ 转置生成, 即 $\bm{M}_2 = \bm{M}_1^{\mathrm{T}}$; 而 $\sum_{i=1}^{d}x_i y_i$ 矩阵则更为简单, 通过点乘即 $\bm{M}_3 = \bm{X} \cdot \bm{X}^{\mathrm{T}}$ 即可计算出第三个矩阵.

最后对这三个矩阵加权求和并开方即可算出最后的矩阵, 即 $\bm{M} = \operatorname{sqrt}(\bm{M}_1 + \bm{M}_2 - 2 \bm{M}_3)$.

不过这个式子理论上正确, 实际上却会出问题. 对角线元素本来应该计算为 $0$, 不过由于计算的误差, 计算结果很有可能生成一个非常小的负数, 而负数是无法开方的, 导致生成 $\mathrm{NaN}$ 而计算结果出错. 所以我们需要在原来式子基础上加上一个很小的正数, 最终为 $\bm{M} = \operatorname{sqrt}(\bm{M}_1 + \bm{M}_2 - 2 \bm{M}_3 + 10^{-10} \cdot \bm{1})$

最终计算结果如下 ($m$ 和 $d$ 为矩阵维度, $n$ 代表循环次数):

| size | plain | tensor | matrix |
| ----|------|-----|----|
| $m = 10, d = 10, n = 10000$ | $16.97 \text{ s}$ | $0.23 \text{ s}$ | $0.39 \text{ s}$ |
| $m = 1000, d = 1000, n = 10$ | $179.39 \text{ s}$ | $186.22 \text{ s}$ | $0.93 \text{ s}$ |

可以看出, 对于维度小的矩阵, 使用张量法和矩阵法效率差不多, 而且运行时间是朴素方法的 $1 / 100$ 级别; 对于维度大的矩阵, 使用矩阵法的运行时间 $0.93$ 秒远远小于张量法和朴素法的超过 $100$ 秒. 

因此, 对于这个问题, 使用矩阵法所取得的效果十分显著.

**(2)**

我们可以对于任何一个给定的排列 $\bm{p} = \{ p_1, p_2, \cdots, p_m \}$, 生成一个 $m \times m$ permutation 矩阵 $\bm{P}$. 其中 $\bm{P}$ 矩阵的生成方式为, 对于矩阵 $\bm{P}$ 第 $i$ 行, 在第 $p_i$ 列的位置置 $1$, 其余均为 $0$. 则 $\bm{X}' = \bm{P} \cdot \bm{X}$ 则为重新排列行向量的矩阵.

最终计算结果如下 ($m$ 和 $d$ 为矩阵维度, $n$ 代表循环次数):

| size | plain | matrix |
| ----|------|-----|----|
| $m = 10, d = 10, n = 100000$ | $3.90 \text{ s}$ | $2.18 \text{ s}$ |
| $m = 1000, d = 1000, n = 1000$ | $12.69 \text{ s}$ | $63.58 \text{ s}$ |

可以看出, 对于维度小的矩阵, 使用朴素法和矩阵法效率差不多, 矩阵法最多比朴素法快了 $1 / 3$; 但是对于维度大的矩阵就恰好相反了, 因为矩阵法每次都需要生成巨大的 permutation 矩阵 $\bm{P}$, 最后总耗时反而是朴素法的 $6$ 倍.


## 三、

**(1)**

我们对每个样例 $(\bm{x}_i, y_i)$ 附上一个代价系数 $k_i$,

其中 $\displaystyle k_i = \begin{cases} 1, & y_i = +1 \\ k, & y_i = -1 \end{cases}$ 也即 $\displaystyle k_i = 1 - \frac{1}{2}(k - 1)(y_i - 1)$.

然后相应的 SVM 优化问题即可改为

$$
\begin{aligned}
\min_{\bm{w}, b, \xi_i} &\quad \frac{1}{2}\left\| \bm{w} \right\|_{2}^{2} + C\sum_{i=1}^{m}k_i\xi_i \\
\text{s.t.}
&\quad y_i(\bm{w}^{\mathrm{T}}\bm{x}_i + b) \ge 1 - \xi_i  \\
&\quad \xi_i \ge 0, i \in [m]  \\
\end{aligned}
$$

**(2)**

通过拉格朗日乘子法得到拉格朗日函数

$$
\begin{aligned}
L(\bm{w}, b, \bm{\alpha}, \bm{\xi}, \bm{\mu}) & = \frac{1}{2} \left\| \bm{w} \right\|_{2}^{2} + C\sum_{i=1}^{m}k_i\xi_i  \\
& \quad +\sum_{i=1}^{m}\alpha_i(1-\xi_i-y_i(\bm{w}^{\mathrm{T}}\bm{x}_i + b)) - \sum_{i=1}^{m}\mu_i\xi_i  \\
\end{aligned}
$$

其中 $\alpha_i \ge 0, \mu_i \ge 0$ 是拉格朗日乘子.

令 $L(\bm{w}, b, \bm{\alpha}, \bm{\xi}, \bm{\mu})$ 对 $\bm{w}, b, \xi_i$ 的偏导等于零可得

$$
\bm{w} = \sum_{i=1}^{m}\alpha_i y_i \bm{x}_i
$$

$$
0 = \sum_{i=1}^{m}\alpha_i y_i
$$

$$
k_i C = \alpha_i + \mu_i
$$

将上三式逐步带入有

$$
\begin{aligned}
&\quad L(\bm{w}, b, \bm{\alpha}, \bm{\xi}, \bm{\mu}) \\
&= \frac{1}{2} \left\| \bm{w} \right\|_{2}^{2} + C\sum_{i=1}^{m}k_i\xi_i + \sum_{i=1}^{m}\alpha_i(1-\xi_i-y_i(\bm{w}^{\mathrm{T}}\bm{x}_i + b)) - \sum_{i=1}^{m}\mu_i\xi_i \\
&= \frac{1}{2} \left\| \bm{w} \right\|_{2}^{2} + \sum_{i=1}^{m}\alpha_i(1-y_i(\bm{w}^{\mathrm{T}}\bm{x}_i + b)) + C\sum_{i=1}^{m}k_i\xi_i - \sum_{i=1}^{m}\alpha_i\xi_i - \sum_{i=1}^{m}\mu_i\xi_i \\
&= -\frac{1}{2}\sum_{i=1}^{m}\alpha_i y_i \bm{x}_i^{\mathrm{T}}\sum_{i=1}^{m}\alpha_i y_i \bm{x}_i + \sum_{i=1}^{m}\alpha_i + \sum_{i=1}^{m}k_i C \xi_i - \sum_{i=1}^{m}\alpha_i\xi_i - \sum_{i=1}^{m}\mu_i\xi_i \\
&= -\frac{1}{2}\sum_{i=1}^{m}\alpha_i y_i \bm{x}_i^{\mathrm{T}}\sum_{i=1}^{m}\alpha_i y_i \bm{x}_i + \sum_{i=1}^{m}\alpha_i + \sum_{i=1}^{m}(k_i C - \alpha_i - \mu_i)\xi_i \\
&= \sum_{i=1}^{m}\alpha_i - \frac{1}{2}\sum_{i=1}^{m}\sum_{j=1}^{m}\alpha_i\alpha_j y_i y_j\bm{x}_i^{\mathrm{T}}\bm{x}_j \\
\end{aligned}
$$

又因为 $\alpha_i \ge 0, \mu_i \ge 0, k_i C = \alpha_i + \mu_i$,

消去 $\mu_i$ 即可得到约束条件 $0 \le \alpha_i \le k_i C$.

因此对偶问题为

$$
\begin{aligned}
\max_{\bm{\alpha}} &\quad \sum_{i=1}^{m}\alpha_i - \frac{1}{2}\sum_{i=1}^{m}\sum_{j=1}^{m}\alpha_i\alpha_j y_i y_j\bm{x}_i^{\mathrm{T}}\bm{x}_j\\
\text{s.t.}
&\quad \sum_{i=1}^{m}\alpha_i y_i = 0  \\
&\quad 0 \le \alpha_i \le k_i C  \\
\end{aligned}
$$

其中 $\displaystyle k_i = \begin{cases} 1, & y_i = +1 \\ k, & y_i = -1 \end{cases}$ 也即 $\displaystyle k_i = 1 - \frac{1}{2}(k - 1)(y_i - 1)$.

根据 (1) 中的原优化问题所需满足的条件 $y_i(\bm{w}^{\mathrm{T}}\bm{x}_i + b) \ge 1 - \xi_i$ 可知 $\alpha_i(y_i f(\bm{x}_i) - 1 + \xi_i) = 0$, 根据 $\xi_i \ge 0$ 可知 $\mu_i \xi_i = 0$.

因此, KKT 条件要求

$$
\begin{cases}
\alpha_i \ge 0, \mu_i \ge 0,  \\
y_i f(\bm{x}_i) - 1 + \xi_i \ge 0,  \\
\alpha_i(y_i f(\bm{x}_i) - 1 + \xi_i) = 0,  \\
\xi_i \ge 0, \mu_i \xi_i = 0.
\end{cases}
$$





