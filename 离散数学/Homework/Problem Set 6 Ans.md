# Problem Set 6

# Problem 1

a) 正确

b) 错误

c) 错误

d) 正确


# Problem 2

$不妨假定A-B\neq \empty, 取a\in A-B, b\in B$

$\therefore (a,b)\in A \times B$

$\because a\not\in B$

$\therefore (a,b)\not\in B\times A$

$\therefore A\times B\neq B\times A$


# Problem 3

a) $R^{-1}=\{(b,a)|(a,b)\in R\}=\{(b,a)|a整除b\}$

b) $R^{-1}=\{(a,b)|(a,b)\not\in R\}=\{(a,b)|a不整除b\}$


# Problem 4

$\because R=\{(1,2),(1,3),(2,3),(2,4),(3,1)\},$
$\quad S=\{(2,1),(3,1),(3,2),(4,2)\}$

$\therefore S \circ R=\{(1,1),(1,2),(2,1),(2,2)\}$


# Problem 5

$\because R=R^{-1},S=S^{-1}$

$\therefore (R\circ S)^{-1}=S^{-1}\circ R^{-1}=S\circ R$

$\because R\circ S \subseteq S\circ R$

$\therefore R\circ S\subseteq (R\circ S)^{-1}$

$\because 显然|R\circ S|=|(R\circ S)^{-1}|, 即元素个数相等$

$\therefore R\circ S = (R\circ S)^{-1}$

$\therefore (R\circ S)^{-1}\subseteq R\circ S$

$\therefore S \circ R\subseteq R\circ S$

$\therefore R\circ S = S\circ R$


# Problem 6

## (1)

$b的论文导师的论文导师是a的时候.$

## (2)

$b的n辈论文导师是a的时候.$

# Problem 7

a) $R_1\cup R_2=\{(a,b)|a\equiv b(mod3) \lor a\equiv b(mod4)\}$

b) $R_1\cap R_2=\{(a,b)|a\equiv b(mod3) \land a\equiv b(mod4)\}$

c) $R_1 - R_2=\{(a,b)|a\equiv b(mod3) \land a\not\equiv b(mod4)\}$

d) $R_2 - R_1=\{(a,b)|a\not\equiv b(mod3) \land a\equiv b(mod4)\}$

e) $R_1 \oplus R_2=\{(a,b)|(a\equiv b(mod3) \land a\not\equiv b(mod4))\lor (a\not\equiv b(mod3) \land a\equiv b(mod4))\}$


# Problem 8

a) $有2^{4^2}=2^{16}=256\times 256=65536种关系.$

b) $有2^{(4^2-1)}=2^{15}=256\times 128=32768种关系.$

# Problem 9

a) $R\circ S=\{(x,y)|y=2x+5\}$

b) $R\circ S=\{(x,y)|y=x^2+3x-3\}$

c) $R\circ S=\{(x,y)|y=2^{\sqrt{x}} \lor y=2^{-\sqrt{x}}\}$

d) $R\circ S=\{(x,y)|y=2^{x^2}\}$

# Problem 10

## a)

$$
\begin{aligned}
(R_1\cup R_2)^{-1}&=\{(y,x)|(x,y)\in R_1\cup R_2\} \\
&=\{(y,x)|(x,y)\in R_1 \lor (x,y)\in R_2\} \\
&=\{(y,x)|(y,x)\in R_1^{-1} \lor (y,x)\in R_2^{-1}\} \\
&=R_1^{-1}\cup R_2^{-1}
\end{aligned}
$$

## b)

$$
\begin{aligned}
(R_1\cap R_2)^{-1}&=\{(y,x)|(x,y)\in R_1\cap R_2\} \\
&=\{(y,x)|(x,y)\in R_1 \land (x,y)\in R_2\} \\
&=\{(y,x)|(y,x)\in R_1^{-1} \land (y,x)\in R_2^{-1}\} \\
&=R_1^{-1}\cap R_2^{-1}
\end{aligned}
$$

