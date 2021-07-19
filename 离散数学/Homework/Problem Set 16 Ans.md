# Problem Set 16

# Problem 1

(a) $是格$

(b) $不是格, \{d,e\}的上界为c和f, 而c和f不可比, \{d,e\}没有上确界$

(c) $是格$

(d) $不是格, \{b, c\}的上界有d和e, 而d和e不可比, \{d,e\}没有上确界$

(e) $不是格, a,b不可比, 没有下界, 也没有下确界$

(f) $是格$


# Problem 2

(1) $不是格$

(2) $是格$

(3) $是格$

(4) $是格$


# Problem 3

(1) $a\lor(a\land b)\succeq a$

(2) $a\land(b\lor c)\succeq (a\land b)\lor(a\land c)$

(3) $b\land(c\lor a)\succeq (b\land c)\lor a$


# Problem 4

$\because a\preceq b\preceq c$

$\therefore a\lor b=b, b\land c=b$

$\therefore a\lor b=b\land c$


# Problem 5

$对于\forall a\in L, 假设b, c都是a的补元$

$\therefore a\lor c=1, a\land c=0, a\lor b=1,a\land b=0$

$\because 全上界和全下界唯一$

$\therefore a\lor c=a\lor b, a\land c=a\land b$

$\because L是分配格$

$
\begin{aligned}
\therefore
b&=b\lor(a\land b) \\
&=b\lor(a\land c) \\
&=(b\lor a)\land(b\lor c) \\
&=(a\lor c)\land(b\lor c) \\
&=(a\land b)\lor c \\
&=(a\land c)\lor c \\
&=c
\end{aligned}
$

$\therefore 有补分配格中任何元素都是唯一的$


# Problem 6

$对于\forall x,y\in S, 即有x,y\in L, x\preceq a且y\preceq a$

$设z为\{x,y\}的上确界, 即z=x\lor y, z\in L$

$\because x\preceq a且y\preceq a$

$\therefore a是x和y的一个上界$

$\therefore z\preceq a$

$\therefore z\in S$

$\therefore S对于\lor是封闭的$

$设r为\{x,y\}的下确界, 即r=x\land y, z\in L$

$\therefore r\preceq x$

$\because x\preceq a$

$\therefore r\preceq x \preceq a, 即r\in S$

$\therefore S对于\land也是封闭的$

$\therefore \langle S, \preceq, \lor, \land\rangle是一个代数系统$

$\because 易知S\subseteq L$

$\therefore S依然满足L所拥有的交换律, 结合律, 吸收律$

$\therefore \langle S, \preceq, \lor, \land\rangle是L的子格$


# Problem 7

(a) $a的补元是d$

(c) $a的补元是f, b的补元是d, c的补元是e$

(f) $a的补元是f, b的补元是e$


# Problem 8

## (a)

$是分配格, 不是有补格, 不是布尔格$

$线构型, 无与M_3或N_5重构的子格, 因此是分配格$

$b和c无补元, 不是有补格, 因而也不是布尔格$

## (c)

$不是分配格, 是有补格, 不是布尔格$

$\{a,b,c,d,f\}是与N_5重构的子格, 因此不是分配格, 也不是布尔格$

$每个元素都有补元, 因而是有补格$

## (f)

$不是分配格, 不是有补格, 不是布尔格$

$\{a,b,c,e,f\}是与N_5重构的子格, 因此不是分配格$

$c和d无补元, 不是有补格, 因而也不是布尔格$


# Problem 9

$\because \forall a\in L, 0\preceq a$

$\therefore a\land 0=0\land a=0, a\lor 0=0\lor a=a$

$\because \forall a\in L, a\preceq 1$

$\therefore a\land 1=a, a\lor 1=1$
