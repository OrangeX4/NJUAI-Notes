# Problem Set 14

# Problem 1

## (1)

$\displaystyle \because\forall x,y\in \mathbb{Z}, f(x+y)=(-1)^{x+y}=(-1)^{x}\cdot (-1)^{y}=f(x)\cdot f(y)$

$\displaystyle \therefore 是同态$

$\displaystyle \because f(1)=f(3)=-1, 不是单同态$

$\displaystyle \because 不存在x使得f(x)=\frac{1}{2}$

$\displaystyle \therefore 不是满同态, 不是同构$

## (2)

$
\begin{aligned}
&\because \forall x,y\in \mathbb{Z}, \\
&\quad f(x+y)=e^{i(x+y)} \\
&=e^{ix}\cdot e^{iy} \\
&=(\cos x+i\sin x)\cdot (\cos y+i\sin y) \\
&=f(x)\cdot f(y)
\end{aligned}
$

$\therefore 是同态$

$\because 若f(x)=f(y)$

$\therefore e^{ix}=e^{iy}$

$\therefore x=y$

$\therefore 是单同态$

$\displaystyle \because 不存在x使得f(x)=\cos\frac{1}{2}+i\sin \frac{1}{2}$

$\therefore 不是满同态, 不是同构$


# Problem 2

$设\langle G, *\rangle 是无限循环群, 则\langle G, *\rangle \simeq \langle \mathbb{Z}, +\rangle$

$\therefore 存在f:G\to \mathbb{Z},$
$\quad 使得\forall x,y\in\mathbb{Z}, f(x+y)=f(x)*f(y), f(y+x)=f(y)*f(x)$

$\because \langle \mathbb{Z}, +\rangle是阿贝尔群$

$\therefore x+y=y+x$

$\therefore f(x+y)=f(y+x)$

$\therefore f(x)*f(y)=f(y)*f(x)$

$\therefore \langle G,*\rangle 也是阿贝尔群$

$设\langle G, *\rangle 是无限循环群, 则\langle G, *\rangle \simeq \langle \mathbb{Z}_n, \oplus_n\rangle$

$\therefore 存在f:G\to \mathbb{Z}_n,$
$\quad 使得\forall x,y\in\mathbb{Z}, f(x\oplus_n y)=f(x)*f(y), f(y\oplus_n x)=f(y)*f(x)$

$\because \langle\mathbb{Z}_n, \oplus_n\rangle是阿贝尔群$

$\therefore x\oplus_n y=y\oplus_n x$

$\therefore f(x\oplus_n y)=f(y\oplus_n x)$

$\therefore f(x)*f(y)=f(y)*f(x)$

$\therefore \langle G,*\rangle 也是阿贝尔群$


# Problem 3

$\therefore \forall x,y\in G_1, f(xy)=f(x)f(y)$

**$若G_1为有限循环群$**

$设G_{1}=\{a^0, a^1,a^2,\cdots,a^{n-1}\}$

$\therefore f(G_1)=\{f(a^0),f(a^1),f(a^2),\cdots,f(a^{n-1})\}$

$\because \forall x\in G_1, f(a^0)f(x)=f(a^0x)=f(x), f(x)f(a^0)=f(xa^0)=f(x)$

$\therefore f(a^0)是f(G_1)的幺$

$\because f(a^k)=f(a^1a^{k-1})=f(a^1)f(a^{k-1})=f(a^1)\cdots f(a^1)=f(a^1)^k$

$\therefore f(G_1)=\langle f(a^1)\rangle$

$\therefore f(G_1)是循环群$

**$若G_1为无限循环群$**

$设G_{1}=\{a^0, a^{\pm 1},a^{\pm 2},\cdots\}$

$\therefore f(G_1)=\{f(a^0),f(a^{\pm 1}),f(a^{\pm 2}),\cdots\}$

$\because \forall x\in G_1, f(a^0)f(x)=f(a^0x)=f(x), f(x)f(a^0)=f(xa^0)=f(x)$

$\therefore f(a^0)是f(G_1)的幺$

$当k\geq 1时,$

$\therefore f(a^k)=f(a^1a^{k-1})=f(a^1)f(a^{k-1})=f(a^1)\cdots f(a^1)=f(a^1)^k$

$当k\leq -1时,$

$\therefore f(a^k)=f(a^{-1}a^{k+1})=f(a^{-1})f(a^{k+1})=f(a^{-1})\cdots f(a^{-1})=f(a^{-1})^{-k}=(f(a^{1})^{-1})^{-k}=f(a^1)^k$

$\therefore f(G_1)=\langle f(a^1)\rangle$

$\therefore f(G_1)是循环群$


# Problem 4

## (1)

$\therefore G=\{a^0, a^1,a^2,\cdots,a^{14}\}$

$设a^{r}是G的生成元$

$\therefore \gcd(15,r)=1$

$\therefore r的值只能取1,2,4,7,8,11,13,14$

$\therefore G的生成元为a^1,a^{2},a^{4},a^{7},a^{8},a^{11},a^{13},a^{14}$

## (2)

$\because 15的因子为1,3,5,15$

$\therefore G的子群分别是:$

$\quad G自身$
$\quad G_3=\{a^0,a^3,a^6,a^9,a^{12}\}$
$\quad G_5=\{a^0,a^5,a^{10}\}$
$\quad G_{15}=\{a^0\}$


# Problem 5

$\because 3阶群在同构意义下只有一个$

| *   | e   | a   | b   |
| --- | --- | --- | --- |
| e   | e   | a   | b   |
| a   | a   | b   | e   |
| b   | b   | e   | a   |

$\therefore 设G=\{e,a,b\}$

$\therefore a^0=e,a^1=a,a^2=b$

$\therefore G为循环群, 设另一个3阶群为S$

$\therefore \exist双射函数f:G\to S, \forall x,y\in G,f(xy)=f(x)f(y)$

$\because \forall x\in G, f(e)f(x)=f(ex)=f(x), f(x)f(e)=f(xe)=f(x)$

$\therefore f(e)是S的单位元$

$\therefore e\neq a\neq a^2, f为双射$

$\therefore f(e)\neq f(a)\neq f(a^2)=f(a)f(a)=f(a)^2$

$\therefore S的生成元为f(a)$

$\therefore 三阶群必为循环群$


# Problem 6

$\therefore \forall x\in G, x^2=e$

$\therefore \forall x,y\in G, (xy)^2=xy xy=e$

$\therefore xy xyy=xy x(yy)=xyx=y$

$\therefore xy xx=xy (xx)=xy=yx$

$\therefore \langle G,*\rangle是阿贝尔群$


# Problem 7

$设G=\{a^0, a^{\pm 1},a^{\pm 2},\cdots\}, G'=\{b^0, b^1,b^2,\cdots,b^{n-1}\}$

$令f:G\to G', f(a^k)=b^{(k\mod n)}$

$\therefore\forall a^x,a^y\in G,$
$f(a^xa^y)=f(a^{x+y})=b^{(x+y\mod n)}=b^{(x\mod n)+(y\mod n)}=b^{(x\mod n)}+b^{(y\mod n)}=f(a^x)f(a^y)$

$\therefore f是G到G'的同态$

$\because f(a^r)=b^{(r\mod n)}=b^r, 0\leq r \leq n-1$

$\therefore f是满射$

$\therefore f是G到G'的满同态映射$


# Problem 8

$假设有理数加群Q为循环群$

$\therefore \exist q\in Q, 使得Q=\langle q\rangle=\{q^0, q^{\pm 1},q^{\pm 2},\cdots\}$

$\because 无限循环群的生成元q只有两个$

$不妨设q>0, 易知Q的幺为0, 设Q中的元素为q^n, n\in \mathbb{Z}$

$当n\leq 0时, q^n=-\displaystyle\sum_{i=1}^{-n} q\leq 0$

$当n\geq 1时, q^n=\displaystyle\sum_{i=1}^n q \geq q$

$\because \displaystyle\frac{q}{2}\in Q, 且0<\frac{q}{2}<q$

$\therefore 不存在n\in \mathbb{Z}使得q^n=\displaystyle\frac{q}{2}$

$\therefore 与假设矛盾, Q不是循环群$

$\because 整数加群Z是循环群$

$\therefore 整数加群Z喝有理数加群Q不同构$