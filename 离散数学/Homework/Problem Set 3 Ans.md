# Problem Set 3

# Problem 1

a) $!\exist x(C(x) \land D(x) \land F(x))$

b) $\forall x(C(x) \land D(x) \land F(x))$

c) $\exist x(C(x) \land F(x) \land \lnot D(x))$

d) $\forall x(\lnot C(x) \lor \lnot D(x) \lor \lnot F(x))$

e) $(\exist xC(x)) \land (\exist yD(y)) \land (\exist zF(z))$


# Problem 2

## a) 

$当 x=-1 的时候 (-1)^3=-1 成立, 所以\exist x(x^3)=-1 真值为 T.$

## b)

$当 x=\frac{1}{2} 的时候 (\frac{1}{2})^4 < (\frac{1}{2})^2 成立,$

$所以 \exist x(x^4<x^2) 真值为T.$

## c)

由于 $(-x)^2=x^2$ 对所有实数$x$均为T, 所以$\forall x((-x)^2=x^2)$ 为$T$.

## d)

当$x = 0$的时候, $2 \times 0 > 0$ 不成立, 即存在反例, 

所以$\forall x(2x>x)$真值为$F$.


# Problem 3

## a)

$P(x): x$遵守驾驶速度限制.

$x$论域是所有的司机.

所有的司机都遵守驾驶速度限制.

$\forall xP(x)$

## b)

有些瑞典电影并不严肃.

$P(x): x$是严肃的.

$x$论域是所有的瑞典电影.

$\exist x(\lnot P(x))$

## c)

有人能保守秘密.

$P(x): x$能保守秘密.

$x$论域是所有人.

$\exist xP(x)$

## d)

班上所有人都有良好的心态.

$P(x): x$有良好的心态.

$x$论域是班上所有人.

$\exist xP(x)$


# Problem 4

## a)

$P(x): x$可以访问电子邮箱.

$x$论域是所有用户.

$\forall xP(x)$

## b)

$P(x): x$可以访问系统邮箱.

$x$论域为组里的所有人.

$q:$ 文件系统被锁定.

$q \to \forall xP(x)$

## c)

$p:$ 防火墙处于诊断状态.

$q:$ 代理服务器处于诊断状态.

$p \leftrightarrow q$

## d)

$P(x): x$工作正常.

$x$论域为所有的路由器.

$q:$ 吞吐量在100~500kbps.

$r:$ 代理服务器不处于诊断模式.

$q \land r \to \exist xP(x)$


# Problem 5

a) 学生 Randy Goldberg 注册了课程 CS 252.

b) 有学生注册了课程 Math 695.

c) 学生 Carol Sitca 注册了学校中的一些课程.

d) 有学生同时注册了课程 Math 222 和 CS252.

e) 有学生注册了另一个学生注册的所有课程.

f) 有两个学生注册的课程一模一样.


# Problem 6

$P(x): x$是三年级学生.

$Q(x): x$是计算机科学专业的.

$R(x): x$是数学专业的.

$S(x): x$是二年级学生.

## a)

$\exist xP(x)$

真值为 $T$

## b)

$\forall xQ(x)$

真值为 $F$

## c)

$\exist x(\lnot R(x) \land \lnot P(x))$

真值为 $T$

## d)

$\forall x(S(x) \lor Q(x))$


# Problem 7

论域为所有实数.

$\forall a \forall b \forall c \exist x_1 \exist x_2 \forall x(a \neq 0 \land ax^2+bx+c=0 \to x=x_1 \lor x=x_2)$