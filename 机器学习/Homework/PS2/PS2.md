# PS2

## 一、

**(1)**

依然有必要继续研究机器学习算法.

NFL 定理有一个重要的前提, 即所有的 "问题" 出现的机会相同, 即 $f$ 是均匀分布的, 但是实际上并不是这样. 对于某一类具体的问题来说, $f$ 一般都不是均匀分布的. 因此, 面对一个具体的问题, 一般都会有一个具体的机器学习算法, 能够取得比其他机器学习算法更好的结果.

**(2)**

对于一个有 $k$ 种分类结果的 $k$ 分类器来说, 其真实目标函数可以是任何函数 $\mathcal{X}\mapsto \{ 1,2,\cdots ,k \}$, 函数空间为 $\{ 1,2,\cdots ,k \}^{|\mathcal{X}|}$.

将 $f$ 视为遵循均匀分布, 则我们有预测正确的概率 $\displaystyle \operatorname{Pr}(h(\bm{x})=f(\bm{x}))=\frac{1}{k}$, 是一个常数. 预测错误的概率是 $\displaystyle \operatorname{Pr}(h(\bm{x})\neq f(\bm{x}))=\frac{k-1}{k}$.

对于分类问题, 任意一种性能度量 $\ell(h(\bm{x}), f(\bm{x}))$ 的输出只有两种结果, 设预测正确的结果为 $c_1$, 预测错误的结果为 $c_0$, 则有分布列 $\displaystyle \operatorname{Pr}(\ell(h(\bm{x}), f(\bm{x}))=c_1) = \frac{1}{k}$, $\displaystyle \operatorname{Pr}(\ell(h(\bm{x}), f(\bm{x}))=c_0) = \frac{k-1}{k}$.

那么有期望 $\displaystyle \mathbb{E}[\ell(h(\bm{x}), f(\bm{x}))] = \frac{1}{k}\cdot c_1+\frac{k-1}{k}\cdot c_0$, 我们可以设 $\displaystyle c=\frac{1}{k}\cdot c_1+\frac{k-1}{k}\cdot c_0$. 以二分类问题的错误率为例子, 此时 $\displaystyle c = \frac{1}{2}\cdot 0 + \frac{2-1}{2}\cdot 1 = \frac{1}{2}$. 

则我们有

$$
\begin{aligned}
\sum_{f}E_{ote}(\mathfrak{L}_{a}|X,f)
&=\sum_{f}\sum_{h}\sum_{\bm{x}\in \mathcal{X}-X}P(\bm{x})\ell(h(\bm{x}), f(\bm{x}))P(h|X,\mathfrak{L}_{a}) \\
&=\sum_{\bm{x}\in \mathcal{X}-X}P(\bm{x})\sum_{h}P(h|X,\mathfrak{L}_{a})\sum_{f}\ell(h(\bm{x}), f(\bm{x})) \\
&=\sum_{\bm{x}\in \mathcal{X}-X}P(\bm{x})\sum_{h}P(h|X,\mathfrak{L}_{a})ck^{|\mathcal{X}|} \\
&=ck^{|\mathcal{X}|}\sum_{\bm{x}\in \mathcal{X}-X}P(\bm{x})\sum_{h}P(h|X,\mathfrak{L}_{a}) \\
&=ck^{|\mathcal{X}|}\sum_{\bm{x}\in \mathcal{X}-X}P(\bm{x})\cdot 1 \\
\end{aligned}
$$

可以看出, 总误差依然与学习算法无关, 因此对于其他的性能度量, NFL 定理依然成立.


## 二、

我们定义 $\hat{\bm{w}} = [\bm{w}; b], \mathbf{X} = [\bm{X}, \bm{1}]$

则原式可用矩阵表示为

$$
(\bm{w}^{*}, b^{*}) = \hat{\bm{w}}^{*} = \argmin_{\hat{\bm{w}}}(\bm{y}-\mathbf{X}\hat{\bm{w}})^{\top}(\bm{y}-\mathbf{X}\hat{\bm{w}})
$$

令 $E_{\hat{\bm{w}}} = (\bm{y}-\mathbf{X}\hat{\bm{w}})^{\top}(\bm{y}-\mathbf{X}\hat{\bm{w}})$, 对 $\hat{\bm{w}}$ 求导得

$$
\frac{\partial \bm{E_{\hat{w}}}}{\partial \hat{\bm{w}}} = 2\mathbf{X}^{\top}(\mathbf{X}\hat{\bm{w}}-\bm{y})
$$

令上式等于零即可得到 $\hat{\bm{w}}$ 的最优解的闭式解.

当 $\mathbf{X}^{\top}\mathbf{X}$ 是满秩矩阵时, 令该式等于零即可得

$$
(\bm{w}^{*}, b^{*}) = \hat{\bm{w}}^{*} = (\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}\bm{y}
$$

令 $\hat{\bm{x}}_{i} = [\bm{x}_{i}, 1]$, 则最终线性回归模型为

$$
f(\hat{\bm{x}}_{i}) = \hat{\bm{x}}_{i}^{\top}(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}\bm{y}
$$


## 二、

原式可用矩阵表示为

$$
(\bm{w}^{*}, b^{*}) = \argmin_{(\bm{w}, b)}\frac{1}{2}(\bm{y}-\bm{X}\bm{w}-\bm{1}b)^{\top}(\bm{y}-\bm{X}\bm{w}-\bm{1}b)
$$

令 $\displaystyle \bm{E} = \frac{1}{2}(\bm{y}-\bm{X}\bm{w}-\bm{1}b)^{\top}(\bm{y}-\bm{X}\bm{w}-\bm{1}b)$

对 $\bm{w}$ 求导得

$$
\frac{\partial \bm{E}}{\partial \bm{w}} = \bm{X}^{\top}(\bm{X}\bm{w}+\bm{1}b-\bm{y})
$$

对 $b$ 求导得

$$
\frac{\partial \bm{E}}{\partial b} = \bm{1}^{\top}(\bm{X}\bm{w}+\bm{1}b-\bm{y})
$$

令上面两式同时等于零即可得到 $\bm{w}$ 和 $b$ 的最优解的闭式解.

当 $\bm{X}^{\top}\bm{X}$ 是满秩矩阵时, 则有

$$
\bm{w}^{*} = (\bm{X}^{\top}\bm{X})^{-1}\bm{X}^{\top}(\bm{y}-\bm{1}b^{*})
$$

令 $\bm{T} = (\bm{X}^{\top}\bm{X})^{-1}$, 则

$$
\bm{w}^{*} = \bm{T}\bm{X}^{\top}(\bm{y}-\bm{1}b^{*})
$$

代入有

$$
\begin{aligned}
b^{*}
&= \bm{1}^{\top}\bm{y} - \bm{1}^{\top}\bm{X}\bm{w}^{*}  \\
&= \bm{1}^{\top}\bm{y} - \bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}(\bm{y}-\bm{1}b^{*})  \\
&= \bm{1}^{\top}\bm{y} - \bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}\bm{y} + \bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}\bm{1}b^{*}  \\
\end{aligned}
$$

最后有

$$
b^{*} = \frac{\bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}\bm{y} - \bm{1}^{\top}\bm{y}}{\bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}\bm{1} - 1}
$$

最后将 $b^{*}$ 带回即可求出

$$
\bm{w}^{*} = \bm{T}\bm{X}^{\top}(\bm{y}-\bm{1}\frac{\bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}\bm{y} - \bm{1}^{\top}\bm{y}}{\bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}\bm{1} - 1})
$$


## 三、

**(1)**

令 $\displaystyle \bm{E} = \frac{1}{2}\left\| \bm{X}\bm{w}+\bm{1}b-\bm{y} \right\|_{2}^{2} + \lambda\left\| \bm{w} \right\|_{2}^{2}$

对 $\bm{w}$ 求导得

$$
\frac{\partial \bm{E}}{\partial \bm{w}} = \bm{X}^{\top}(\bm{X}\bm{w}+\bm{1}b-\bm{y}) + 2\lambda \bm{w}
$$

对 $b$ 求导得

$$
\frac{\partial \bm{E}}{\partial b} = \bm{1}^{\top}(\bm{X}\bm{w}+\bm{1}b-\bm{y})
$$

当 $(\bm{X}^{\top}\bm{X}+2\lambda \bm{I}_d)$ 是满秩矩阵时, 令该式等于零即可得

$$
\bm{w}^{*}_{\mathbf{Ridge}} = (\bm{X}^{\top}\bm{X}+2\lambda \bm{I}_d)^{-1}\bm{X}^{\top}(\bm{y}-\bm{1}b^{*}_{\mathbf{Ridge}})
$$

令 $\bm{T} = (\bm{X}^{\top}\bm{X}+2\lambda \bm{I}_d)^{-1}$, 则

$$
\bm{w}^{*}_{\mathbf{Ridge}} = \bm{T}\bm{X}^{\top}(\bm{y}-\bm{1}b^{*}_{\mathbf{Ridge}})
$$

代入有

$$
\begin{aligned}
b^{*}_{\mathbf{Ridge}}
&= \bm{1}^{\top}\bm{y} - \bm{1}^{\top}\bm{X}\bm{w}^{*}_{\mathbf{Ridge}}  \\
&= \bm{1}^{\top}\bm{y} - \bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}(\bm{y}-\bm{1}b^{*}_{\mathbf{Ridge}})  \\
&= \bm{1}^{\top}\bm{y} - \bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}\bm{y} + \bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}\bm{1}b^{*}_{\mathbf{Ridge}}  \\
\end{aligned}
$$

最后有

$$
b^{*}_{\mathbf{Ridge}} = \frac{\bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}\bm{y} - \bm{1}^{\top}\bm{y}}{\bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}\bm{1} - 1}
$$

最后将 $b^{*}_{\mathbf{Ridge}}$ 带回即可求出

$$
\bm{w}^{*}_{\mathbf{Ridge}} = \bm{T}\bm{X}^{\top}(\bm{y}-\bm{1}\frac{\bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}\bm{y} - \bm{1}^{\top}\bm{y}}{\bm{1}^{\top}\bm{X}\bm{T}\bm{X}^{\top}\bm{1} - 1})
$$

加上第二题的结果, 可以看出, 使用矩阵 $\bm{T}$ 抽象之后, 最优解和原始最优解的形式是一样的, 不同的是 $\bm{T}$ 的值, 二者的矩阵 $\bm{T}$ 括号内相差了一个 $2\lambda \bm{I}_d$ 项.

所以我们可以认为 $\bm{w}^{*}_{\mathbf{LS}}$ 和 $b^{*}_{\mathbf{LS}}$ 是 $\lambda=0$ 的 $\bm{w}^{*}_{\mathbf{Ridge}}$ 和 $b^{*}_{\mathbf{Ridge}}$ 特殊情况.

**(2)**

将恒等式

$$
\bm{X} = \bm{X}
$$

右端乘上 $(\bm{X}^{\top}\bm{X}+\lambda I_{d})(\bm{X}^{\top}\bm{X}+\lambda I_{d})^{-1}$ 即 $I_{d}$ 则有

$$
\bm{X} = \bm{X}(\bm{X}^{\top}\bm{X}+\lambda I_{d})(\bm{X}^{\top}\bm{X}+\lambda I_{d})^{-1}
$$

将 $\bm{X}$ 乘入括号内则有

$$
\bm{X} = (\bm{X}\bm{X}^{\top}\bm{X}+\lambda \bm{X})(\bm{X}^{\top}\bm{X}+\lambda I_{d})^{-1}
$$

再将 $\bm{X}$ 提出至右侧则有

$$
\bm{X} = (\bm{X}\bm{X}^{\top}+\lambda I_{m})\bm{X}(\bm{X}^{\top}\bm{X}+\lambda I_{d})^{-1}
$$

最后则有

$$
(\bm{X}\bm{X}^{\top}+\lambda I_{m})^{-1}\bm{X} = \bm{X}(\bm{X}^{\top}\bm{X}+\lambda I_{d})^{-1}
$$

式子成立.

这个结论能够帮助岭回归的计算.

当样例的维度 $d$ 大于样例数目 $m$ 的时候, 将 $\bm{X}(\bm{X}^{\top}\bm{X}+2\lambda I_{d})^{-1}$ 转为 $(\bm{X}\bm{X}^{\top}+2\lambda I_{m})^{-1}\bm{X}$ 能够将矩阵求逆求 $\bm{T}$ 的矩阵维度减少, 进而加快矩阵求逆的速度.

**(3)**

**(a)**

算出线性回归模型测试集上的 MSE 结果为 20.724023437336253.

**(b)**

取不同的权重所得结果为

| 0.0 | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 | 1.2 | 1.4 | 1.6 | 1.8 | 2.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| 20.72 | 20.92 | 21.09 | 21.21 | 21.31 | 21.39 | 21.4 | 21.50 | 21.54 | 21.57 | 21.60 |

![](./Figure_1.png)

可以看出, MSE 随着 $\lambda$ 的增大而缓慢增大, 所以我们可以选择一个相对较小但仍然为正数的 $\lambda$ 值.


## 四、

**(1)**

由贝叶斯公式可知

$$
\begin{aligned}
p(y=n|\bm{x}) & = \frac{p(y=n)p(\bm{x}|y=n)}{p(\bm{x})}  \\
& = \frac{\displaystyle \pi_{n}\cdot ((2\pi)^{\frac{d}{2}}\det (\bm{\Sigma})^{\frac{1}{2}})^{-1}\exp (-\frac{1}{2}(\bm{x}-\bm{\mu}_{n})^{\top}\bm{\Sigma}^{-1}(\bm{x}-\bm{\mu}_{n}))}{p(\bm{x})}  \\
& = \frac{\displaystyle \pi_{n}\cdot ((2\pi)^{\frac{d}{2}}\det (\bm{\Sigma})^{\frac{1}{2}})^{-1}\exp (\bm{x}^{\top}\bm{\Sigma}^{-1}\bm{\mu}_{n}-\frac{1}{2}\bm{\mu}_{n}^{\top}\bm{\Sigma}^{-1}\bm{\mu}_{n}-\frac{1}{2}\bm{x}^{\top}\bm{\Sigma}^{-1}\bm{x})}{p(\bm{x})}  \\
\end{aligned}
$$

并且 $\argmax_{n}p(y=m|\bm{x})$ 可以转化为 $\argmax_{n}\ln p(y=m|\bm{x})$ 即有

$$
\begin{aligned}
\argmax_{n} &\ln \pi_{n}+\ln ((2\pi)^{\frac{d}{2}}\det (\bm{\Sigma})^{\frac{1}{2}})^{-1}+\bm{x}^{\top}\bm{\Sigma}^{-1}\bm{\mu}_{n} \\&-\frac{1}{2}\bm{\mu}_{n}^{\top}\bm{\Sigma}^{-1}\bm{\mu}_{n}-\frac{1}{2}\bm{x}^{\top}\bm{\Sigma}^{-1}\bm{x}-\ln p(\bm{x}) \\
\end{aligned}
$$

去除与 $n$ 无关的项即可得

$$
\argmax_{n} \bm{x}^{\top}\bm{\Sigma}^{-1}\bm{\mu}_{n}-\frac{1}{2}\bm{\mu}_{n}^{\top}\bm{\Sigma}^{-1}\bm{\mu}_{n}+\ln \pi_{n}
$$

**(2)**

将式子

$$
\bm{x}^{\top}\hat{\bm{\Sigma}}^{-1}(\hat{\bm{\mu}}_{2}-\hat{\bm{\mu}}_{1}) > \frac{1}{2}(\hat{\bm{\mu}}_{2}-\hat{\bm{\mu}}_{1})^{\top}\hat{\bm{\Sigma}}^{-1}(\hat{\bm{\mu}}_{2} - \hat{\bm{\mu}}_{1}) - \ln \frac{m_{2}}{m_{1}}
$$

拆开可得

$$
\bm{x}^{\top}\hat{\bm{\Sigma}}^{-1}\hat{\bm{\mu}}_{2} - \bm{x}^{\top}\hat{\bm{\Sigma}}^{-1}\hat{\bm{\mu}}_{1} > \frac{1}{2}\hat{\bm{\mu}}_{2}^{\top}\hat{\bm{\Sigma}}^{-1}\hat{\bm{\mu}}_{2} - \frac{1}{2}\hat{\bm{\mu}}_{1}^{\top}\hat{\bm{\Sigma}}^{-1}\hat{\bm{\mu}}_{1}-\ln \frac{m_{2}}{m_{1}}
$$

进行移项

$$
\bm{x}^{\top}\hat{\bm{\Sigma}}^{-1}\hat{\bm{\mu}}_{2}-\frac{1}{2}\hat{\bm{\mu}}_{2}^{\top}\hat{\bm{\Sigma}}^{-1}\hat{\bm{\mu}}_{2}+\ln \frac{m_{2}}{m} > \bm{x}^{\top}\hat{\bm{\Sigma}}^{-1}\hat{\bm{\mu}}_{1}-\frac{1}{2}\hat{\bm{\mu}}_{1}^{\top}\hat{\bm{\Sigma}}^{-1}\hat{\bm{\mu}}_{1}+\ln \frac{m_{1}}{m}
$$

将 $\displaystyle \ln \frac{m_{n}}{m}$ 替换为 $\ln \hat{\pi}_{n}$ 可得

$$
\bm{x}^{\top}\hat{\bm{\Sigma}}^{-1}\hat{\bm{\mu}}_{2}-\frac{1}{2}\hat{\bm{\mu}}_{2}^{\top}\hat{\bm{\Sigma}}^{-1}\hat{\bm{\mu}}_{2}+\ln \hat{\pi}_{2} > \bm{x}^{\top}\hat{\bm{\Sigma}}^{-1}\hat{\bm{\mu}}_{1}-\frac{1}{2}\hat{\bm{\mu}}_{1}^{\top}\hat{\bm{\Sigma}}^{-1}\hat{\bm{\mu}}_{1}+\ln \hat{\pi}_{1}
$$

即有 $n^{*} = \argmax_{n} \bm{x}^{\top}\bm{\Sigma}^{-1}\bm{\mu}_{n}-\frac{1}{2}\bm{\mu}_{n}^{\top}\bm{\Sigma}^{-1}\bm{\mu}_{n}+\ln \pi_{n} = 2$

所以此时 LDA 将样例预测为第 2 类.

几何意义:

$\displaystyle \frac{1}{2}(\hat{\bm{\mu}}_{2}+\hat{\bm{\mu}}_{1})$ 是 $\hat{\bm{\mu}}_{1}$ 和 $\hat{\bm{\mu}}_{2}$ 这两个类别中心的中点.

而 $x^{\top}\hat{\bm{\Sigma}}^{-1}(\hat{\bm{\mu}}_{2}-\hat{\bm{\mu}}_{1})$ 可以化为 $(\hat{\bm{\Sigma}}^{-\frac{1}{2}}x)^{\top}(\hat{\bm{\Sigma}}^{-\frac{1}{2}}(\hat{\bm{\mu}}_{2}-\hat{\bm{\mu}}_{1}))$

即将特殊的多维正态分布缩放旋转成了标准多维正态分布, 然后衡量离第 1 类的类别中心 $\hat{\bm{\mu}}_{1}$ 的远近.

若大于号成立, 说明 $\bm{x}$ 比中点 $\displaystyle \frac{1}{2}(\hat{\bm{\mu}}_{1}+\hat{\bm{\mu}}_{2})$ 离 $\hat{\bm{\mu}}_{1}$ 更远, 也就是离 $\hat{\bm{\mu}}_{2}$ 更近.

但是还要考虑一个因素, 如果第 2 类的样例比第 1 类的样例数目多, 就要加入一定的偏好, 比如这里的对数几率 $\ln (m_2 / m_1)$, 当 $m_2 > m_1$ 时是正数, 就能更容易判断为第 2 类.

**(3)**

求解

$$
\max_{\bm{W}} \frac{\operatorname{tr}(\bm{W}^{\top}\bm{S}_{b}\bm{W})}{\operatorname{tr}(\bm{W}^{\top}\bm{S}_{w}\bm{W})}
$$

最后可以转化为广义特征值问题求解

$$
\bm{S}_{b}\bm{W} = \lambda \bm{S}_{w}\bm{W}
$$

即求解

$$
\bm{S}_{w}^{-1}\bm{S}_{b}\bm{W} = \lambda \bm{W}
$$

也就是求 $\bm{S}_{w}^{-1}\bm{S}_{b}$ 特征值最大的前几个的特征向量.

而我们知道

$$
\bm{S}_{b} = \sum_{i=1}^{N} m_{i}(\bm{\mu}_{i}-\bm{\mu})(\bm{\mu}_{i}-\bm{\mu})^{\top}
$$

因此我们有

$$
\begin{aligned}
\operatorname{rank}(\bm{S}_{w}^{-1}\bm{S}_{b})
&\le \min\{ \operatorname{rank}(\bm{S}_{w}^{-1}), \operatorname{rank}(\bm{S}_{b}) \}  \\
&\le \operatorname{rank}(\bm{S}_{b})  \\
&= \operatorname{rank}(\sum_{i=1}^{N} m_{i}(\bm{\mu}_{i}-\bm{\mu})(\bm{\mu}_{i}-\bm{\mu})^{\top})  \\
&\le \sum_{i=1}^{N} \operatorname{rank}((\bm{\mu}_{i}-\bm{\mu})(\bm{\mu}_{i}-\bm{\mu})^{\top})  \\
&= \sum_{i=1}^{N} \operatorname{rank}(\bm{\mu}_{i}-\bm{\mu})  \\
&= N \\
\end{aligned}
$$

因此 $\bm{S}_{w}^{-1}\bm{S}_{b}$ 最多有 $N$ 个非零特征值, 如果选取所有的特征值, 相当于选取了所有的有效特征向量, 也就没有投影的意义了; 所以我们最多只能从 $N$ 个特征值中选择其中最大的 $N-1$ 个特征值, 对应 $N-1$ 个特征向量. 

所以 FDA 投影的维度最多为 $N-1$.

## 五、

**(1)**

OvO 的优势: OvO 的每个分类器仅用到两个类的样例, 在类别很多的时候, OvO 的训练时间开销通常比 OvR 小.

OvO 的劣势: OvO 需要训练 $N(N-1)/2$ 个分类器, 所以存储开销和训练时间开销通常比较大.

OvR 的优势: OvR 只需要训练 $N$ 个分类器.

OvR 的劣势: 每次训练时都用到了所有的数据, 在类别很多的时候, 训练时间开销更大.

这两种多分类推广方式都可能存在难以处理的情况.

例如对 OvR 来说, 如果类别特别多的时候, 每次都要使用全部的数据来处理, 时间开销就接近 $O(n^{2})$ 了, 几乎是不可接受的.

即使是对于 OvO 来说, 我们也能构造出一个类似的例子, 例如有一半的样例都是属于第 0 类, 但是剩下的一半几乎每个样例都对应一个类别, 这样时间开销和空间开销也都到达了 $O(n^{2})$ 了, 也几乎是不可接受的.

**(2)**

对 OvR 来说, 由于对每一个类进行了相同的处理, 其拆解出来的二分类任务中类别不平衡的影响会相互抵消, 因此通常不需要显式考虑正负类别不平衡带来的影响.
