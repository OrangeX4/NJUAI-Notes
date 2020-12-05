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

