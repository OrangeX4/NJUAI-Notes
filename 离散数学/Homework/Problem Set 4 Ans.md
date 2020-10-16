# Problem Set 4

# Problem 1
$$
\begin{aligned}
&1. \forall x(P(x)\land R(x))   &(前提引入) \\
&2. P(c) \land R(c), 任意c   &(全称实例, 由1.) \\
&3. P(c), 任意c  &(化简, 由2.) \\
&4. \forall x(P(x) \to (Q(x) \land S(x)))   &(前提引入) \\
&5. Q(c)\land S(c), 任意c   &(全称假言推理, 由3.4.) \\
&6. S(c), 任意c  &(化简, 由5.) \\
&7. R(c), 任意c  &(化简, 由2.) \\
&8. R(c)\land S(c), 任意c  &(合取, 由6.7.) \\
&9. \forall x(R(x) \land S(x))  &(全称引入, 由8.) \\
\end{aligned}
$$


# Problem 2

$$
\begin{aligned}
&1. \exist x\lnot P(x)  &(前提引入) \\
&2. \lnot P(c)  &(存在实例, 由1.)  \\
&3. \forall x(P(x) \lor Q(x))  &(前提引入)  \\
&4. P(c)\lor Q(c)  &(全称实例, 由3.)  \\
&5. \forall x(\lnot Q(x) \lor S(x))  &(前提引入)  \\
&6. \lnot Q(c) \lor S(c)  &(全称实例, 由5.)  \\
&7. P(c) \lor S(x)  &(消解律, 由4.6.) \\
&8. S(c)  &(析取三段论, 由2.7.) \\
&9. \forall x(R(x) \to \lnot S(x))  &(前提引入)  \\
1&0. \lnot R(c)  &(全称取拒式, 由8.9.) \\
1&1. \exist x\lnot R(x)  &(存在引入, 由10.)  \\
\end{aligned}
$$


# Problem 3

$该定理的表述为\forall x \forall y(P(x, y) \to Q(x, y))$
$其中P(x, y): x, y是实数, Q(x): |x| + |y| \geq |x+y|$

### 使用直接证明法:

$当x, y同号或x,y其中一个为0时:$
$|x + y| = |x| + |y| \leq |x| + |y|$ 

$当x, y异号时:$
$|x + y| = ||x| - |y|| \leq |x| + |y|$

$综上|x| + |y| \geq |x+y|$成立.

$所以\forall x \forall y(P(x, y) \to Q(x, y))为真.$


# Problem 4

## a)

$P(x): x$是乌鸦.

$Q(x): x$是北京鸭.

$R(x): x$是白色的.

### 原题转化为:

如果$\forall x(P(x) \to \lnot R(x))$和$\forall x(Q(x) \to R(x))$为真, 则$\forall x(Q(x) \to \lnot P(x))$为真.

### 证明

$$
\begin{aligned}
&1.\forall x(P(x) \to \lnot R(x))  &(前提引入) \\
&2.\forall x(\lnot P(x) \lor \lnot R(x))  &(德摩根律, 由1.) \\
&3.\lnot P(c) \lor \lnot R(c), 任意c  &(全称实例, 由3.)  \\
&4.\forall x(Q(x) \to R(x))  &(前提引入)  \\
&5.\forall x(\lnot Q(x) \lor R(x))  &(德摩根律, 由3.) \\
&6.\lnot Q(c) \lor R(c), 任意c  &(全称实例, 由5.) \\
&7.\lnot P(c) \lor \lnot Q(c), 任意c  &(消解, 由5.6.) \\
&8.Q(x) \to \lnot P(c), 任意c  &(德摩根律, 由7.)  \\
&9.\forall x(Q(x) \to \lnot P(x))  &(全称引入, 由8.)
\end{aligned}
$$

## b)

论域为人.

$P(x): x$喜欢步行.

$Q(x): x$喜欢乘汽车.

$R(x): x$喜欢骑自行车.

### 原题转化为:

如果$\forall x(P(x) \to \lnot Q(x))$, $\forall x(Q(x) \lor R(x))$和$\exist x\lnot R(x)$为真, 则$\exist x\lnot P(x)$为真.

### 证明:

$$
\begin{aligned}
&1.\exist x\lnot R(x)  &(前提引入) \\
&2.\lnot R(c)  &(存在实例, 由1.)  \\
&3.\forall x(Q(x) \lor R(x))  &(前提引入)  \\
&4.Q(c) \lor R(c)  &(全称实例, 由3.)  \\
&5.Q(c)  &(析取三段论, 由2.4.) \\
&6.\forall x(P(x) \to \lnot Q(x)) &(前提引入) \\
&7.P(c) \to \lnot Q(c)  &(全称实例)  \\
&8.\lnot P(c)  &(取拒式, 由5.7.)  \\
&9.\exist x\lnot P(x)  &(存在引入, 由8.) \\
\end{aligned}
$$


# Problem 5

### 猜想:

$\forall x \forall y(R(x) \land R(y) \to \displaystyle\sqrt{\frac{x^2 + y^2}2} \geq \frac{x+y}{2}), 其中R(x): x是实数.$

### 证明:

使用直接证明法.

假设$x, y$都是实数.

$当\displaystyle\frac{x+y}{2} > 0时候$

$\because (x-y)^2=x^2+y^2-2xy \geq 0$

$\therefore x^2+y^2 \geq 2xy$

$\therefore 2x^2 + 2y^2 \geq x^2 + 2xy + y^2$

$\displaystyle\therefore \frac{x^2 + y^2}{2} \geq \frac{x^2 + 2xy + y^2}{4}$

$\displaystyle\therefore \sqrt{\frac{x^2 + y^2}2} \geq \frac{x+y}{2}$

$当\displaystyle\frac{x+y}{2} \leq 0时候$

$\displaystyle\therefore \sqrt{\frac{x^2 + y^2}2} \geq 0 \geq \frac{x+y}{2}$

综上原式总是成立.

$\forall x \forall y(R(x) \land R(y) \to \displaystyle\sqrt{\frac{x^2 + y^2}2} \geq \frac{x+y}{2})$成立.


# Problem 6

$原式可转化为:$
$P(x) \to Q(x), P(x): x是整数, Q(x): x的四次方的最后一位必然是0,1,5,6中的一个.$

### 证明:

使用直接证明法:

$假设x是整数, 不妨令x=10a+b, 其中b为一位整数, a为整数.$

$$
\begin{aligned}
\therefore x^4 &= (10a+b)^4 \\
&= (10a)^4 + 4(10a)^3b + 6(10a)^2b^2 + 4(10a)b^3 + b^4 \\
&= 10(1000a^4 + 400a^3b + 60a^2b^2 + 4ab^3) + b^4 \\
\end{aligned}
$$

$易得b^4的个位数就是x^4的个位数.$

$b^4=0 或 1 或 16 或 81 或 256 或 625 或 1296 或 2401 或 4096 或 6561$

$可看出x的四次方的最后一位必然是0,1,5,6中的一个.$

$P(x) \to Q(x)成立.$


# Problem 7

原式可转化为:
$\forall a \forall b (P(x) \land Q(x) \to \exist c(a < c < b))$