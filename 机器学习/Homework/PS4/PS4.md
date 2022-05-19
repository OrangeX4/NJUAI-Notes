# PS4

## 一、



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

<!-- elapsed time for small scale and plain function: 16.966638803482056
elapsed time for small scale and matrix function: 0.39102745056152344
elapsed time for small scale and tensor function: 0.2259986400604248
elapsed time for large scale and plain function: 179.38620924949646
elapsed time for large scale and matrix function: 0.9318420886993408
elapsed time for large scale and tensor function: 186.22054433822632 -->

可以看出, 对于维度小的矩阵, 使用张量法和矩阵法效率差不多, 而且运行时间是朴素方法的 $1 / 100$ 级别; 对于维度大的矩阵, 使用矩阵法的运行时间 $0.93$ 秒远远小于张量法和朴素法的超过 $100$ 秒. 

因此, 对于这个问题, 使用矩阵法所取得的效果十分显著.

**(2)**

我们可以对于任何一个给定的排列 $\bm{p} = \{ p_1, p_2, \cdots, p_m \}$, 生成一个 $m \times m$ permutation 矩阵 $\bm{P}$. 其中 $\bm{P}$ 矩阵的生成方式为, 对于矩阵 $\bm{P}$ 第 $i$ 行, 在第 $p_i$ 列的位置置 $1$, 其余均为 $0$. 则 $\bm{X}' = \bm{P} \cdot \bm{X}$ 则为重新排列行向量的矩阵.

最终计算结果如下 ($m$ 和 $d$ 为矩阵维度, $n$ 代表循环次数):

| size | plain | matrix |
| ----|------|-----|----|
| $m = 10, d = 10, n = 100000$ | $3.90 \text{ s}$ | $2.18 \text{ s}$ |
| $m = 1000, d = 1000, n = 1000$ | $12.69 \text{ s}$ | $63.58 \text{ s}$ |

<!-- elapsed time for small scale and plain function: 3.907089948654175
elapsed time for small scale and matrix function: 2.184194326400757
elapsed time for large scale and plain function: 12.69484281539917
elapsed time for large scale and matrix function: 63.58450651168823 -->

可以看出, 对于维度小的矩阵, 使用朴素法和矩阵法效率差不多, 矩阵法最多比朴素法快了 $1 / 3$; 但是对于维度大的矩阵就恰好相反了, 因为矩阵法每次都需要生成巨大的 permutation 矩阵 $\bm{P}$, 最后总耗时反而是朴素法的 $6$ 倍.