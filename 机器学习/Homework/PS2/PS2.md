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
