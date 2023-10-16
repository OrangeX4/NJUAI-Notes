#import "../../../Typst/report-template.typ": *
#import "../../../Typst/typst-sympy-calculator.typ": *

#set heading(numbering: Numbering.with(base: 2, "(a)"))

// apply the template
#show: report.with(
    size: 12pt,
    subject: "模式识别", 
    title: "HW4", 
    date: "2023 年春季", 
    author: "201300035 方盛俊 人工智能学院",
    show-outline: false,
)


= 习题一

==

使用 Python 进行调用, 代码为:

```python
from liblinear.liblinearutil import *

mnist = svm_read_problem('mnist')
mnist_t = svm_read_problem('mnist.t')

# 使用默认参数训练模型
default_model = train(mnist[0], mnist[1])
# 在测试集上的准确率
print("default_model:")
p_label, p_acc, p_val = predict(mnist_t[0], mnist_t[1], default_model)

# 对每个训练和测试样例的特征值进行开根变换
def sqrt_data(data):
    sqrt_data = ([*data[0]], [*data[1]])
    for i in range(len(sqrt_data[1])):
        sqrt_data[1][i] = {key: sqrt_data[1][i][key] ** 0.5 for key in sqrt_data[1][i]}
    return sqrt_data

sqrt_mnist = sqrt_data(mnist)
sqrt_mnist_t = sqrt_data(mnist_t)
sqrt_model = train(sqrt_mnist[0], sqrt_mnist[1])
print("sqrt_model:")
sqrt_p_label, sqrt_p_acc, sqrt_p_val = predict(sqrt_mnist_t[0], sqrt_mnist_t[1], sqrt_model)
```

==

使用默认参数训练与测试得到的准确率为:

```txt
default_model:
Accuracy = 91.53% (9153/10000) (classification)
```

==

使用 $x arrow.l sqrt(x)$ 变换得到的数据进行训练与测试得到的准确率为:

```txt
sqrt_model:
Accuracy = 91.37% (9137/10000) (classification)
```

==

得到的准确率和后一问的准确率几乎相同, 且为极高的 91.53% 与 91.37%. 据猜测, 可能是软件版本更新导致默认参数发生了变化.

按照正常想法来说, 开根变换后准确率应该会有所上升. 这是因为未经过缩放的原 mnist 数据集的特征取值范围较大, 且不同特征之间的取值范围又不一致, 导致数值较大的特征对最终结果影响较大. 经过开根变换后, 近似相当于将取值范围进行了缩小, 变得接近于经过缩放的数据 (scaled mnist), 因此最终准确率会有所上升.


= 习题二

==

$ 1 - sigma(x) = 1 - 1 / (1 + e^(-x)) = e^(-x) / (1 + e^(-x)) = 1 / (1 + e^x) = sigma(-x) $


==

$ sigma'(x) = dif / (dif x) sigma(x) = dif / (dif x) 1 / (1 + e^(-x)) = e^(-x) / (1 + e^(-x))^2 = 1 / (1 + e^(-x)) dot 1 / (1 + e^x) = sigma(x) (1 - sigma(x)) $

#figure(
    image("images/p2_b.png", width: 100%),
    caption: [绿色线为 $sigma(x)$ 的曲线, 橙色线为 $sigma'(x)$ 的曲线.]
) <sigma_figure>

==

第 $i$ 层网络可以表达为 $yvec^((i)) = sigma(zvec^((i))) = sigma(f(xvec^((i)), thetavec^((i))))$, 其中 $xvec^((i))$ 是第 $i$ 层的输入, 而 $zvec^((i)) = f(xvec^((i)), thetavec^((i)))$ 是第 $i$ 层网络激活函数 $sigma(dot.c)$ 前对输入的处理.

因此由链式法则有

$ (diff ell) / (diff ( thetavec^((i)) )^T) = (diff ell) / (diff ( yvec^((i)) )^T) (diff yvec^((i))) / (diff ( zvec^((i)) )^T) (diff zvec^((i))) / (diff ( thetavec^((i)) )^T) $

其中由于我们知道 $yvec^((i)) = sigma(zvec^((i)))$ 是一个逐元素操作, 因此有 $y_j^((i)) = sigma(z_j^((i)))$, 则我们分析 $(diff yvec^((i))) / (diff ( zvec^((i)) )^T)$ 的单个元素, 则有

$ [(diff yvec^((i))) / (diff ( zvec^((i)) )^T)]_j = sigma'(z_j^((i))) $

而由 @sigma_figure 我们又知道 $sigma'(z_j^((i)))$ 是最大值为 $0.25$ 的函数, 且在 $|z_j^((i))| -> oo$ 时 $sigma(z_j^((i))) -> 0$.

因此, 在乘上了 $sigma'(z_j^((i)))$ 的时候, 尤其是当 $i$ 由 $L$ 变为 $1
$ 时, 从 $i = L$ 开始到 $i = 1$ 乘上了多个 $sigma'(z_j^((i)))$, 得到的结果 $norm((diff ell) / (diff ((thetavec^((i))))^T))$ 就越趋近于 $0$, 即梯度消失困难.


= 习题三

// 已知随机变量 $X$ 密度函数 $q(x)$ 满足当 $x >= 0$ 时 $q(x) > 0$; 当 $x < 0$ 时 $q(x) = 0$. 以及 $X$ 的均值为 $mu > 0$.

// 我们要求在这样约束条件下的最大熵分布, 即有优化问题:

// $
// max & h(x) = - integral_0^oo q(x) ln(q(x)) dif x  \
// "s.t." & integral_0^oo q(x) dif x = 1  \
// & integral_0^oo x q(x) = mu
// $

// 使用拉格朗日乘子法, 有拉格朗日函数

// $
// J & = - integral_0^oo q(x) ln(q(x)) dif x + lambda_1 (integral_0^oo q(x) dif x - 1) + lambda_2 (integral_0^oo x q(x) - mu)  \
// & = integral_0^oo (- ln(q(x)) + lambda_1 + lambda_2 x) q(x) dif x - (lambda_1 + lambda_2 mu)  \
// $

// 令其对 $x$ 求偏导并等于零即有

// $ (diff J) / (diff x) = (- ln(q(x)) + lambda_1 + lambda_2 x) q(x) = 0 $

// 因为有 $x >= 0, q(x) > 0$, 因此我们可知

// $ - ln(q(x)) + lambda_1 + lambda_2 x = 0 $

// 解得

// $ q(x) = e^(lambda_1 + lambda_2 x) $

// 我们带回约束条件 1 和约束条件 2 即有

// $ integral_0^oo e^(lambda_1 + lambda_2 x) dif x = evalat( e^(lambda_1 + lambda_2 x) / lambda_2 )_0^oo = - e^(lambda_1) / lambda_2 = 1 $

// $ integral_0^oo x e^(lambda_1 + lambda_2 x) dif x = evalat( ((lambda_2 x - 1) e^(lambda_1 + lambda_2 x)) / lambda_2^2 )_0^oo = e^(lambda_1) / lambda_2^2 = mu $

// 其中 $lambda_2 < 0$.

// 解上述两式即可得 $e^(lambda_1) = 1 / mu, lambda_2 = - 1 / mu$

// 因此最终可得

// $ q(x) = 1/mu e^(- 1/mu x) = lambda e^(- lambda x) $

// 即参数为 $lambda = 1/mu$ 的指数分布是在这样约束条件的最大熵分布.

假设有随机变量 $Y$ 满足分布 $p(x)$, 且分布 $p(x)$ 时满足题目条件的分布, 即有 $x >= 0$ 时 $p(x) > 0$; 当 $x < 0$ 时 $p(x) = 0$. 以及 $Y$ 的均值为 $E[Y] = integral_0^oo x p(x) = mu > 0$.

由于 $X$ 是参数为 $lambda = 1/mu$ 的指数分布, 即有

$
q(x) = cases(lambda e^(-lambda x) when x >= 0, 0 when x < 0)
$

#let KL = math.op("KL")

由不等式 $KL(p || q) >= 0$ 可知

$
0 & <= KL(p || q)  \
& = integral p(x) ln p(x) / q(x) dif x  \
& = integral p(x) ln p(x) dif x - integral p(x) ln q(x) dif x  \
& = -h(Y) - integral p(x) ln q(x) dif x  \
& = -h(Y) - integral_0^oo p(x) ln lambda e^(-lambda x) dif x  \
& = -h(Y) - ln lambda integral_0^oo p(x) dif x + lambda integral_0^oo x p(x) dif x  \
& = -h(Y) - ln lambda + lambda mu  \
& = -h(Y) - ln lambda integral_0^oo q(x) dif x + lambda integral_0^oo x q(x) dif x  \
& = -h(Y) - integral_0^oo q(x) ln lambda e^(-lambda x) dif x  \
& = -h(Y) - integral q(x) ln q(x) dif x  \
& = -h(Y) + h(X)  \
$

即有

$ h(X) >= h(Y) $

即参数为 $lambda = 1/mu$ 的指数分布是在这样约束条件的最大熵分布.


= 习题四

我们先将收缩阈值操作符 (标量情况下) 化为可读性更好的形式, 其中 $lambda > 0$:

$ cal(T)_lambda(x) = sign(x)(|x| - lambda)_+ = cases(x + lambda when x < -lambda, 0 when -lambda <= x <= lambda, x - lambda when x > lambda) $

为了在 $lambda > 0$ 的条件下求解优化问题

$ argmin_xvec norm(xvec - yvec)^2 + lambda norm(xvec)_1 $

我们令 $F(xvec) = norm(xvec - yvec)^2 + lambda norm(xvec)_1$, 则由范数的定义可知

$ F(xvec) = ((x_1 - y_1)^2 + lambda |x_1|) + dots.c + ((x_n - y_1)^2 + lambda |x_n|) $

我们又令 $f_i(x_i) = (x_i - y_i)^2 + lambda |x_i|, i = 1, 2, ..., n$, 由 $f_i(x_i)$ 之间的独立性可知, 只要我们分别求解

$ argmin_(x_i) f_i(x_i) = (x_i - y_i)^2 + lambda |x_i| $

即可得原优化问题的解.

对函数 $f(x) = (x - y)^2 + lambda |x|$ 求导可得

$ f'(x) = 2 (x - y) + lambda sign(x), x != 0 $

令导数等于零可得

$ x = y - lambda/2 sign(x), x != 0 $

下面我们进行分类讨论:

当 $y < -lambda/2$ 时,

假设 $x < 0$ 则有 $x = y - lambda/2 sign(x) = y + lambda/2 < 0$ 假设成立.

假设 $x > 0$ 则有 $x = y - lambda/2 sign(x) = y - lambda/2 < -lambda < 0$ 假设不成立.

因此有 $x = y + lambda/2$ 与 $x = 0$ 这两种可能取值, 我们带入 $f(x) = (x - y)^2 + lambda |x|$ 有

$ f(0) - f(y + lambda/2) = y^2 - [(lambda/2)^2 - lambda(y + lambda/2)] = (y + lambda/2)^2 > 0 $

即有 $f(y + lambda/2) < f(0)$,

因此此时 $x = y + lambda/2$.

当 $y > lambda/2$ 时,

假设 $x < 0$ 则有 $x = y - lambda/2 sign(x) = y + lambda/2 > lambda > 0$ 假设不成立.

假设 $x > 0$ 则有 $x = y - lambda/2 sign(x) = y - lambda/2 > 0$ 假设成立.

因此有 $x = y - lambda/2$ 与 $x = 0$ 这两种可能取值, 我们带入 $f(x) = (x - y)^2 + lambda |x|$ 有

$ f(0) - f(y - lambda/2) = y^2 - [(lambda/2)^2 + lambda(y - lambda/2)] = (y - lambda/2)^2 > 0 $

即有 $f(y - lambda/2) < f(0)$,

因此此时 $x = y - lambda/2$.

当 $-lambda/2 <= y <= lambda/2$ 时,

假设 $x < 0$ 则有 $x = y - lambda/2 sign(x) = y + lambda/2 >= 0$ 假设不成立.

假设 $x > 0$ 则有 $x = y - lambda/2 sign(x) = y - lambda/2 <= 0$ 假设不成立.

我们只需证明 $f(Delta x) > f(0)$ 对于 $Delta x != 0$ 时成立即可. 由于

$ f(Delta x) = (Delta x - y)^2 + lambda |Delta x| = (Delta x)^2 - 2 Delta x y + lambda |Delta x| + f(0) $

当 $Delta x > 0$ 时利用 $y <= lambda/2$ 有

$
f(Delta x) & = (Delta x)^2 - 2 Delta x y + lambda |Delta x| + f(0)  \
& >= (Delta x)^2 - 2 Delta x lambda/2 + lambda |Delta x| + f(0)  \
& = (Delta x)^2 + f(0)  \
& > 0
$

当 $Delta x < 0$ 时利用 $y <= lambda/2$ 有

$
f(Delta x) & = (Delta x)^2 - 2 Delta x y + lambda |Delta x| + f(0)  \
& >= (Delta x)^2 - 2 Delta x lambda/2 + lambda |Delta x| + f(0)  \
& = (Delta x)^2 + 2 lambda|Delta x|+ f(0)  \
& > 0
$

因此此时 $x = 0$ 可得极小值.

综上可得

$ x^* = cases(y + lambda/2 when y < -lambda/2, 0 when -lambda/2 <= y <= lambda/2, y - lambda/2 when y > lambda/2) $

即有

$ x^* = sign(y)(|y| - lambda/2)_+ = cal(T)_(lambda/2) (y) $


#pagebreak()


= 习题五

==

由于情形 1.1 可以得 $p(A, C) = p(A)p(C|A)$ 与 $p(A, B, C) = p(A)p(C|A)p(B|C)$, 因此有

$ p(A, B|C) = p(A, B, C) / p(C) = (p(A)p(C|A)p(B|C)) / p(C) $

$ p(A|C)p(B|C) = p(A, C) / p(C) p(B|C) = (p(A)p(C|A)p(B|C)) / p(C) $

因此两条等式相等, 即 $p(A, B|C) = p(A|C)p(B|C)$, 说明有

$ A perp B | C $


==

由于情形 1.2 可以得 $p(B, C) = p(B)p(C|B)$ 与 $p(A, B, C) = p(B)p(C|B)p(A|C)$, 因此有

$ p(A, B|C) = p(A, B, C) / p(C) = (p(B)p(C|B)p(A|C)) / p(C) $

$ p(A|C)p(B|C) = p(B, C) / p(C) p(A|C) = (p(B)p(C|B)p(A|C)) / p(C) $

因此两条等式相等, 即 $p(A, B|C) = p(A|C)p(B|C)$, 说明有

$ A perp B | C $


==

由于情形 2 可以得 $p(A, B, C) = p(C)p(A|C)p(B|C)$, 因此有

$ p(A, B|C) = p(A, B, C) / p(C) = (p(C)p(A|C)p(B|C)) / p(C) = p(A|C)p(B|C) $

即有

$ A perp B | C $


==

由于情形 2 可以得 $p(A, B, C) = p(C|A, B)p(A)p(B)$.

当 $C$ 没有被观测到时有

$
p(A, B) & = sum_C p(A, B, C)  \
& = sum_C p(C|A, B)p(A)p(B)  \
& = p(A)p(B)  \
$

即 $A$ 和 $B$ 独立.

#let xor = math.plus.circle

我们可以找到一些简单的例子, 例如令 $A$ 和 $B$ 独立地遵循 $p = 0.5$ 的伯努利分布, 而令 $C = A xor B$, 即 $C$ 为 $A$ 与 $B$ 的异或.

在没有观测到 $C$ 时, $A$ 和 $B$ 是独立的, 均遵循 $p = 0.5$ 的伯努利分布, 可以看作随机抛两次硬币分别决定 $A$ 和 $B$ 的值.

当给定 $C = 0$ 时, 一定有 $A = B$; 当给定 $C = 1$ 时, 一定有 $A != B$, 这时候可以看出, $A$ 和 $B$ 不再是独立的了.


==

在我们给定 $F$ 的情况下, 由于 $F$ 是 $C$ 的后代, 不独立, 一般则有  $p(F|C) != p(F)$.

因此由贝叶斯公式可得

$ p(C|F) = p(C, F) / p(F) = (p(C)p(F|C)) / p(F) = p(C) p(F|C) / p(F) != p(C) $

即给定 $F$ 的情况下 $C$ 的取值会受到影响, 再由上一问的结果则可知 $A$ 和 $B$ 不再是独立的, 而是存在依赖关系.