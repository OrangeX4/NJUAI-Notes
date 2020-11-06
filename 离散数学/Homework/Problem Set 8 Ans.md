# Problem Set 8

# Problem 1

a) 不是

b) 是

c) 不是


# Problem 2

a) 是

b) 不是

c) 是

d) 不是


# Problem 3

a) $\{-1,1\}$

b) $\{x|-1<x<1\land x\neq 0\}$

c) $\{x|x<-2\land x>2\}$


# Problem 4

## a)

$不是单射, 不是满射, 也不是双射.$

$\because f((1,2))=f((2,1))=4$

$\therefore 不是单射$

$\because 不存在(x,y)使得f((x,y))=x+y+1=0$

$\therefore 不是满射$

$\therefore 也不是双射$

## b)

$A=\{(0,2),(1,1),(2,0)\}$

## c)

$B=\{3,5,7\}$


# Problem 5

## a)

$是单射, 但是不是满射.$

$\because 任取x,y\in \mathbb N$

$若f(x)=f(y)即(x,x+1)=(y,y+1)$

$则有x=y$

$\therefore f是单射的$

$不存在x使得f(x)=(1,1)$

$\therefore 不是满射$

## b)

$存在.$

$f^{-1}: \{(x, x+1)|x\in \mathbb{N}\}\to \mathbb{N}, f((x,x+1))=x$

## c)

$\text{Ran}(f)=\{(x, x+1)|x\in \mathbb{N}\}$


# Problem 6

$若对于b_1,b_2有g(b_1)=g(b_2)$

$即\{x|x\in A\land f(x)=b_1\}=\{x|x\in A\land f(x)=b_2\}$

$\because f为满射$

$\therefore \forall b \in B\exist x\in A(f(x)=b)$

$\therefore g(b_1), g(b_2)不是空集$

$\therefore \{x|x\in A\land f(x)=b_1 \land f(x)=b_2\}也不是空集$

$\therefore f(x)=b_1和f(x)=b_2可对同一个x成立$

$\therefore 根据函数的定义可知b_1=b_2$

$\therefore g为单射$


# Problem 7

$对于关系f,g,我们有:$

$
\begin{aligned}
&(x,y)\in (f\circ g)^{-1} \\
\Leftrightarrow&(y,x)\in f\circ g \\
\Leftrightarrow&\exist t(t\in Y\land (y,t)\in g\land (t,x)\in f) \\
\Leftrightarrow&\exist t(t\in Y\land (t,y)\in g^{-1}\land (x,t)\in f^{-1}) \\
\Leftrightarrow&(x,y)\in g^{-1}\circ f^{-1} \\
\end{aligned}
$

$只需证明(f\circ g)^{-1}是函数$

$即要证(\forall x,y,z)(x(f\circ g)^{-1}y\land x(f\circ g)^{-1}z \to y = z)$

$当有\exist t_1(t_1\in Y\land (t_1,y)\in g^{-1}\land (x,t_1)\in f^{-1})$
$且有\exist t_2(t_2\in Y\land (t_2,z)\in g^{-1}\land (x,t_2)\in f^{-1})时$

$\because f是Y到Z的双射函数, g是X到Y的双射函数$

$\therefore f^{-1},g^{-1}也是函数$

$\because (x,t_1)\in f^{-1}, (x,t_2)\in f^{-1}$

$\therefore t_1=t_2$

$\because (t_1,y)\in g^{-1}, (t_2,z)\in g^{-1}$

$\therefore y=z$

$\therefore 可知(f\circ g)^{-1}也是函数$

$\therefore f\circ g的反函数可以用(f\circ g)^{-1}=g^{-1}\circ f^{-1}表示$


# Problem 8

## a)

$\because S是m元集, m为正整数$

$\therefore 采取一定的排序方式, 可以对S里的元素命名为a_1, a_2,\cdots, a_m$
$\quad 并且a_i(i=1,2,\cdots,m)是确定的且两两相异的$

$令f=\{(a_i,i)|i\in \{1,2,\cdots,m\}\}$

$若f(a_x)=f(a_y)即x=y$

$则有a_x=a_y$

$\therefore f是单射的$

$\because \text{Ran}(f)=\{y|\exist x\in S(f(x)=y)\}=\{1,2,\cdots,m\}$

$\therefore f是满射的$

$\therefore 该f是双射函数, 说明存在一个双射函数成立$

## b)

$\therefore 同(a)可知存在a_i\in S, b_i\in T,i=1,2,\cdots,m$

$令f=\{(a_i,b_i)|i\in \{1,2,\cdots,m\}\}$

$若f(a_x)=f(a_y)即b_x=b_y$

$则有a_x=a_y$

$\therefore f是单射的$

$\because \text{Ran}(f)=\{y|\exist x\in S(f(x)=y)\}=T$

$\therefore f是满射的$

$\therefore 该f是双射函数, 说明存在一个双射函数成立$

# Problem 9

$\because f和g是函数$

$\therefore \forall x,y,z((x,y)\in f \land (x,z)\in f \to y=z)$
$且\forall x,y,z((x,y)\in g \land (x,z)\in g \to y=z)$

$对任意的x,y,z, 当有(x,y)\in f\cap g \land (x,z)\in f\cap g时$

$即有(x,y)\in f \land (x,y)\in g \land (x,z)\in f \land (x,z)\in g$

$\therefore (x,y)\in f \land (x,z)\in f$

$\therefore y=z$

$\therefore \forall x,y,z((x,y)\in f\cap g \land (x,z)\in f\cap g \to y=z)$

$\therefore f\cap g也是函数$
