# Problem Set 7

# Problem 1

a) 自反, 传递

b) 对称

c) 对称

d) 对称


# Problem 2

$取元素b\in A使得(a,b)\in R错误, 并不一定能找出这样的(a,b)$


# Problem 3

$\because 集合A上的R是自反的$

$\therefore \forall x\in A(xRx)$

$\because aRb \Leftrightarrow bR^{-1}a$

$\therefore \forall x\in A(xR^{-1}x)$

$\therefore R^{-1}是自反的$


# Problem 4

$\because 集合A上的R是自反的$

$\therefore \forall x\in A(xRx)$

$\therefore \forall x\in A(xRx \land xRx)$

$\therefore \forall x\in A(xRxRx)$

$\therefore \forall x\in A(xR^2x)$

$同理 \forall x\in A(xRx \land \cdots \land xRx)$

$\therefore \forall x\in A(xR^nx)$

$\therefore R^n是自反的$


# Problem 5

$$
M_{R_1}=
\begin{bmatrix}
0 &1 &0 \\
1 &1 &1 \\
1 &0 &0 \\
\end{bmatrix}
,
M_{R_1}=
\begin{bmatrix}
0 &1 &0 \\
0 &1 &1 \\
1 &1 &1 \\
\end{bmatrix}
$$

a)

$$
M_{R_1\cup R_2}=
\begin{bmatrix}
0 &1 &0 \\
1 &1 &1 \\
1 &1 &1 \\
\end{bmatrix}
$$

b)

$$
M_{R_1\cap R_2}=
\begin{bmatrix}
0 &1 &0 \\
0 &1 &1 \\
1 &0 &0 \\
\end{bmatrix}
$$

c)

$$
\begin{aligned}
\begin{bmatrix}
0 &1 &0 \\
0 &1 &1 \\
1 &1 &1 \\
\end{bmatrix}
\\
\begin{bmatrix}
0 &1 &0 \\
1 &1 &1 \\
1 &0 &0 \\
\end{bmatrix}
\begin{bmatrix}
0 &1 &1 \\
1 &1 &1 \\
0 &1 &0 \\
\end{bmatrix}
\end{aligned}
$$

$$
M_{R_2\circ R_1}=
\begin{bmatrix}
0 &1 &1 \\
1 &1 &1 \\
0 &1 &0 \\
\end{bmatrix}
$$

d)

$$
\begin{aligned}
\begin{bmatrix}
0 &1 &0 \\
1 &1 &1 \\
1 &0 &0 \\
\end{bmatrix}
\\
\begin{bmatrix}
0 &1 &0 \\
1 &1 &1 \\
1 &0 &0 \\
\end{bmatrix}
\begin{bmatrix}
1 &1 &1 \\
1 &1 &1 \\
0 &1 &0 \\
\end{bmatrix}
\end{aligned}
$$

$$
M_{R_1\circ R_2}=
\begin{bmatrix}
1 &1 &1 \\
1 &1 &1 \\
0 &1 &0 \\
\end{bmatrix}
$$

e)

$$
M_{R_1\oplus R_2}=
\begin{bmatrix}
0 &0 &0 \\
1 &0 &0 \\
0 &1 &1 \\
\end{bmatrix}
$$


# Problem 6

## a)

$$
\begin{aligned}
&
\begin{bmatrix}
0 &0 &1 &0 &0 \\
0 &0 &0 &1 &0 \\
1 &0 &0 &0 &0 \\
0 &1 &0 &0 &0 \\
0 &0 &0 &1 &0 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
0 &0 &1 &0 &0 \\
0 &0 &0 &1 &0 \\
1 &0 &1 &0 &0 \\
0 &1 &0 &0 &0 \\
0 &0 &0 &1 &0 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
0 &0 &1 &0 &0 \\
0 &0 &0 &1 &0 \\
1 &0 &1 &0 &0 \\
0 &1 &0 &1 &0 \\
0 &0 &0 &1 &0 \\
\end{bmatrix}
\\
\Rightarrow
&
\begin{bmatrix}
1 &0 &1 &0 &0 \\
0 &0 &0 &1 &0 \\
1 &0 &1 &0 &0 \\
0 &1 &0 &1 &0 \\
0 &0 &0 &1 &0 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
1 &0 &1 &0 &0 \\
0 &1 &0 &1 &0 \\
1 &0 &1 &0 &0 \\
0 &1 &0 &1 &0 \\
0 &1 &0 &1 &0 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
1 &0 &1 &0 &0 \\
0 &1 &0 &1 &0 \\
1 &0 &1 &0 &0 \\
0 &1 &0 &1 &0 \\
0 &1 &0 &1 &0 \\
\end{bmatrix}
\end{aligned}
$$

## b)

$$
\begin{aligned}
&
\begin{bmatrix}
0 &0 &0 &0 &0 \\
0 &0 &1 &0 &1 \\
0 &0 &0 &0 &1 \\
1 &0 &0 &0 &0 \\
0 &1 &1 &0 &0 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
0 &0 &0 &0 &0 \\
0 &0 &1 &0 &1 \\
0 &0 &0 &0 &1 \\
1 &0 &0 &0 &0 \\
0 &1 &1 &0 &0 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
0 &0 &0 &0 &0 \\
0 &0 &1 &0 &1 \\
0 &0 &0 &0 &1 \\
1 &0 &0 &0 &0 \\
0 &1 &1 &0 &1 \\
\end{bmatrix}
\\
\Rightarrow
&
\begin{bmatrix}
0 &0 &0 &0 &0 \\
0 &0 &1 &0 &1 \\
0 &0 &0 &0 &1 \\
1 &0 &0 &0 &0 \\
0 &1 &1 &0 &1 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
0 &0 &0 &0 &0 \\
0 &0 &1 &0 &1 \\
0 &0 &0 &0 &1 \\
1 &0 &0 &0 &0 \\
0 &1 &1 &0 &1 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
0 &0 &0 &0 &0 \\
0 &1 &1 &0 &1 \\
0 &1 &1 &0 &1 \\
1 &0 &0 &0 &0 \\
0 &1 &1 &0 &1 \\
\end{bmatrix}
\end{aligned}
$$

## c)

$$
\begin{aligned}
&
\begin{bmatrix}
0 &1 &1 &0 &1 \\
1 &0 &1 &0 &0 \\
1 &0 &0 &0 &0 \\
1 &0 &0 &0 &0 \\
0 &0 &0 &1 &0 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
0 &1 &1 &0 &1 \\
1 &1 &1 &0 &1 \\
1 &1 &1 &0 &1 \\
1 &1 &1 &0 &1 \\
0 &0 &0 &1 &0 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
1 &1 &1 &0 &1 \\
1 &1 &1 &0 &1 \\
1 &1 &1 &0 &1 \\
1 &1 &1 &0 &1 \\
0 &0 &0 &1 &0 \\
\end{bmatrix}
\\
\Rightarrow
&
\begin{bmatrix}
1 &1 &1 &0 &1 \\
1 &1 &1 &0 &1 \\
1 &1 &1 &0 &1 \\
1 &1 &1 &0 &1 \\
0 &0 &0 &1 &0 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
1 &1 &1 &0 &1 \\
1 &1 &1 &0 &1 \\
1 &1 &1 &0 &1 \\
1 &1 &1 &0 &1 \\
1 &1 &1 &1 &1 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
1 &1 &1 &1 &1 \\
1 &1 &1 &1 &1 \\
1 &1 &1 &1 &1 \\
1 &1 &1 &1 &1 \\
1 &1 &1 &1 &1 \\
\end{bmatrix}
\end{aligned}
$$

## d)

$$
\begin{aligned}
&
\begin{bmatrix}
0 &0 &0 &0 &1 \\
1 &0 &0 &1 &0 \\
0 &0 &0 &1 &0 \\
1 &0 &1 &0 &0 \\
1 &1 &1 &0 &1 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
0 &0 &0 &0 &1 \\
1 &0 &0 &1 &1 \\
0 &0 &0 &1 &0 \\
1 &0 &1 &0 &1 \\
1 &1 &1 &0 &1 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
0 &0 &0 &0 &1 \\
1 &0 &0 &1 &1 \\
0 &0 &0 &1 &0 \\
1 &0 &1 &0 &1 \\
1 &1 &1 &1 &1 \\
\end{bmatrix}
\\
\Rightarrow
&
\begin{bmatrix}
0 &0 &0 &0 &1 \\
1 &0 &0 &1 &1 \\
0 &0 &0 &1 &0 \\
1 &0 &1 &1 &1 \\
1 &1 &1 &1 &1 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
0 &0 &0 &0 &1 \\
1 &0 &1 &1 &1 \\
1 &0 &1 &1 &1 \\
1 &0 &1 &1 &1 \\
1 &1 &1 &1 &1 \\
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
1 &1 &1 &1 &1 \\
1 &1 &1 &1 &1 \\
1 &1 &1 &1 &1 \\
1 &1 &1 &1 &1 \\
1 &1 &1 &1 &1 \\
\end{bmatrix}
\end{aligned}
$$


# Problem 7

$论域为正整数.$

$\therefore R=\{((a,b), (c,d))|a+d=b+c\}$

$对于自反性:$

$\because \forall a\forall b(a+b=b+a)$

$\therefore \forall a\forall b((a, b),(a,b))\in R$

$\therefore 自反性成立.$

$对于对称性:$

$假设((a,b), (c,d))\in R$

$\therefore a+d=b+c$

$\therefore c+b=d+a$

$\therefore ((c,d),(a,b))\in R$

$\therefore (\forall a,b,c,d)((a,b)R(c,d) \to (c,d)R(a,b))$

$\therefore 自反性成立$

$对于传递性:$

$(\forall x, y ,z\in A)(xRyRz \to xRz)$

$假设((a,b), (e,f)), ((e,f), (c,d))\in R$

$\therefore a+f=b+e, e+d=f+c$

$\therefore a+d=b+c$

$\therefore ((a,b), (c,d))\in R$

$\therefore (\forall a,b,c,d,e,f)((a,b)R(e,f)R(c,d) \to (a,b)R(c,d))$

$\therefore 传递性性成立$

$\because R满足自反,对称和传递性$

$\therefore R是等价关系$


# Problem 8

$\because R和S是A上的对称关系$

$\therefore (\forall x,y\in A)(xRy \to yRx), (\forall x,y\in A)(xSy \to ySx)$

$\therefore (\forall x,y\in A)(xRy \leftrightarrow yRx), (\forall x,y\in A)(xSy \leftrightarrow ySx)$

$\because R\circ S=S\circ R$

$\therefore (\forall x,y \in A)(\exist t(xStRy) \leftrightarrow \exist t(xRtSy))$

$\therefore (\forall x,y \in A)(\exist t(xStRy) \leftrightarrow \exist t(xRt\land tSy))$

$\therefore (\forall x,y \in A)(\exist t(xStRy) \leftrightarrow \exist t(ySt\land tRx))$

$\therefore (\forall x,y \in A)(\exist t(xStRy) \leftrightarrow \exist t(yStRx))$

$\therefore (\forall x,y\in A)(\exist t(xStRy) \to \exist t(yStRx))$

$\therefore R\circ S是对称关系$


# Problem 9

$\because R是A上的等价关系$

$\therefore R具有自反性$

$\therefore (\forall x,y\in A)(xRy\to xRx \land xRy)$

$\therefore (\forall x,y\in A)(xRy\to \exist t(xRt \land tRy))$

$\therefore (\forall x,y\in A)(xRy\to \exist t(xRtRy))$

$\therefore R\subseteq R^2$

$\because R具有传递性$

$\therefore R^2\subseteq R$

$\therefore R^2=R$


# Problem 10

$设R是A上的关系$

$即证r(s(R))=s(r(R))$

$r(s(R))=r(R\cup R^{-1})=R\cup R^{-1}\cup I_A=R\cup I_A\cup R^{-1}$

$
\begin{aligned}
s(r(R))&=s(R\cup I_A) \\
&=R\cup I_A\cup (R\cup I_A)^{-1} \\
&=R\cup I_A\cup I_A^{-1}\cup R^{-1} \\
&=R\cup I_A\cup I_A\cup R^{-1} \\
&=R\cup I_A\cup R^{-1} \\
\end{aligned}
$

$\therefore r(s(R))=s(r(R))$

$\therefore 原命题得证.$