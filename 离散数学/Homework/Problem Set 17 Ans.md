# Problem Set 17

# Problem 1

(1) $b\land(a\lor c)$

(2) $b\lor(a\land c)$


# Problem 2

$对于a\preceq b \Rightarrow a\land b'=0:$

$\because a\preceq b$

$\therefore a\land b=a$

$\therefore a\land b'=a\land b\land b'=a\land 0=0$

$对于a\land b'=0 \Rightarrow a'\lor b=1:$

$由对偶式可知a\preceq b\Leftrightarrow a'\lor b=1$

$对于a'\lor b=1\Rightarrow a\preceq b:$

$\because a'\lor b=1=a'\lor a\lor b$

$\therefore b=a\lor b 或 a\lor b\preceq a'且a\preceq a'(舍去)$

$\therefore a\preceq b$

# Problem 3

$易见x\oplus y对B封闭$

$\therefore \langle B,\oplus\rangle 构成代数系统$

$$
\begin{aligned}
\because (x\oplus y)\oplus z
&=([(x\land y')\lor(x'\land y)]\land z')\lor([(x\land y')\lor(x'\land y)]'\land z) \\
&=(x\land y'\land z')\lor(x'\land y\land z')\lor[(x'\lor y)\land(x\lor y')\land z] \\
&=(x\land y'\land z')\lor(x'\land y\land z')\lor[(x'\lor y)\land(x\land z)]\lor [(x'\lor y)\land(y'\land z)] \\
&=(x\land y'\land z')\lor(x'\land y\land z')\lor[(x'\land x\land z)\lor (y\land x\land z)]\lor [(x'\land y'\land z)\lor (y\land y'\land z)] \\
&=(x\land y'\land z')\lor(x'\land y\land z')\lor(x'\land y'\land z)\lor(x\land y\land z) \\
\end{aligned}
$$

$$
\begin{aligned}
\quad x\oplus (y\oplus z)
&=(x\land[(y\land z')\lor(y'\land z)]')\lor(x'\land[(y\land z')\lor(y'\land z)]) \\
&=[x\land(y'\lor z)\land(y\lor z')]\lor(x'\land y\land z')\lor (x'\land y'\land z) \\
&=(x\land y'\land z')\lor(x'\land y\land z')\lor(x'\land y'\land z)\lor(x\land y\land z) \\
\end{aligned}
$$

$\therefore \langle B,\oplus\rangle满足结合律, 构成半群$

$\because x\oplus 0=(x\land 1)\lor(x'\land 0)=x, 0\oplus x=(0\land x')\lor (1\land x)=x$

$\therefore 0是\langle B,\oplus\rangle的幺, \langle B,\oplus\rangle形成幺半群$

$\because x\oplus x=(x\land x')\lor(x'\land x)=0$

$\therefore x的逆元是它自身, 逆元均存在, \langle B,\oplus\rangle形成群$

$\because x\oplus y=(x\land y')\lor (x'\land y)=(y\land x')\lor (y'\land x)=y\oplus x$

$\therefore \langle B,\oplus\rangle形成阿贝尔群$


# Problem 4

$\because a\preceq c$

$\therefore a\land c=a$

$\therefore a\lor(b\land c)=(a\lor b)\land (a\lor c)=(a\lor b)\land c$


# Problem 5

## (1)

$当n=2时,$

$由德摩根律可知(a_1\lor a_2)=a_1'\land a_2'成立$

$假设当n=k时, 有(a_1\lor a_2\lor \cdots \lor a_k)'=a_1'\land a_2'\land \cdots \land a_k'$

$当n=k+1时,$

$
\begin{aligned}
(a_1\lor a_2\lor \cdots \lor a_k \lor a_{k+1})'
&=(a_1\lor a_2\lor \cdots \lor a_k)' \land a_{k+1}' \\
&=a_1'\land a_2'\land \cdots \land a_k' \land a_{k+1}' \\
\end{aligned}
$

$\therefore (a_1\lor a_2\lor \cdots \lor a_n)'=a_1'\land a_2'\land \cdots \land a_n'成立$

## (2)

$当n=2时,$

$由德摩根律可知(a_1\land a_2)=a_1'\lor a_2'成立$

$假设当n=k时, 有(a_1\land a_2\land \cdots \land a_k)'=a_1'\lor a_2'\lor \cdots \lor a_k'$

$当n=k+1时,$

$
\begin{aligned}
(a_1\land a_2\land \cdots \land a_k \land a_{k+1})'
&=(a_1\land a_2\land \cdots \land a_k)' \lor a_{k+1}' \\
&=a_1'\lor a_2'\lor \cdots \lor a_k' \lor a_{k+1}' \\
\end{aligned}
$

$\therefore (a_1\land a_2\land \cdots \land a_n)'=a_1'\lor a_2'\lor \cdots \lor a_n'成立$


# Problem 6

$对于\forall a,b\in B,$

$
\begin{aligned}
a\preceq b
&\Leftrightarrow a\land b=a \\
&\Leftrightarrow a'\lor b'=a' \\
&\Leftrightarrow b'\lor a'=a' \\
&\Leftrightarrow b'\preceq a' \\
\end{aligned}
$


# Problem 7

$\because B_1\simeq B_2, B_2\simeq B_3$

$\therefore 存在双射函数f:B_1\to B_2, 双射函数g:B_2\to B_3$
$\quad 使得(\forall x,y\in B_1)(x\preceq y\leftrightarrow f(x)\preceq f(y))$
$\quad \qquad(\forall x,y\in B_2)(x\preceq y\leftrightarrow g(x)\preceq g(y))$

$\therefore 双射函数F=g\circ f可以满足$
$\quad (\forall x,y\in B_1)(x\preceq y\leftrightarrow f(x)\preceq f(y)\leftrightarrow g(f(x))\preceq g(f(y))\leftrightarrow F(x)\preceq F(y))$

$\therefore B_1\simeq B_3$


# Problem 8

## (1)

| x    | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| F(x) | 0   | 1   | 1   | 1   | 0   | 1   | 0   | 0   |

## (2)

$F(x,y,z)=(x'\land y'\land z)\lor(x'\land y\land z')\lor(x'\land y\land z)\lor(x\land y'\land z)\lor(x\land y\land z)$

## (3)

$F(x,y,z)=(x'\land y)\lor(x'\land z)\lor(x\land y'\land z)$

# Problem 9

$对于充分性:$

$当a=b时, 易见(a\land b')\lor (a'\land b)=(a\land a')\lor (a'\land a)=0$

$对于必要性:$

$\because (a\land b')\lor (a'\land b)=0$

$\therefore a\land b'=0, a'\land b=0$

$\therefore a\land b'=0, a\lor b'=1$

$\therefore b'是a的补元$

$\therefore 由补元唯一性定理可知, b'=a'$

$\therefore a=b$