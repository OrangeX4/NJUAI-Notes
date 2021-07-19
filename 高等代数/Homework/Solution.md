# 一

## (1)

$\because P(1,2(-1))\begin{bmatrix}1&2&2&\cdots &2\\0&1&1&\cdots &1\\0&0&1&\cdots &1\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\cdots &1\end{bmatrix}=\begin{bmatrix}1&1&1&\cdots &1\\0&1&1&\cdots &1\\0&0&1&\cdots &1\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\cdots &1\end{bmatrix}=B$

$\therefore A^{-1}P(1,2(-1))^{-1}=B^{-1}$

$\therefore A^{-1}=B^{-1}P(1,2(-1))=B^{-1}Q(2,1(-1))$

$用数学归纳法.$

$当n=2时, 易知有B_2^{-1}=\begin{bmatrix}1&1\\0&1\end{bmatrix}^{-1}=\begin{bmatrix}1&-1\\0&1\end{bmatrix}$

$假设当n=k时, B_k^{-1}=\begin{bmatrix}1&-1&0&\cdots &0\\0&1&-1&\cdots &0\\0&0&1&\cdots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\cdots &-1\\0&0&0&\cdots &1\end{bmatrix}$

$当n=k+1时,$

$
\begin{aligned}
B_{k+1}^{-1}
&=\begin{bmatrix}B_k&1\\0&1\end{bmatrix}^{-1}=(\displaystyle\prod_{i=1}^kP(k-i+1,(k+1)(1))\begin{bmatrix}B_k&0\\0&1\end{bmatrix})^{-1} \\
&=\begin{bmatrix}B_k^{-1}&0\\0&1\end{bmatrix}\displaystyle\prod_{i=1}^kP(i,(k+1)(-1)) \\
&=\begin{bmatrix}B_k^{-1}&0\\0&1\end{bmatrix}\displaystyle\prod_{i=1}^kQ(k+1,i(-1)) \\
&=\begin{bmatrix}1&-1&0&\cdots &0\\0&1&-1&\cdots &0\\0&0&1&\cdots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\cdots &-1\\0&0&0&\cdots &1\end{bmatrix}
\end{aligned}
$

$\therefore A^{-1}=B^{-1}Q(2,1(-1))=\begin{bmatrix}1&-2&0&\cdots &0\\0&1&-1&\cdots &0\\0&0&1&\cdots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\cdots &-1\\0&0&0&\cdots &1\end{bmatrix}$

## (2)

$\because |A|=1$

$\therefore A^*=A^{-1}$

$\therefore 代数余子式之和S=n(1-1)=0$


# 二

$假设存在这样的整系数多项式f(x), 使得f(b_i)=b_{i+1}$

$f(b_1)=a_nb_1^n+\cdots +a_{1}b_1+a_0=b_2 \qquad(1)$
$f(b_2)=a_nb_2^n+\cdots +a_{1}b_2+a_0=b_3 \qquad(2)$
$\cdots $
$f(b_m)=a_nb_m^n+\cdots +a_{1}b_m+a_0=b_1 \qquad(m)$

$令(k+1)-(k)得:$
$a_n(b_{k+1}^n-b_{k}^n)+\cdots +a_{1}(b_{k+1}-b_{k})=b_{k+2}-b_{k+1}$
$a_n(b_{k+1}^{n-1}+\cdots +b_{k}^{n-1})(b_{k+1}-b_{k})+\cdots +a_{1}(b_{k+1}-b_{k})=b_{k+2}-b_{k+1}$

$\therefore (b_{k+1}-b_{k})|(b_{k+2}-b_{k+1})$

$\therefore (b_{2}-b_{1})|(b_{3}-b_{2})|\cdots |(b_{1}-b_{m})$

$\therefore b_{2}-b_{1}=b_{3}-b_{2}=\cdots =b_{1}-b_{m}$

$\because (b_{2}-b_{1})+(b_{3}-b_{2})+\cdots +(b_{1}-b_{m})=0$

$\therefore b_{2}-b_{1}=b_{3}-b_{2}=\cdots =b_{1}-b_{m}=0$

$\therefore b_1=b_2=\cdots =b_m, 与题意b_i互不相同矛盾$

$\therefore 不存在多项式f(x)满足题意$

# 三

$D=\begin{vmatrix}2&1&-5&1\\1&-3&0&-6\\0&2&-1&2\\1&4&-7&6\end{vmatrix}=-\begin{vmatrix}1&-3&0&-6\\0&7&-5&13\\0&2&-1&2\\0&0&-2&-1\end{vmatrix}=-(7-52-10+28)=62-28-7=27$

$D_1=\begin{vmatrix}8&1&-5&1\\9&-3&0&-6\\-5&2&-1&2\\0&4&-7&6\end{vmatrix}=\begin{vmatrix}8&1&-5&1\\57&3&-30&0\\-21&0&9&0\\-48&-2&23&0\end{vmatrix}=-(-42*30-48*27+63*23+57*18)=81$

$D_2=\begin{vmatrix}2&8&-5&1\\1&9&0&-6\\0&-5&-1&2\\1&0&-7&6\end{vmatrix}=-\begin{vmatrix}1&0&-7&6\\0&-26&0&2\\0&-5&-1&2\\0&-37&0&7\end{vmatrix}=-(26*7-2*37)=74-182=-108$

$D_3=\begin{vmatrix}2&1&8&1\\1&-3&9&-6\\0&2&-5&2\\1&4&0&6\end{vmatrix}=\begin{vmatrix}1&4&0&6\\0&-7&9&-12\\0&2&-3&0\\0&0&1&-1\end{vmatrix}=-27$

$D_4=\begin{vmatrix}2&1&-5&8\\1&-3&0&9\\0&2&-1&-5\\1&4&-7&0\end{vmatrix}=\begin{vmatrix}1&4&-7&0\\0&-7&7&9\\0&2&-11&0\\0&0&-2&1\end{vmatrix}=27$

$\therefore\displaystyle x_1=\frac{D_1}{D}=3, x_2=\frac{D_2}{D}=-4, x_3=\frac{D_3}{D}=-1, x_4=\frac{D_4}{D}=1$


# 四

$当n=2,3时,$

$\begin{bmatrix}1&0&0\\0&1&0\\2&0&1\end{bmatrix}\begin{bmatrix}1&0&0\\0&1&0\\2&0&1\end{bmatrix}=\begin{bmatrix}1&0&0\\0&1&0\\4&0&1\end{bmatrix}=\begin{bmatrix}1&0&0\\0&1&0\\2\times2&0&1\end{bmatrix}$
$\begin{bmatrix}1&0&0\\0&1&0\\4&0&1\end{bmatrix}\begin{bmatrix}1&0&0\\0&1&0\\2&0&1\end{bmatrix}=\begin{bmatrix}1&0&0\\0&1&0\\6&0&1\end{bmatrix}=\begin{bmatrix}1&0&0\\0&1&0\\2\times3&0&1\end{bmatrix}$

$假设当n=k时有\begin{bmatrix}1&0&0\\0&1&0\\2&0&1\end{bmatrix}^k=\begin{bmatrix}1&0&0\\0&1&0\\2k&0&1\end{bmatrix}成立$

$当n=k+1时,$

$\begin{bmatrix}1&0&0\\0&1&0\\2&0&1\end{bmatrix}^{k+1}=\begin{bmatrix}1&0&0\\0&1&0\\2k&0&1\end{bmatrix}\begin{bmatrix}1&0&0\\0&1&0\\2&0&1\end{bmatrix}=\begin{bmatrix}1&0&0\\0&1&0\\2(k+1)&0&1\end{bmatrix}$

$\therefore \begin{bmatrix}1&0&0\\0&1&0\\2&0&1\end{bmatrix}^{100}=\begin{bmatrix}1&0&0\\0&1&0\\200&0&1\end{bmatrix}$

$当n=2,3,\cdots $

$\begin{bmatrix}0&0&1\\0&1&0\\0&0&0\end{bmatrix}\begin{bmatrix}0&0&1\\0&1&0\\0&0&0\end{bmatrix}=\begin{bmatrix}0&0&0\\0&1&0\\0&0&0\end{bmatrix}$
$\begin{bmatrix}0&0&0\\0&1&0\\0&0&0\end{bmatrix}\begin{bmatrix}0&0&1\\0&1&0\\0&0&0\end{bmatrix}=\begin{bmatrix}0&0&0\\0&1&0\\0&0&0\end{bmatrix}$

$\therefore \begin{bmatrix}0&0&1\\0&1&0\\0&0&0\end{bmatrix}^{99}=\begin{bmatrix}0&0&0\\0&1&0\\0&0&0\end{bmatrix}$

$\therefore M=\begin{bmatrix}1&0&0\\0&1&0\\200&0&1\end{bmatrix}\begin{bmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{bmatrix}\begin{bmatrix}0&0&0\\0&1&0\\0&0&0\end{bmatrix}=\begin{bmatrix}1&0&0\\0&1&0\\200&0&1\end{bmatrix}\begin{bmatrix}0&a_{12}&0\\0&a_{22}&0\\0&a_{32}&0\end{bmatrix}=\begin{bmatrix}0&a_{12}&0\\0&a_{22}&0\\0&200a_{12}+a_{32}&0\end{bmatrix}$


# 五

$令A=[\alpha_1\quad\alpha_2\quad\cdots \quad\alpha_n]$
$(给向量组降维使之变为方阵)$

$\because A^TA=\begin{bmatrix}\alpha_1^T\\\alpha_2^T\\\vdots \\\alpha_n^T\end{bmatrix}[\alpha_1\quad\alpha_2\quad\cdots \quad\alpha_n]=\begin{vmatrix}\alpha_1^T\alpha_1&\alpha_1^T\alpha_2&\cdots &\alpha_1^T\alpha_n\\\alpha_2^T\alpha_1&\alpha_2^T\alpha_2&\cdots &\alpha_2^T\alpha_n\\\vdots &\vdots & &\vdots \\\alpha_n^T\alpha_1&\alpha_n^T\alpha_2&\cdots &\alpha_n^T\alpha_n\end{vmatrix}$

$\therefore D=|A^TA|=|A^T||A|=|A|^2$

$\therefore D和|A|同时为0或同时不为0, 且|A|\neq 0\Leftrightarrow 向量组线性无关$

$\therefore 向量组线性\alpha_1,\alpha_2,\cdots,\alpha_n线性无关的充要条件是D\neq 0$

---

$D\neq 0$

$\Leftrightarrow$

$
\begin{cases}
a_{11}(a_{11}k_{11}+\cdots +a_{1n}k_{1n})+\cdots +a_{n1}(a_{11}k_{n1}+\cdots +a_{1n}k_{nn})=0 \\
a_{12}(a_{11}k_{11}+\cdots +a_{1n}k_{1n})+\cdots +a_{n2}(a_{11}k_{n1}+\cdots +a_{1n}k_{nn})=0 \\
\cdots \\
a_{1n}(a_{11}k_{11}+\cdots +a_{1n}k_{1n})+\cdots +a_{nn}(a_{11}k_{n1}+\cdots +a_{1n}k_{nn})=0 \\
\cdots \\
\cdots \\
\cdots \\
a_{1n}(a_{n1}k_{11}+\cdots +a_{nn}k_{1n})+\cdots +a_{nn}(a_{n1}k_{n1}+\cdots +a_{nn}k_{nn})=0 \\
\end{cases}
$
$有非零解k_{ij}$

$\Leftrightarrow$

$
\begin{cases}
a_{11}(a_{11}k_{11}+\cdots +a_{n1}k_{n1})+\cdots +a_{1n}(a_{11}k_{1n}+\cdots +a_{n1}k_{nn})=0 \\
a_{21}(a_{11}k_{11}+\cdots +a_{n1}k_{n1})+\cdots +a_{2n}(a_{11}k_{1n}+\cdots +a_{n1}k_{nn})=0 \\
\cdots \\
a_{n1}(a_{11}k_{11}+\cdots +a_{n1}k_{n1})+\cdots +a_{nn}(a_{11}k_{1n}+\cdots +a_{n1}k_{nn})=0 \\
\cdots \\
\cdots \\
\cdots \\
a_{n1}(a_{1n}k_{11}+\cdots +a_{nn}k_{n1})+\cdots +a_{nn}(a_{1n}k_{1n}+\cdots +a_{nn}k_{nn})=0 \\
\end{cases}
$
$有非零解k_{ij}$

$\Leftrightarrow$

$
\begin{cases}
a_{11}(a_{11}k_{11}+\cdots +a_{n1}k_{n1})+\cdots +a_{1n}(a_{11}k_{1n}+\cdots +a_{n1}k_{nn})=0 \\
a_{11}(a_{12}k_{11}+\cdots +a_{n2}k_{n1})+\cdots +a_{1n}(a_{12}k_{1n}+\cdots +a_{n2}k_{nn})=0 \\
\cdots \\
a_{11}(a_{1n}k_{11}+\cdots +a_{nn}k_{n1})+\cdots +a_{1n}(a_{1n}k_{1n}+\cdots +a_{nn}k_{nn})=0 \\
\cdots \\
\cdots \\
\cdots \\
a_{n1}(a_{1n}k_{11}+\cdots +a_{nn}k_{n1})+\cdots +a_{nn}(a_{1n}k_{1n}+\cdots +a_{nn}k_{nn})=0 \\
\end{cases}
$
$有非零解k_{ij}$

$\Leftarrow 或 \Rightarrow 或\Leftrightarrow 或都不是?$

$
\begin{cases}
a_{11}k_{1j}+\cdots +a_{n1}k_{nj}=0 \\
a_{12}k_{1j}+\cdots +a_{n2}k_{nj}=0 \\
\cdots \\
a_{1n}k_{1j}+\cdots +a_{nn}k_{nj}=0 \\
\end{cases}
$
$有非零解k_{ij}$

$\Leftrightarrow$

$存在不全等于0的k_i使得k_1\alpha_1+k_2\alpha_2+\cdots +k_n\alpha_n=0$

$\Leftrightarrow$

$\alpha_1,\alpha_2,\cdots,\alpha_n线性无关$

$'|A|方程组有非零解 \Rightarrow D方程组有非零解'易证$

$'D有非零解 \Rightarrow |A|有非零解'的逆否命题是'|A|只有零解 \Rightarrow D只有零解'$

$参照(2)和(5)可知$

$
\begin{cases}
a_{11}k_{11}+\cdots +a_{1n}k_{1n}=0 \\
\cdots \\
a_{11}k_{n1}+\cdots +a_{1n}k_{nn}=0 \\
\cdots \\
\cdots \\
a_{n1}k_{11}+\cdots +a_{nn}k_{1n}=0 \\
\cdots \\
a_{n1}k_{n1}+\cdots +a_{nn}k_{nn}=0 \\
\end{cases}
$
$只有零解$

$\Leftrightarrow$

$
\begin{cases}
a_{11}k_{11}+\cdots +a_{1n}k_{1n}=0 \\
\cdots \\
a_{n1}k_{11}+\cdots +a_{nn}k_{1n}=0 \\
\cdots \\
\cdots \\
a_{11}k_{n1}+\cdots +a_{1n}k_{nn}=0 \\
\cdots \\
a_{n1}k_{n1}+\cdots +a_{nn}k_{nn}=0 \\
\end{cases}
$
$只有零解$

$\Leftrightarrow$

$对任意1\leq i\leq n 均有$
$
\begin{cases}
a_{11}k_{i1}+\cdots +a_{1n}k_{in}=0 \\
\cdots \\
a_{n1}k_{i1}+\cdots +a_{nn}k_{in}=0 \\
\end{cases}
$
$只有零解$

$\Leftrightarrow$

$|A^T|=|A|\neq 0成立$

---

$系数矩阵\begin{vmatrix}\alpha_1\alpha_1^T&\alpha_2\alpha_1^T&\cdots &\alpha_n\alpha_1^T\\\alpha_1\alpha_2^T&\alpha_2\alpha_2^T&\cdots &\alpha_n\alpha_2^T\\\vdots &\vdots & &\vdots \\\alpha_1\alpha_n^T&\alpha_2\alpha_n^T&\cdots &\alpha_n\alpha_n^T\end{vmatrix}对应的的线性方程组即为$

$\displaystyle\bigcap_{p=1}^n\bigcap_{q=1}^m\sum_{i=1}^n\sum_{j=1}^ma_{iq}a_{pj}k_{ij}=0$


$\displaystyle\bigcap_{p=1}^m\sum_{i=1}^na_{ip}k_i=0\rightarrow \forall k_i=0\rightarrow \bigcap_{i=1}^n k_i=0$
$\Rightarrow$
$\displaystyle\bigcap_{p=1}^n\bigcap_{q=1}^m\sum_{i=1}^n\sum_{j=1}^ma_{iq}a_{pj}k_{ij}=0\rightarrow \forall k_{ij}=0:$

$
\begin{aligned}
&\bigcap_{p=1}^n\bigcap_{q=1}^m\sum_{i=1}^n\sum_{j=1}^ma_{iq}a_{pj}k_{ij}=0 \\
\Leftrightarrow&\bigcap_{p=1}^n\bigcap_{q=1}^m\sum_{i=1}^na_{iq}\sum_{j=1}^ma_{pj}k_{ij}=0 \\
\Rightarrow&\bigcap_{p=1}^n\bigcap_{i=1}^n\sum_{j=1}^ma_{pj}k_{ij}=0  \qquad(带入已知)\\
\Leftrightarrow&\bigcap_{i=1}^n\bigcap_{p=1}^n\sum_{j=1}^ma_{pj}k_{ij}=0 \\
\Leftrightarrow&\bigcap_{i=1}^n\bigcap_{p=1}^n\sum_{j=1}^na_{pj}k_{ij}=0 \qquad(n=m)\\
\Leftrightarrow&\bigcap_{i=1}^n\bigcap_{p=1}^n\sum_{j=1}^na_{jp}k_{ij}=0 \qquad(转置)\\
\Rightarrow&\bigcap_{i=1}^n\bigcap_{j=1}^nk_{ij}=0 \qquad(带入已知)\\
\Rightarrow&\forall k_{ij}=0 \qquad(带入已知)\\
\end{aligned}
$

$\displaystyle\bigcap_{p=1}^m\sum_{i=1}^na_{ip}k_i=0\rightarrow \exist k_i\neq 0$
$\Rightarrow$
$\displaystyle\bigcap_{p=1}^n\bigcap_{q=1}^m\sum_{i=1}^n\sum_{j=1}^ma_{iq}a_{pj}k_{ij}=0\rightarrow \exist k_{ij}\neq 0:$

$
\begin{aligned}
&\bigcap_{p=1}^n\bigcap_{q=1}^m\sum_{i=1}^n\sum_{j=1}^ma_{iq}a_{pj}k_{ij}=0 \\
\Leftrightarrow&\bigcap_{p=1}^n\bigcap_{q=1}^m\sum_{j=1}^m\sum_{i=1}^na_{iq}a_{pj}k_{ij}=0 \\
\Leftrightarrow&\bigcap_{p=1}^n\bigcap_{q=1}^m\sum_{j=1}^ma_{pj}\sum_{i=1}^na_{iq}k_{ij}=0 \\
\end{aligned}
$

$带入\exist k_i\neq 0, 可知\exist k_{ij}\neq 0使得方程组成立$

# 六

## (1)

$
\begin{aligned}
PQ
&=\begin{bmatrix}E&O\\-\alpha^TA^*&|A|\end{bmatrix}\begin{bmatrix}A&\alpha\\\alpha^T&b\end{bmatrix}=\begin{bmatrix}A&\alpha\\O&|A|(b-\alpha^TA^*\alpha)\end{bmatrix} \\
\end{aligned}
$

## (2)

$\because |PQ|=|P||Q|=|A|^2|b-\alpha^TA^*\alpha|, |P|=|A|\neq 0$

$\therefore 充要条件是\alpha^TA^{-1}\alpha\neq b$