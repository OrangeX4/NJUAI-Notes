# PS5

<!-- ## 一、

**(1)**

我们设定一个新的分类 $c_h$, 用其来表示 "拒绝", 也就是交给人类专家处理. 则我们可知, 将 $\bm{x}$ 分类为 $c_h$ 的期望损失, 也即风险为 $\lambda_h$, 所以有 $R(c_h|\bm{x}) = c_h$.

令 $\mathcal{Y}' = \mathcal{Y} \cup \{ c_h \}$. 此时, 贝叶斯最优分类器 $h^{*}(\bm{x})$ 的表达式仍可以写为

$$
h^{*}(\bm{x}) = \argmin_{c \in \mathcal{Y}'} R(c|\bm{x})
$$

其中 $R(c_h|\bm{x}) = c_h$.

**(2)**

当 $R(c_h|\bm{x})$ 是 $R(c_i|\bm{x})$ 之中的最小值, 也就是 $\displaystyle c_h \le R(c_i|\bm{x})=\sum_{j=1}^{N}\lambda_{ij}P(c_j|\bm{x})$, 对于所有 $1 \le i \le N$ 时, 分类器将一直拒绝分类.

如果令表达式与 $\bm{x}$ 无关, 则我们有 $\displaystyle c_h \le \min\{ \sum_{j=1}^{N}\lambda_{ij}P(c_j|\bm{x}) \} = \min\{ \lambda_{ij} \}$. 也即是 $c_h$ 小于等于 $\lambda_{ij}$ 的最小值时.

当 $R(c_h|\bm{x})$ 是 $R(c_i|\bm{x})$ 之中的最大值, 也就是 $\displaystyle c_h \ge R(c_i|\bm{x})=\sum_{j=1}^{N}\lambda_{ij}P(c_j|\bm{x})$, 对于所有 $1 \le i \le N$ 时, 分类器将一直拒绝分类.

如果令表达式与 $\bm{x}$ 无关, 则我们有 $\displaystyle c_h \le \max\{ \sum_{j=1}^{N}\lambda_{ij}P(c_j|\bm{x}) \} = \max\{ \lambda_{ij} \}$. 也即是 $c_h$ 大于等于 $\lambda_{ij}$ 的最大值时.

**(3)**

我们将二分类问题两种分类的风险和拒绝的风险计算得

$R(c_1|\bm{x}) = \lambda_{11}P(c_1|\bm{x}) + \lambda_{12}P(c_2|\bm{x}) = 1-p_1$

$R(c_2|\bm{x}) = \lambda_{21}P(c_1|\bm{x}) + \lambda_{22}P(c_2|\bm{x}) = p_1$

$R(c_h|\bm{x}) = \lambda_h$

由贝叶斯最优分类器表达式 $\displaystyle h^{*}(\bm{x}) = \argmin_{c \in \mathcal{Y}'} R(c|\bm{x})$ 可知

当 $p_1 \le \lambda_h$ 且 $p_1 \le 1-p_1$, 即 $p_1 \le \min\{ \lambda_h, 0.5 \} = 0.3$ 时, 预测为第二类.

当 $\lambda_h \le 1-p_1$ 且 $\lambda_h \le p_1$, 即 $0.3 = \lambda_h \le p_1 \le 1-\lambda_h = 0.7$ 时, 拒绝预测.

当 $1-p_1 \le \lambda_h$ 且 $1-p_1 \le p_1$, 即 $p_1 \ge \max\{ 1-\lambda_h, 0.5 \} = 0.7$ 时, 预测为第二类.

则我们有 $\theta_1 = 0.3, \theta_2 = 0.7$.


## 二、

**(1)**

我们令 $D = \{ x_1, x_2, \cdots, x_{99} \}$.

使用最大似然估计, 假设硬币正面向上的概率为 $\theta$, 记 $x = 1$ 为正面朝上, $x = 0$ 为反面朝上. 则对数似然为

$$
\begin{aligned}
LL(\theta) &= \log P(D | \theta)  \\
&= \sum_{x \in D} \log P(x|\theta)  \\
&= \sum_{x \in D} \log \theta \\
&= 99\log \theta
\end{aligned}
$$

则参数 $\theta$ 的极大似然估计为 $\displaystyle \hat{\theta} = \argmax_{\theta} LL(\theta) = 1.0$.

则第 100 次抛硬币正面朝上的概率为 $P(1|\theta) = \theta = 1.0$.

**(2)**

如果依然使用频率主义学派的思想, 认为参数 $\theta$ 是一个客观存在的固定值, 那么根据专家的见解 "肯定有 50% 的概率正面向上", 则有 $\theta = 0.5$.

设前 $99$ 次均为正面为事件 $A$, 第 $100$ 次为正面为事件 $B$, 则有

$$
P(B|A) = \frac{P(B)P(A|B)}{P(A)} = \frac{\theta \cdot \theta^{99}}{\theta^{99}} = \theta = 0.5
$$

则在第 100 次抛硬币时, 其正面朝上的概率为 $P(B|A) = 0.5$.

如果使用贝叶斯学派的思想, 将 $P(x)=0.5$ 视作先验, 对其进行最大后验估计. 由于我们无法确定参数 $\theta$ 的分布, 因此我们也无法准确地计算出 $\hat{\theta}$ 的值, 也就无法知道最终的概率. 但是我们知道的是, 最终概率介于 $0.5$ 和 $1.0$ 之间, 具体的值依选取的分布而定. 


**(3)**

我们令 $D = \{ x_1, x_2, \cdots, x_{400} \}$.

首先做极大似然估计:

对数似然为

$$
\begin{aligned}
LL(\theta) &= \log P(D | \theta)  \\
&= \sum_{x \in D} \log P(x|\theta)  \\
&= 100\log \theta + 300\log (1-\theta) \\
&= 100(\log \theta + 3 \log(1-\theta))
\end{aligned}
$$

则参数 $\theta$ 的极大似然估计为 $\displaystyle \hat{\theta} = \argmax_{\theta} LL(\theta) = 0.25$.

然后做最大后验估计:

由贝叶斯公式可知

$$
P(\theta|D) = \frac{P(D|\theta)P(\theta)}{P(D)}
$$

由于先对于 $\theta$ 来说, $P(x)$ 与 $\theta$ 无关, 可以视作常数, 因此

$$
\hat{\theta} = \argmax_{\theta} P(\theta|D) = \argmax_{\theta} P(D|\theta)P(\theta)
$$

由于专家认为 $\displaystyle \theta \sim \mathcal{N}(\frac{1}{2}, \frac{1}{900})$, 因此先验为 $\displaystyle P(\theta) = \frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(\theta-\mu)^{2}}{2\sigma^{2}}} = \frac{1}{30\sqrt{2\pi}}e^{-450(\theta-0.5)^{2}}$.

则有

$$
\begin{aligned}
\hat{\theta} &= \argmax_{\theta} P(D|\theta)P(\theta)  \\
&= \argmax_{\theta} \theta^{100} \cdot (1-\theta)^{300} \cdot \frac{1}{30\sqrt{2\pi}}e^{-450(\theta-0.5)^{2}}  \\
&= \argmax_{\theta} 100\log\theta + 300\log(1-\theta) -450(\theta-0.5)^{2}  \\
&= \argmax_{\theta} 2\log\theta + 6\log(1-\theta) -9(\theta-0.5)^{2}  \\
\end{aligned}
$$

令 $L(\theta) = 2\log\theta + 6\log(1-\theta) -9(\theta-0.5)^{2}$, 则有

$$
\begin{aligned}
\frac{\mathrm{d}L(\theta)}{\mathrm{d}\theta}
&= \frac{2}{\theta} - \frac{6}{1-\theta} - 18\theta + 9  \\
&= \frac{- 18 \theta^{3} + 27 \theta^{2} - \theta - 2}{\theta (\theta - 1)}  \\
\end{aligned}
$$

令 $\displaystyle - 18 \theta^{3} + 27 \theta^{2} - \theta - 2 = 0$ 且 $0 < \theta < 1$ 可得 $\displaystyle \hat{\theta} = \theta = \frac{1}{3} \thickapprox 0.33$.

**(4)**

极大似然估计是频率主义学派的思想, 认为参数 $\theta$ 是一个客观存在的固定值, 可以通过优化似然函数等准则来确定参数值, 因此最后的估计出的 $\theta$ 是由所测数据唯一决定的, 不会被人类专家的先验概率知识影响, 因此得到的结果常常比较 "极端". 例如第 (1) 问中 $\theta$ 被干脆地估计成了 $1.0$, 也就是必然事件. 而第 (3) 问中地极大似然估计所得结果是 $0.25$, 比较偏离 $0.5$.

最大后验估计是贝叶斯学派地思想, 认为参数 $\theta$ 是未观察到的随机变量, 其本身也可以有分布, 而不是一个固定值. 所以我们可以引入人类专家的先验 $\theta \sim \mathcal{N}(\frac{1}{2}, \frac{1}{900})$, 然后用其参与 $\theta$ 的估计. 最后得出的结果受数据影响也较小, 因此最终结果 $0.33$ 没有那么偏离 $0.5$.


## 三、

**(1)**

检查训练集上类别分类情况可知, 分类为类别 $0$ 的数量为 $39$, 分类为类别 $0$ 的数量为 $37$, 分类为类别 $0$ 的数量为 $44$.

由题意可知 $n=120$. 设随机变量 $Y_0$ 为 $n$ 次中分类为类别 $0$ 的次数, $Y_1$ 为分为类别 $1$ 的次数, $Y_2$ 为分为类别 $2$ 的次数. 则我们有多项分布

$$
P(Y_0=y_0, Y_1=y_1, Y_2=y_2) = \frac{n!}{y_0!y_1!y_2!}p_0^{y_0}p_1^{y_1}p_2^{y_2}
$$

其中 $y_0+y_1+y_2=n$, $p_0+p_1+p_2=1$, $0 \le p_i \le 1$, 且 $p_0, p_1, p_2$ 分别对应分类为对应类别的概率.

由极大似然估计可知

$$
\begin{aligned}
\hat{p}_0, \hat{p}_1, \hat{p}_2 & = \argmax_{p_0, p_1, p_2}P(Y_0=39, Y_1=37, Y_2=44)  \\
& = \argmax_{p_0, p_1, p_2}\frac{120!}{39!37!44!}p_0^{39}p_1^{37}p_2^{44}  \\
& = \argmax_{p_0, p_1, p_2}39\log p_0 + 37\log p_1 + 44\log p_2  \\
\end{aligned}
$$

我们编写 Python 代码优化可得最终结果

$$
\hat{p}_0 = 0.32500634, \hat{p}_1 = 0.30835317, \hat{p}_2 = 0.3666405
$$

因此先验为

$$
P(y) = \begin{cases}
  0.32500634, & y = 0 \\
  0.30835317, & y = 1 \\
  0.3666405, & y = 2 \\
\end{cases}
$$

**(2)**

代码为:

```python
GNB_classifier = GaussianNB()
GNB_classifier.fit(feature_train, label_train)
print(f"score: {GNB_classifier.score(feature_test, label_test)}")
```

最终测试性能得分为 $0.9666667$.

**(3)**

代码为:

```python
GNB_classifier = GaussianNB(priors=[1./3., 1./3., 1./3.])
GNB_classifier.fit(feature_train, label_train)
print(f"score: {GNB_classifier.score(feature_test, label_test)}")
```

手动指定先验为三个类上的均匀分布, 即各个类均为 $\frac{1}{3}$, 最终测试性能得分仍为 $0.9666667$.

**(4)**

![](./images/Figure_1.png)

我们画出每个类别 ($y=0,1,2$) 下不同特征 $(x_1, x_2, x_3, x_4)$ 对应的频率直方图, 这些图像部分地展现了其真实的数值分布的形状, 我们可以根据这些图像形状判断出应该使用哪一类概率分布形式.

如图所示, 基本所有图像都呈现出 "中间高, 两边低" 的形状, 基本没有出现 "均匀分布" 或者 "多峰" 的形状, 因此我们选择高斯分布, 就能较为真实地反映条件概率的形式.


## 四、

**(1)**

AdaBoost 算法在获得 $H_{t-1}$ 之后样本分布会进行调整, 使下一轮的基学习器 $h_t$ 能纠正 $H_{t-1}$ 的一些错误. 理想的 $h_{t}$ 能够最小化

$$
\begin{aligned}
\ell_{\exp}(H_{t-1} + \alpha_{t} h_{t} | \mathcal{D}) & = \mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})(H_{t-1}(\bm{x}) + \alpha_{t}h_{t}(\bm{x}))}]  \\
& = \mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-1}(\bm{x})}e^{-\alpha_{t}f(\bm{x})h_{t}(\bm{x})}]  \\
\end{aligned}
$$

注意到 $f^{2}(\bm{x}) = h_{t}^{2}(\bm{x})=1$, 因此可以对 $e^{-\alpha_{t}f(\bm{x})h_{t}(\bm{x})}$ 的泰勒展式近似为

$$
\begin{aligned}
\ell_{\exp}(H_{t-1} + \alpha_{t} h_{t} | \mathcal{D}) & \simeq  \mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-1}(\bm{x})}(1-\alpha_{t}f(\bm{x})h_{t}(\bm{x}) + \frac{\alpha_{t}^{2}f^{2}(\bm{x})h_{t}^{2}(\bm{x})}{2})]  \\
& \simeq  \mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-1}(\bm{x})}(1-\alpha_{t}f(\bm{x})h_{t}(\bm{x}) + \frac{\alpha_{t}^{2}}{2})]  \\
\end{aligned}
$$

于是, 理想的基学习器

$$
\begin{aligned}
h_{t}(\bm{x}) & = \argmin_{h} \ell_{\exp}(H_{t-1}+\alpha_{t}h | \mathcal{D})  \\
& \simeq  \argmin_{h} \mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-1}(\bm{x})}(1-\alpha_{t}f(\bm{x})h(\bm{x}) + \frac{\alpha_{t}^{2}}{2})]  \\
& = \argmax_{h} \mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-1}(\bm{x})}f(\bm{x})h(\bm{x})]  \\
& = \argmax_{h} \mathbb{E}_{\bm{x}\sim \mathcal{D}}[\frac{e^{-f(\bm{x})H_{t-1}(\bm{x})}}{\mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-1}(\bm{x})}]}f(\bm{x})h(\bm{x})]  \\
\end{aligned}
$$

注意到 $\mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-1}(\bm{x})}]$ 是一个常数. 令 $\mathcal{D}_{t}$ 表示一个分布

$$
\mathcal{D}_{t}(\bm{x}) = \frac{\mathcal{D}(\bm{x})e^{-f(\bm{x})H_{t-1}(\bm{x})}}{\mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-1}(\bm{x})}]}
$$

则根据数学期望的定义, 这等价于令

$$
\begin{aligned}
h_{t}(\bm{x}) & = \argmax_{h} \mathbb{E}_{\bm{x}\sim \mathcal{D}}[\frac{e^{-f(\bm{x})H_{t-1}(\bm{x})}}{\mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-1}(\bm{x})}]}f(\bm{x})h(\bm{x})]  \\
& = \argmax_{h} \mathbb{E}_{\bm{x}\sim \mathcal{D}_{t}}[f(\bm{x})h(\bm{x})]  \\
\end{aligned}
$$

由 $f(\bm{x}), h(\bm{x}) \sim \{ -1, +1 \}$, 有

$$
f(\bm{x})h(\bm{x}) = 1-2\mathbb{I}(f(\bm{x}) \neq h(\bm{x}))
$$

则理想的基学习器

$$
h_{t}(\bm{x}) = \argmin_{h}\mathbb{E}_{\bm{x}\sim \mathcal{D}_{t}}[\mathbb{I}(f(\bm{x}) \neq h(\bm{x}))]
$$

考虑到 $\mathcal{D}_{t}$ 和 $\mathcal{D}_{t-1}$ 的关系, 有

$$
\begin{aligned}
\mathcal{D}_{t}(\bm{x}) & = \frac{\mathcal{D}(\bm{x})e^{-f(\bm{x})H_{t-1}(\bm{x})}}{\mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-1}(\bm{x})}]}  \\
& = \frac{\mathcal{D}(\bm{x})e^{-f(\bm{x})H_{t-2}(\bm{x})}e^{-f(\bm{x})\alpha_{t-1}h_{t-1}(\bm{x})}}{\mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-1}(\bm{x})}]}  \\
& = \mathcal{D}_{t-1}(\bm{x})e^{-f(\bm{x})\alpha_{t-1}h_{t-1}(\bm{x})}\frac{\mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-2}(\bm{x})}]}{\mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-1}(\bm{x})}]}  \\
\end{aligned}
$$

因此 $\mathcal{D}_{t}$ 和 $\mathcal{D}_{t-1}$ 的关系为

$$
\mathcal{D}_{t} = \frac{\mathcal{D}_{t-1}(\bm{x})e^{-f(\bm{x})\alpha_{t-1}h_{t-1}(\bm{x})}}{Z_{t-1}}
$$

其中规范化因子 $Z_{t-1}$ 为

$$
Z_{t-1} = \frac{\mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-1}(\bm{x})}]}{\mathbb{E}_{\bm{x}\sim \mathcal{D}}[e^{-f(\bm{x})H_{t-2}(\bm{x})}]}
$$

**(2)**

考虑指数损失函数 $e^{\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}$ 的含义. 对于任意一个样本 $\bm{x}$ 来说, 预测值 $H(\bm{x})$ 与真实值 $\bm{y}$ 越相近时, $\bm{y}^{\mathrm{T}}H(\bm{x})$ 就越大, 因此 $e^{\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}$ 就越小, 作为一个损失函数来说满足了需求.

假如 $H(\bm{x})$ 无法判断属于哪个类别, 则会有 $[H(\bm{x})]_{n} = 0$, 最后使得 $e^{\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}=1$, 恰好处于一个分隔线位置.

而加上了 $\frac{1}{N}$ 也是为了标准化损失函数的值域范围, 因为 $\bm{y}^{\mathrm{T}}H(\bm{x})$ 结果值受到分类数也就是 $N$ 的大小的影响, 因此应该乘上一个 $\frac{1}{N}$ 消除分类数目的影响.

**(3)**

可以将 $\ell_{\text{multi-exp}}$ 化为

$$
\ell_{\text{multi-exp}} = \mathbb{E}_{\bm{x}\sim \mathcal{D}}[\sum_{\bm{y}}P(\bm{y}|\bm{x})e^{-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}]
$$

并且我们知道 $\sum_{n=1}^{N}\bm{y}_{n}=\bm{1}\bm{y}=0$ 且 $\sum_{n=1}^{N}[H(\bm{x})]_{n}=\bm{1}H(\bm{x})=0$, 构造拉格朗日函数有

$$
L = \sum_{\bm{y}}\mathbb{E}_{\bm{x}\sim \mathcal{D}}[\sum_{\bm{y}}P(\bm{y}|\bm{x})e^{-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}] + \mu \bm{1}\bm{y} + \lambda \bm{1}H(\bm{x})
$$

若 $H(\bm{x})$ 能令指数损失函数最小化, 则对 $H(\bm{x})$ 求偏导得

$$
\begin{aligned}
\frac{\partial L}{\partial H(\bm{x})} & = \frac{\partial}{\partial H(\bm{x})}(\sum_{\bm{y}}\mathbb{E}_{\bm{x}\sim \mathcal{D}}[\sum_{\bm{y}}P(\bm{y}|\bm{x})e^{-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}] + \mu \bm{1}\bm{y} + \lambda \bm{1}H(\bm{x}))  \\
& = \sum_{\bm{y}}P(\bm{y}|\bm{x})\frac{\partial}{\partial H(\bm{x})}e^{-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})} + \lambda \bm{1}  \\
& = \sum_{\bm{y}}P(\bm{y}|\bm{x})e^{-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}\frac{\partial}{\partial H(\bm{x})}(-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})) + \lambda \bm{1}  \\
& = -\frac{1}{N}\sum_{\bm{y}}P(\bm{y}|\bm{x})e^{-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}\bm{y} + \lambda \bm{1}  \\
\end{aligned}
$$ -->

令该式等于零即有

$$
-\frac{1}{N}\sum_{\bm{y}}P(\bm{y}|\bm{x})e^{-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}\bm{y} + \lambda \bm{1} = 0
$$

两端同时乘上 $\bm{1}^{\mathrm{T}}$ 有

$$
-\frac{1}{N}\sum_{\bm{y}}P(\bm{y}|\bm{x})e^{-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}\bm{1}^{\mathrm{T}}\bm{y} + \lambda \bm{1}^{\mathrm{T}}\bm{1} = N\lambda = 0
$$

因此 $\lambda = 0$, 可以从原式中消除.

对于原式, 我们选取其中一个 $\bm{y}$, 将与 $\bm{y}$ 无关的项移到右侧

$$
P(\bm{y}|\bm{x})e^{-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}\bm{y} = - \sum_{\bm{y}' \neq \bm{y}}P(\bm{y}'|\bm{x})e^{-\frac{1}{N}\bm{y}'^{\mathrm{T}}H(\bm{x})}\bm{y}'
$$

不妨令 $\bm{y}_{n} = 1$, 则有 $\displaystyle \bm{y}_{n}' = -\frac{1}{N-1}$, 也就可以将式子

$$
P(\bm{y}|\bm{x})e^{-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}\bm{y}_{n} = - \sum_{\bm{y}' \neq \bm{y}}P(\bm{y}'|\bm{x})e^{-\frac{1}{N}\bm{y}'^{\mathrm{T}}H(\bm{x})}\bm{y}_{n}'
$$

变为

$$
P(\bm{y}|\bm{x})e^{-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})} = - \sum_{\bm{y}' \neq \bm{y}}P(\bm{y}'|\bm{x})e^{-\frac{1}{N}\bm{y}'^{\mathrm{T}}H(\bm{x})}(-\frac{1}{N-1})
$$

则我们有

$$
\sum_{\bm{y}' \neq \bm{y}}(P(\bm{y}'|\bm{x})e^{-\frac{1}{N}\bm{y}'^{\mathrm{T}}H(\bm{x})} - P(\bm{y}|\bm{x})e^{-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}) = 0
$$

对任意 $\bm{y}$ 都成立, 对 $N$ 个 $\bm{y}$ 对应的 $N$ 个式子进行变换, 则最终可推出

$$
P(\bm{y}'|\bm{x})e^{-\frac{1}{N}\bm{y}'^{\mathrm{T}}H(\bm{x})} = P(\bm{y}|\bm{x})e^{-\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})}
$$

对任意 $\bm{y} \neq \bm{y}'$ 都成立. 因此由

$$
e^{\frac{1}{N}\bm{y}^{\mathrm{T}}H(\bm{x})-\frac{1}{N}\bm{y}'^{\mathrm{T}}H(\bm{x})} = \frac{P(\bm{y}|\bm{x})}{P(\bm{y}'|\bm{x})}
$$

解得

$$
\bm{y}^{\mathrm{T}}H(\bm{x})-\bm{y}'^{\mathrm{T}}H(\bm{x}) = N \ln \frac{P(\bm{y}|\bm{x})}{P(\bm{y}'|\bm{x})}
$$

所以可知 $\bm{y}^{\mathrm{T}}H(\bm{x}) \ge \bm{y}'^{\mathrm{T}}H(\bm{x})$ 当且仅当 $P(\bm{y}|\bm{x}) \ge P(\bm{y}'|\bm{x})$, 对于 $\forall \bm{y}'$.

因此有

$$
\argmax_{\bm{y}}[\bm{y}^{\mathrm{T}}H(\bm{x})] = \argmax_{\bm{y}}P(\bm{y}|\bm{x})
$$

并且又有

$$
\begin{aligned}
\argmax_{\bm{y}}[\bm{y}^{\mathrm{T}}H(\bm{x})] & = \argmax_{n}\sum_{n'=1}^{N}\bm{y}_{n'}[H(\bm{x})]_{n'} \\
& = \argmax_{n}(1 \cdot [H(\bm{x})]_{n} + \sum_{n'\neq n}(-\frac{1}{N-1})[H(\bm{x})]_{n'}) \\
& = \argmax_{n}((1+\frac{1}{N-1})[H(\bm{x})]_{n} + \sum_{n' = 1}^{N}(-\frac{1}{N-1})[H(\bm{x})]_{n'})  \\
& = \argmax_{n} [H(\bm{x})]_{n}  \\
\end{aligned}
$$

这也就意味着目标函数 $\argmax_{n}[H(\bm{x})]_{n}$ 或 $\argmax_{\bm{y}}[\bm{y}^{\mathrm{T}}H(\bm{x})]$ 达到了贝叶斯最优错误率.


<!-- ## 五、

**(1)**

对式子展开则有

$$
\begin{aligned}
E_{bag} &= \mathbb{E}_{\bm{x}}[(\frac{1}{T}\sum_{t=1}^{T}\epsilon_{t}(\bm{x}))^{2}]  \\
&= \frac{1}{T^{2}}\mathbb{E}_{\bm{x}}[(\sum_{t=1}^{T}\epsilon_{t}(\bm{x}))^{2}]  \\
&= \frac{1}{T^{2}}\mathbb{E}_{\bm{x}}[\sum_{t=1}^{T}\epsilon_{t}(\bm{x})^{2} + 2\sum_{t < l}\epsilon_{t}(\bm{x})\epsilon_{l}(\bm{x})]  \\
&= \frac{1}{T^{2}}\sum_{t=1}^{T}\mathbb{E}_{\bm{x}}[\epsilon_{t}(\bm{x})^{2}] + \frac{2}{T^{2}}\sum_{t < l}\mathbb{E}_{\bm{x}}[\epsilon_{t}(\bm{x})\epsilon_{l}(\bm{x})]  \\
&= \frac{1}{T^{2}}\sum_{t=1}^{T}\mathbb{E}_{\bm{x}}[\epsilon_{t}(\bm{x})^{2}]  \\
&= \frac{1}{T}E_{av}  \\
\end{aligned}
$$

因此我们有 $E_{bag}$ 和 $E_{av}$ 关系为 $\displaystyle E_{bag} = \frac{1}{T}E_{av}$.

**(2)**

可构造出式子

$$
\begin{aligned}
&\quad\ \sum_{t < l}^{T}\mathbb{E}_{\bm{x}}[(\epsilon_{t}(\bm{x})-\epsilon_{l}(\bm{x}))^{2}]  \\
&= \mathbb{E}_{\bm{x}}[\sum_{t < l}^{T}(\epsilon_{t}(\bm{x})^{2}+\epsilon_{l}(\bm{x})^{2} - 2\epsilon_{t}(\bm{x})\epsilon_{l}(\bm{x}))]  \\
& = \mathbb{E}_{\bm{x}}[(T-1)\sum_{t=1}^{T}\epsilon_{t}(\bm{x})^{2} - 2\sum_{t < l}\epsilon_{t}(\bm{x})\epsilon_{l}(\bm{x})]  \\
& = (T-1)\sum_{t=1}^{T}\mathbb{E}_{\bm{x}}[\epsilon_{t}(\bm{x})^{2}] - 2\sum_{t < l}\mathbb{E}_{\bm{x}}[\epsilon_{t}(\bm{x})\epsilon_{l}(\bm{x})]  \\
& = T^{2}((\frac{1}{T}\sum_{t=1}^{T}\mathbb{E}_{\bm{x}}[\epsilon_{t}(\bm{x})^{2}]) - (\frac{1}{T^{2}}\sum_{t=1}^{T}\mathbb{E}_{\bm{x}}[\epsilon_{t}(\bm{x})^{2}] + \frac{2}{T^{2}}\sum_{t < l}\mathbb{E}_{\bm{x}}[\epsilon_{t}(\bm{x})\epsilon_{l}(\bm{x})]))  \\
& = T^{2}(E_{av} - E_{bag})  \\
& \ge 0  \\
\end{aligned}
$$

因此无需对 $\epsilon_{t}(\bm{x})$ 做任何假设即有 $E_{bag} \le E_{av}$.


## 六、

**(1)**

对于 Step 1:

由于我们有新 $\Gamma'$:

$$
\Gamma_{ij}' = \begin{cases}
1, & \left\| \bm{x}_{i} - \bm{\mu}_{j} \right\|^{2} \le \left\| \bm{x}_{i} - \bm{\mu}_{j'} \right\|^{2}, \forall j' \\
0, & \text{otherwise}
\end{cases}
$$

因此新目标函数值减去原目标函数值为

$$
\begin{aligned}
E' - E &= \sum_{i=1}^{m}\sum_{j=1}^{k}\Gamma'_{ij}\left\| \bm{x}_i - \bm{\mu}_j \right\|^{2} - \sum_{i=1}^{m}\sum_{j=1}^{k}\Gamma_{ij}\left\| \bm{x}_i - \bm{\mu}_j \right\|^{2} \\
&= \sum_{i=1}^{m}\sum_{j=1}^{k}(\Gamma'_{ij}-\Gamma_{ij})\left\| \bm{x}_i - \bm{\mu}_j \right\|^{2} \\
&= \sum_{i=1}^{m}(\left\| \bm{x}_i - \bm{\mu}_j \right\|^{2} - \left\| \bm{x}_i - \bm{\mu}_{j'} \right\|^{2}) \\
&\le 0
\end{aligned}
$$

其中 $\bm{\mu}_j$ 是离 $\bm{x}_i$ 最近的簇, 而 $\bm{\mu}_{j'}$ 可能是任意一个簇, 因此我们有 $E' \le E$. 即 Step 1 会使目标函数 $J$ 的值降低或不增加.

对于 Step 2:

对于任意一个簇 $j$ 来说, 它的簇中心原来是 $\bm{\mu}_{j}$, 可能是任意一个向量, 之后被优化为

$$
\bm{\mu}_j' = \frac{\sum_{i=1}^{m}\Gamma_{ij}\bm{x}_i}{\sum_{i=1}^{m}\Gamma_{ij}}
$$

原来的目标函数可以改写为

$$
E = \sum_{j=1}^{k}\sum_{i=1}^{m}\Gamma_{ij}\left\| \bm{x}_i - \bm{\mu}_j \right\|^{2}
$$

即交换求和符号, 这样我们只需要证明 $\displaystyle E_{j} = \sum_{i=1}^{m}\Gamma_{ij}\left\| \bm{x}_i - \bm{\mu}_j \right\|^{2}$ 降低或不增加即可.

$$
\begin{aligned}
E_j' - E_j & = \sum_{i=1}^{m}\Gamma_{ij}\left\| \bm{x}_i - \bm{\mu}_j' \right\|^{2} - \sum_{i=1}^{m}\Gamma_{ij}\left\| \bm{x}_i - \bm{\mu}_j \right\|^{2}  \\
& = \sum_{i=1}^{m}\Gamma_{ij}(\left\| \bm{x}_i - \bm{\mu}_j' \right\|^{2} - \left\| \bm{x}_i - \bm{\mu}_j \right\|^{2})  \\
& = \sum_{i=1}^{m}\Gamma_{ij}(\bm{x}_i - \bm{\mu}_j' + \bm{x}_i - \bm{\mu}_j)^{\mathrm{T}}(\bm{x}_i - \bm{\mu}_j' - \bm{x}_i + \bm{\mu}_j)  \\
& = \sum_{i=1}^{m}\Gamma_{ij}(\bm{\mu}_j - \bm{\mu}_j')^{\mathrm{T}}(2\bm{x}_i - \bm{\mu}_j' - \bm{\mu}_j)  \\
& = (\bm{\mu}_j - \bm{\mu}_j')^{\mathrm{T}}(2(\sum_{i=1}^{m}\Gamma_{ij}\bm{x}_i) - (\sum_{i=1}^{m}\Gamma_{ij})(\bm{\mu}_j' + \bm{\mu}_j))  \\
& = (\sum_{i=1}^{m}\Gamma_{ij})(\bm{\mu}_j - \bm{\mu}_j')^{\mathrm{T}}(2\frac{\sum_{i=1}^{m}\Gamma_{ij}\bm{x}_i}{\sum_{i=1}^{m}\Gamma_{ij}} - \bm{\mu}_j' - \bm{\mu}_j)  \\
& = (\sum_{i=1}^{m}\Gamma_{ij})(\bm{\mu}_j - \bm{\mu}_j')^{\mathrm{T}}(2\bm{\mu}_j' - \bm{\mu}_j' - \bm{\mu}_j)  \\
& = -(\sum_{i=1}^{m}\Gamma_{ij})(\bm{\mu}_j - \bm{\mu}_j')^{\mathrm{T}}(\bm{\mu}_j - \bm{\mu}_j')  \\
& \le 0  \\
\end{aligned}
$$

因此我们有 $E_j' - E_j$, 也即有 Step 2 会使目标函数 $J$ 的值降低或不增加.

**(2)**

假设算法不会在有限步内停止, 则目标函数的值 $E$ 一直在变化.

由 (1) 可知, 目标函数 $E$ 的值降低或不增加, 又因为 $E$ 一直在变化, 可以将一系列 $E$ 的值视作严格单调递减数列, 由于 $E \ge 0$, 有下界, 因此一定收敛.

并且我们可知, $E$ 的值由簇的分类 $C_j$ 和簇中心 $\bm{\mu}_j$ 唯一确定, 而 $\displaystyle \bm{\mu}_j = \frac{\sum_{i=1}^{m}\Gamma_{ij}\bm{x}_{i}}{\sum_{i=1}^{m}\Gamma_{ij}}$, 因此 $\bm{\mu}_j$ 也由 $C_j$ 唯一确定, 也即 $E$ 由 $C_j$ 唯一确定, 其中 $j = 1, \cdots, k$.

由于样本 $\bm{x}_i$ 是有限个的, 因此 $C_j$ 的划分方式是有限个的, 也就是 $E$ 的取值是离散的有限个的值, 再由 $E$ 是严格单调递减数列且有下界可知, 一定会有一个最小值 $E_{\min} \le E$, 对于任何一个 $E$ 值来说. 因此 $E$ 一定会在 $E_{\min}$ 的时候停止, 与假设矛盾.

因此算法会在有限步内停止.

**(3)**

假设我们对于 $k$ 已经有了目标函数的最小值 $E_{k}$, 也就是说此时的算法已经停止了, 有了一系列的簇中心 $\bm{\mu}_1, \cdots, \bm{\mu}_k$.

我们在这一系列簇中心的基础上, 加入一个随机的簇中心 $\bm{\mu}_{k+1}$, 令其等于任意一个样本, 形成一系列新的簇中心 $\bm{\mu}_1, \cdots, \bm{\mu}_k, \bm{\mu}_{k+1}$, 再重新将这一系列簇中心投入算法中.

在再次投入算法之前, 可以认为 $C_{k+1}$ 簇中没有任何样本, 因此此时目标函数值依然等于 $E_{k}$, 没有变化.

而由 (1) 可知, 等到算法终止之后, 目标函数的值 $E_{k+1}$ 也仍然只会降低或不增加.

这样, 我们便证明了目标函数的最小值是关于 $k$ 的非增函数. -->
