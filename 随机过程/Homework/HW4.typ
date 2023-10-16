#import "../../Typst/report-template.typ": *
#import "../../Typst/typst-sympy-calculator.typ": *
#import "../../Typst/tablex.typ": *
#import "../../Typst/typst-canvas/canvas.typ": canvas

#set heading(numbering: Numbering.with(base: 2, "(a)"))
#show math.equation.where(block: true): it => math.display(it)

// apply the template
#show: report.with(
    size: 12pt,
    subject: "随机过程", 
    title: "HW4",
    date: "2023 年春季",
    author: "201300035 方盛俊 人工智能学院",
    par-indent: false
)


= Problem 1

设 $Y$ 为 branching process 1 中每个体繁衍出的子代数目,

因此有 $X_(n+1) = sum_(i=1)^(X_n) Y_i$ 以及 $E[Y] = m$, 则

$
& E[Z_(n+1) | Z_1, Z_2, ..., Z_n]  \
= & E[X_(n+1) / m^(n+1) | Z_1, Z_2, ..., Z_n]  \
= & E[(sum_(i=1)^(X_n) Y_i) / m^(n+1) | Z_1, Z_2, ..., Z_n]  \
= & X_n / m^(n+1)E[Y]  \
= & X_n / m^n = Z_n
$

因此 ${Z_n, n >= 1}$ 是一个 martingale.


= Problem 2

我们使用 $ x = a / p $ 计算得到一个公平的博弈模型:

#gridx(
    columns: 6,
    align: center,
    column-gutter: 1em,
    [H], [H], [T], [T], [H], [H],
    colspanx(6)[
        #block(height: 1em, width: 100%)[
            #let length = 100% + 1.2em
            #let mark-size = 0.3em
            #line(start: (0%, mark-size), end: (length, mark-size))
            #line(start: (length - mark-size, 0em), end: (length, mark-size))
            #line(start: (length - mark-size, 2 * mark-size), end: (length, mark-size))
        ]
    ],
    $ 1/p $, $ 1/p^2 $, $ 1/(p^2 q) $, $ 1/(p^2 q^2) $, $ 1/(p^3 q^2) $, $ 1/(p^4 q^2) $
)

可见每个赌徒在每个时刻的期望获利为 $0$.

令 $X_n$ 为赌场在 $n$ 天后的获利, 则 ${X_n, n >= 1}$ 是一个 martingale.

设首次出现 HHTTHH 的时间为 $N$, 则有

#gridx(
    columns: 7,
    align: center,
    column-gutter: 1em,
    [......], [H], [H], [T], [T], [H], [H],
    colspanx(7)[
        #block(height: 1em, width: 100%)[
            #let length = 100% + 1.2em
            #let mark-size = 0.3em
            #line(start: (0%, mark-size), end: (length, mark-size))
            #line(start: (length - mark-size, 0em), end: (length, mark-size))
            #line(start: (length - mark-size, 2 * mark-size), end: (length, mark-size))
        ]
    ],
    [......], $ N - 5 $, $ N - 4 $, $ N - 3 $, $ N - 2 $, $ N - 1 $, $ N $,
)

因此可以计算得到

$
X_n & = N - 6 - (1/(p^4 q^2) - 1) + 1 + 1 + 1 - (1/p^2 - 1) - (1/p - 1)  \
& = N - 1/(p^4 q^2) - 1/p^2 - 1/p
$

使用 martingale stopping theorem 可得

$ E[X_n] = E[X_1] = 0 $

而又有 

$ E[X_n] = E[N - 1/(p^4 q^2) - 1/p^2 - 1/p] = E[N] - 1/(p^4 q^2) - 1/p^2 - 1/p $

因此可得

$ E[N] = 1/(p^4 q^2) + 1/p^2 + 1/p $



= Problem 3

由于 $X$ 为可以进行的试验数目, 而第 $i$ 个试验可以进行的的概率为 $product_(i in A_j) p_i$, 则有

$ mu = E[X] = sum_(j = 1)^(m) product_(i in A_j) p_i $

由于 $X$ 只与 $X_i$ 有关, 我们可以令 $X = h(X_1, ..., X_n)$

我们设向量 $x = (x_1, ..., x_n)$ 与 $y = (y_1, ..., y_n)$ 仅有一处不同, 可以设为 $x_k != y_k$, 而其余相同.

我们不妨令 $x_k = 0, y_k = 1$, 反过来同理.

由于第 $k$ 个部件最多只会被 $3$ 个试验使用, 因此我们有 $h(y) <= h(x) + 3$, 则可得

$ |h(x) - h(y)| <= 3 $

两边除以 $3$ 即有

$ |h(x) / 3 - h(y) / 3| <= 1 $

我们应用 Azuma 不等式的引理可得

$ P(X - sum_(j = 1)^(m) product_(i in A_j) p_i >= 3a) <= exp{-a^2/(2n)} $

以及

$ P(X - sum_(j = 1)^(m) product_(i in A_j) p_i <= -3a) <= exp{-a^2/(2n)} $


#pagebreak(weak: true)


= Problem 4

令 $ S_n = X_1 + dots.c + X_n, psi(t) = E[e^(-t X)], g(t) = e^(-t (mu - epsilon.alt)) / psi(t) $

则 $g(0) = 1$ 且 $ g'(0) = (-(mu - epsilon.alt)e^(-t(mu - epsilon.alt)) psi(t) - psi'(t)e^(-t(mu - epsilon.alt))) / (psi^2 (t)) bar_(t = 0) = -(mu - epsilon.alt) - (-mu) = epsilon.alt > 0 $

可得存在 $t_0 > 0$ 使得 $g(t_0) > 1$

假设 $ S_n / n <= mu - epsilon.alt $ 也即 $ -S_n >= - n (mu - epsilon.alt) $, 则有

$ e^(-t_0 S_n) / (psi^n (t_0)) >= e^(-t_0 n (mu - epsilon.alt)) / (psi^n (t_0)) = (e^(-t_0 (mu - epsilon.alt)) / psi(t_0))^n = g^(n)(t_0) $

而由 $g(t_0) > 1$ 则有 $ lim_(n -> oo) g^n (t_0) -> oo $

而我们知道由于 $ E[e^(-t_0 X_i) / psi(t_0)] = 1 $ 可得

$ e^(-t_0 S_n) / (psi^n (t_0)) = (product_(i = 1)^(n) e^(-t_0 X_i)) / (psi^(n)(t_0)) = product_(i = 1)^(n) e^(-t_0 X_i) / psi(t_0) $

是一个 martingale, 这是因为对于任意 $E[Y_i] = 1$ 与 $Z_n = product_(i = 1)^(n) Y_i$ 有

$ E[Z_(n+1) | Z_1, Z_2, ..., Z_n] = Z_n dot E[X_(n+1) | Z_1, Z_2, ..., Z_n] = Z_n dot E[X_(n+1)] = Z_n $

因此由 martingale 收敛定理可知以概率 $1$ 有 $ lim_(n -> oo) e^(-t_0 S_n) / (psi^n (t_0)) $ 存在且有限.

因此由上述结论可以推出 $ P(lim_(n -> oo) S_n / n <= mu - epsilon.alt) = 0 $
