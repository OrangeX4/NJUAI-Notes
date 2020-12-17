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

$\therefore \langle B,\oplus\rangle满足结合律, $

