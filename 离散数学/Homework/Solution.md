# 2019-2020年第一学期人工智能学院离散数学期末考试试卷参考答案

# 一

$定义谓词:$

$C(x):x是猫$
$D(x):x是狗$
$R(x):x能抓住老鼠$
$将南大神兽记为n$

$则原题转换为证明:$

$
\begin{aligned}
&R(n) \\
&\forall x(C(x)\leftrightarrow R(x)) \\
&\underline{\forall x(D(x)\to \lnot R(x))} \\
\therefore \ 
&C(n)\land\lnot D(n)
\end{aligned}
$

#### 证明:

$
\begin{aligned}
&(1)\quad D(n)\to\lnot R(n) &(全称实例) \\
&(2)\quad R(n) &(前提) \\
&(3)\quad \lnot D(n) &(取拒式,由(1)(2)) \\
&(4)\quad C(n)\leftrightarrow R(n) &(全称实例) \\
&(5)\quad C(n)\rightarrow R(n)\land R(n)\rightarrow C(n) &(等价等值式, 由(4)) \\
&(6)\quad R(n)\rightarrow C(n) &(化简, 由(5)) \\
&(7)\quad C(n) &(假言三段论, 由(2)(6)) \\
&(8)\quad C(n)\land \lnot D(n) &(合取引入, 由(3)(7)) \\
\end{aligned}
$


# 二

$将这六个人作为图的六个点, 两个点相邻当且仅当对应的两个人认识$

$问题可转化为, 一个阶数为6的图或补图, 总有三个顶点构成回路$

#### 证明:

$对6阶图G中任意一个点u, 若该点的度数\deg(u)\leq 2,$
$则在补图\overline{G}中u的度数大于等于3$

$\therefore 我们可知任意点u在原图或者补图中度数必然大于等于3$

$设点u相邻的这3个点为v_1,v_2,v_3$

$若其中至少两点相邻, 设为v_1v_2, 那么uv_1v_2u形成了一条回路$

$若其中三点均不相邻,$
$那么对于它的补图来说这三个点是相邻的, 构成v_1v_2v_3v_1回路$

$\therefore 任何6个人中, 总有3个人相互认识或者相互不认识$


# 三



# 四

![](2021-01-03-23-55-04.png)

$对应为:$

| ← | → | ↑ | ↓ | ↔ | ↕ |
|---|---|---|---|---|---| 
|11 |01 |000|100|001|100|

$\therefore 2\times(31+19)+3\times(9+15+12+13)=247$

$\therefore 字符数为249或250个$