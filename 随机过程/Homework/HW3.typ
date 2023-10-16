#import "../../Typst/report-template.typ": *
#import "../../Typst/typst-sympy-calculator.typ": *

#set heading(numbering: Numbering.with(base: 2, "(a)"))

// apply the template
#show: report.with(
    size: 10pt,
    subject: "随机过程", 
    title: "HW3",
    date: "2023 年春季",
    author: "201300035 方盛俊 人工智能学院",
    par-indent: false
)

#show math.equation.where(block: true): it => math.display(it)
#show math.equation.where(block: false): set text(1.1em)

#set page(margin: (x: 2em))
#set text(15pt)

= Problem 1

There is that $i$ is null recurrent and $i <-> j$, now we prove that $j$ is null recurrent.

$ i <-> j => d(i) = d(j) = d >= 1 $

$ pi_i = lim_(n -> oo) P_(i i)^(n d) = d / mu_(i i) = 0 $

$ i <-> j => exists s, t >= 0, P_(i j)^s > 0, P_(j i)^t > 0 $

$ P_(i i)^(t + s) >= P_(j i)^t P_(i j)^s > 0 => d "divides" t + s $

$ pi_i = lim_(m -> oo) P_(i i)^(t + s + m d) = 0 $

$ P_(i i)^(t + s + m d) >= P_(i j)^s P_(j j)^(m d) P_(j i)^t $

$ 0 = lim_(m -> oo) P_(i i)^(t + s + m d) >= P_(i j)^s P_(j i)^t dot lim_(m -> oo) P_(j j)^(m d) $

because $ P_(i j)^s > 0, P_(j i)^t > 0 $ we have

$ pi_j = lim_(m -> oo) P_(j j)^(m d) = 0 $

So $j$ is null recurrent.



= Problem 2

We know $ P_(00) = P_(N N) = 1, P_(i, i+1) = p = 1 - P_(i, i-1), N = 6 $

So we have

#let p = 0.4

$ Q = mat(0, p, 0, 0, 0; 1-p, 0, p, 0, 0; 0, 1-p, 0, p, 0; 0, 0, 1-p, 0, p; 0, 0, 0, 1-p, 0) = mat(0, 0.4, 0, 0, 0; 0.6, 0, 0.4, 0, 0; 0, 0.6, 0, 0.4, 0; 0, 0, 0.6, 0, 0.4; 0, 0, 0, 0.6, 0) $

Because $ M = I + Q M $, we know

$ M = (I - Q)^(-1) = mat(1, -0.4, 0, 0, 0; -0.6, 1, -0.4, 0, 0; 0, -0.6, 1, -0.4, 0; 0, 0, -0.6, 1, -0.4; 0, 0, 0, -0.6, 1)^(-1) = mat(211/133, 130/133, 4/7, 40/133, 16/133; 195/133, 325/133, 10/7, 100/133, 40/133; 9/7, 15/7, 19/7, 10/7, 4/7; 135/133, 225/133, 15/7, 325/133, 130/133; 81/133, 135/133, 9/7, 195/133, 211/133) $

So we can get

$ m_(3, 3) = 19/7, m_(3, 2) = 15/7, f_(3, 4) = m_(3, 4) / m_(4, 4) = (10/7) / (325/133) = 38/65 $



= Problem 3

Define the generating function $ phi.alt(s) = sum_(j=0)^oo s^j P_j $

Since $ P_0 + P_1 < 1 $, We can get

$ phi.alt'(s) = sum_(j = 0)^oo j s^(j - 1) P_j $

$ phi.alt prime.double(s) = sum_(j = 0)^oo j (j - 1) s^(j - 2) P_j > 0 $

for all $ s in (0, 1) $, hence $ phi.alt(s) $ is a strictly convex function in $ (0, 1) $.

We define $ psi(s) = phi.alt(s) - s $

Hence we have

$ psi(0) = phi.alt(0) - 0 = P_0 $

$ psi(1) = phi.alt(1) - 1 = 1 - 1 = 0 $

$ psi'(s) = phi.alt'(s) - 1 $

$ psi'(0) = phi.alt'(0) - 1 = P_1 - 1 $

and $ psi'(s) $ is a monotonically increasing function.

When $ phi.alt'(1) <= 1 $, we get

$ psi'(s) <= psi'(1) = phi.alt'(1) - 1 <= 0 $

So $ psi(s) $ is a monotonically decreasing function and

$ psi(s) = phi.alt(s) - s >= psi(1) = 0 $

$ phi.alt(s) >= s $

When $ phi.alt'(1) > 1 $, we get

$ psi'(0) = phi.alt'(0) - 1 = P_1 - 1 < 0 $

$ psi'(1) = phi.alt'(1) - 1 > 0 $

Hence there is $ s_1 in (0, 1) $ where $ psi'(s_1) = 0, psi(s_1) < psi(1) = 0 $,

and there is $ s_2 in (0, s_1) $ where $ psi(s_2) = 0 $.

So $pi_0 = s_2 < 1$ in this case.

Thus, since $ phi.alt(pi_0) = pi_0, pi_0 = 1 $ if, and only if, $ phi.alt'(1) <= 1 $

The result follows, since $ phi.alt'(1) = sum_(j)^oo j P_j = mu $



= Problem 4

because $ pi_i P_(i j) = pi_j P_(j i)^* $

$ sum_j pi_j P_(j i)^* = sum_j pi_i P_(i j) = pi_i sum_j P_(i j) = pi_i $

So $ pi_i, i >= 0 $ are also the stationary probabilities of the reverse chain.




= Problem 5

$
& P(X_k = i_k | X_j = i_j, forall j != k)  \
= & P(X_k = i_k, X_j = i_j, forall j != k) / P(X_j = i_j, forall j != k)  \
= & (P(X_j = i_j, forall j >= k | X_j = i_j, forall j < k) P(X_j = i_j, forall j < k)) / (P(X_j = i_j, forall j > k | X_j = i_j, forall j < k) P(X_j = i_j, forall j < k))  \
= & (P(X_j = i_j, forall j >= k | X_(k-1) = i_(k-1)) P(X_j = i_j, forall j < k)) / (P(X_j = i_j, forall j > k | X_(k-1) = i_(k-1)) P(X_j = i_j, forall j < k))  \
= & P(X_j = i_j, forall j >= k | X_(k-1) = i_(k-1)) / P(X_j = i_j, forall j > k | X_(k-1) = i_(k-1))  \
= & (P(X_k = i_k | X_(k-1) = i_(k-1), X_j = i_j, forall j > k) P(X_j = i_j, forall j > k | X_(k-1) = i_(k-1))) / (P(X_j = i_j, forall j > k | X_(k-1) = i_(k-1)))  \
= & P(X_k = i_k | X_(k-1) = i_(k-1), X_j = i_j, forall j > k)  \
= & (P(X_k = i_k, X_(k-1) = i_(k-1), X_j = i_j, forall j > k)) / P(X_(k-1) = i_(k-1), X_j = i_j, forall j > k)  \
= & (P(X_j = i_j, forall j > k + 1 | X_k = i_k, X_(k-1) = i_(k-1), X_(k+1) = i_(k+1)) P(X_k = i_k, X_(k-1) = i_(k-1), X_(k+1) = i_(k+1))) / (P(X_j = i_j, forall j > k + 1 | X_(k-1) = i_(k-1), X_(k+1) = i_(k+1)) P(X_(k-1) = i_(k-1), X_(k+1) = i_(k+1)))  \
= & (P(X_j = i_j, forall j > k + 1 | X_(k+1) = i_(k+1)) P(X_k = i_k, X_(k-1) = i_(k-1), X_(k+1) = i_(k+1))) / (P(X_j = i_j, forall j > k + 1 | X_(k+1) = i_(k+1)) P(X_(k-1) = i_(k-1), X_(k+1) = i_(k+1)))  \
= & P(X_k = i_k, X_(k-1) = i_(k-1), X_(k+1) = i_(k+1)) / P(X_(k-1) = i_(k-1), X_(k+1) = i_(k+1))  \
= & P(X_k = i_k | X_(k-1) = i_(k-1), X_(k+1) = i_(k+1)))  \
$

