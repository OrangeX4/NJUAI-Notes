# 习题课

## Exercise 1

试用一阶语言将以下的推理符号化, 并试用系统 $G$ 给出形式证明:

所有的狗都不吃鱼. 没有一只猫不吃鱼. 故没有一只狗是猫.

**解:**

先进行形式化:

设一元谓词 $d(x)$ 指 $x$ 为狗. $c(x)$ 指 $x$ 为猫. $e(x)$ 指 $x$ 吃鱼.

所有的狗都不吃鱼: $\forall x(d(x)\to \lnot e(x))$

没有一只猫不吃鱼: $\lnot \exists x(c(x)\to e(x))$

没有一只狗是猫: $\lnot \exists x(d(x)\land c(x))$

即要推导 $\forall x(d(x)\to \lnot e(x)), \lnot \exists x(c(x)\to e(x))\vdash \lnot \exists x(d(x)\land c(x))$

使用 G 系统推出证明树即可

$\displaystyle \frac{\cdots}{\forall x(d(x)\to \lnot e(x)), \lnot \exists x(c(x)\to e(x))\vdash \lnot \exists x(d(x)\land c(x))}$


## Exercise 2

证明任何协调集都可以拓展成为最大协调集.

**证明:**

假设所有公式组成的集合为 $\{A_1, A_2, \cdots \}$, $\mathcal{L}$ 的任意一个协调公式集为 $\Gamma$, 下面证其可以扩张为一个极大协调公式集 $\Gamma'$.

进行数学归纳:

**奠基 (Basic):** 当 $n=0$ 时, $\Gamma_0=\Gamma$, 易知 $Con(\Gamma_0)$

**归纳假设 (I.H.):** 假设当 $n-1$ 时, 有 $Con(\Gamma_{n-1})$

**归纳步骤 (I.S.):**

由归纳假设可知 $Con(\Gamma_{n-1})$

若 $Con(\Gamma_{n-1}\cup\{A_n\})$, 则令 $\Gamma_{n}=\Gamma_{n-1}\cup\{A_n\}$

若 $Incon(\Gamma_{n-1}\cup\{A_n\})$, 则令 $\Gamma_{n}=\Gamma_{n-1}$

所以可知 $Con(\Gamma_{n})$

归纳成立.

令 $\Gamma'=\Gamma_0\cup\Gamma_1\cup\Gamma_2\cup\cdots\cup\Gamma_{n}\cup\cdots$

**下面证明 $\Gamma'$ 极大协调.**

由归纳的步骤我们可知, 对于任何一个公式 $A_{n}$:

$Con(\Gamma'\cup \{A_{n}\})\Rightarrow Con(\Gamma_{n-1}\cup \{A_{n}\})\Rightarrow A_{n}\in \Gamma_{n}\Rightarrow A_{n}\in \Gamma'$

即对任何公式 $A$ 均有若 $Con(\Gamma'\cup\{A\})$ 则 $A\in \Gamma'$

所以 $\Gamma'$ 极大协调, 即

一阶语言 $\mathcal{L}$ 的一个协调公式集 $\Gamma$ 均可扩张为 $\mathcal{L}$ 的一个极大协调公式集 $\Gamma'$.


## Exercise 3

$\Gamma=\{\lnot(x\doteq S^{n}(0))|n\in\mathbb{N}\}$

### (1)

证明 $\Gamma$ 在标准算术模型中不可满足.

**证明:**

反设 $M\models_{\sigma} \Gamma$

设 $k=\sigma(x)\in \mathbb{N}, N=\{\mathbb{N}, 0\}$

从而 $k\neq n$ 对于 $\forall n\in \mathbb{N}$, 产生矛盾.


### (2)

证明 $\Gamma$ 可满足.

**证明:**

设 $S$ 为 $\Gamma$ 的任意一个有穷子集

从而可设 $S\subseteq \{\lnot(x\doteq S^{n}(0))|n\leqslant k\}$, 其中 $k\in \mathbb{N}$

令 $\sigma(x)=k+1$ 从而 $M\models_{\sigma}S$, 从而可满足.

由紧性定理可知, $\Gamma$ 可满足.


## Exercise 4

用一阶语言描述极限存在的定义.


## Exercise 5

证明 $\forall xP(x,x), \forall xyz(P(x,y)\land P(y,z)\to P(x,y))\vdash \forall x\forall y(P(x,y)\to P(y,z))$ 不可证.

构造模型 $M=(\{0,1\}, \leqslant)$

显然这个模型不能使该矢列满足, 则该矢列不可证.

## Exercise 6

证明若一阶语言句子集 $Σ$ 具有论域基数可为任意大自然数的模型, 
则 $Σ$ 具有一个论域为无穷集的模型.

**证明:**

令 $\displaystyle \varphi_n \triangleq \exists x_1,...,x_n. \bigwedge_{1\leq i < j\leq n} \neg (x_i \doteq x_j)$

易见 $\mathfrak{M} \models \varphi_n \Leftrightarrow |M|\geq n$

$\mathfrak{M} \models \{ \varphi_i | i\in \mathbb{N}^+ \} \Leftrightarrow |M|\geq \aleph_0$

令 $\Gamma \triangleq \Sigma \cup \{ \varphi_i | i \in \mathbb{N}^+ \}$, 对于任何 $\Gamma$ 的

有穷子集 $\Delta \subseteq \Sigma \cup \{ \varphi_i | i  \in \mathbb{N}^+ \}$, 存在 $k$ 使

$\Delta \subseteq \Sigma \cup \{ \varphi_1 ,..., \varphi_k\}$,

由于 $\Sigma$ 具有论域基数大于 $k$ 的模型, 故 $\Delta$ 可满足,

由紧致性定理知 $\Gamma$ 可满足, 那么有, $\mathfrak{M}\vDash \Gamma$

从而 $\mathfrak{M} \vDash \{ \varphi_i | i  \in \mathbb{N}^+\}$, 故 $|M|\geq \aleph_0$.


## Exercise 7

证明 $\models \exists x\forall yP(x,y)\to \forall y\exists xP(x,y)$.

**证明:**

设 $\mathfrak{M}$ 为任何模型.

$\mathfrak{M}\models \exists x\forall yP(x,y)$,

存在 $a\in M$ 对任何 $b\in M$ 有 $\left<a,b\right>\in P_{\mathfrak{M}}$

$\Rightarrow$

对任何 $b$ 存在 $a$ (取上面的 $a$) 使得

$\left<a,b\right>\in P_{\mathfrak{M}}\Rightarrow \mathfrak{M}\models\forall y\exists xP(x,y)$

**另一种证法:**

要证 $\models \exists x\forall yP(x,y)\to \forall y\exists xP(x,y)$, 由 Completeness 知

只需证 $\vdash \exists x\forall yP(x,y)\to \forall y\exists xP(x,y)$

$$
\begin{aligned}
\frac{\displaystyle \frac{\displaystyle \frac{\displaystyle \frac{\displaystyle \frac{P(t,u), \forall yP(t,y)\vdash P(t,u), \exists xP(x,u)}{P(t,u), \forall yP(t,y)\vdash\exists xP(x,u)}\exists R}{\forall yP(t,y)\vdash\exists xP(x,u)}\forall L}{\forall yP(t,y)\vdash\forall y\exists xP(x,y)}\forall R}{\exists x\forall yP(x,y)\vdash\forall y\exists xP(x,y)}\exists L}{\vdash \exists x\forall yP(x,y)\to \forall y\exists xP(x,y)}\to R \\
\end{aligned}
$$

$\therefore\ \vdash \exists x\forall yP(x,y)\to \forall y\exists xP(x,y)$

$\therefore\ \models \exists x\forall yP(x,y)\to \forall y\exists xP(x,y)$


## Exercise 8

证明 $\not\models \forall x\exist yP(x,y)\to \exist y\forall xP(x,y)$.

**证明:**

构造模型 $\mathfrak{M}=(\mathbb{N},<), P_{M}=\{(a.b)|a<b\}$

即可证明其不满足.


## Exercise 9

只需证每个有穷图可 $4$ 色则无穷图可四色.

设 MAP 为一张无穷地图, 令全体国家的集合为

$\{a_i |i\in I\}$, 这里 $|I|\geq \aleph_0$.

设一阶语言 $\mathcal{L}$ 由以下构成

1. 常元: $\{a_i | i\in I\}$
2. 一元谓词符: $C_k (x) (k=1,2,3,4)\quad(C_k (x)$表示$x$着$k$色)
3. 二元谓词符: $q(x,y)\quad(q(x,y)$ 表示 $x$ 与 $y$ 有大于 $0$ 的公共边界).

令 $Q \triangleq \{<i,j>|i,j\in I\}$ 且在 MAP 中 $a_i$ 与 $a_j$ 有大于 $0$ 的公共边界.

令 $\Gamma \triangleq \{q(a_i,a_j) | <i,j> \in Q\}$
$\qquad\cup \{\neg q(a_i,a_j) | <i,j> \notin Q\}$
$\qquad\cup\{ \forall x(c_1(x)\vee c_2(x)\vee c_3(x)\vee c_4(x))\}$
$\qquad\cup\{ \forall x \forall y (q(x, y)\rightarrow (\neg (c_1(x)\wedge c_1(y))  \wedge \neg(c_2(x)\wedge c_2(y))\wedge \neg(c_3(x)\wedge c_3(y))\wedge \neg(c_4(x)\wedge c_4(y))))\}$

设 $S\subseteq \Gamma$ 为 $\Gamma$ 的任何有穷子集, 不妨设 $\{a_0,...,a_n\}$

为出现在 $S$ 中的全体常元, 令 $M=\{a_0,...,a_n\}, MAP[s]$ 为 $\{a_0,\dots,a_n\}$ 的生成子图. 从而 $MAP[s]$ 可着 $4$ 色. 

令 $(C_{k})_\frak{M} \triangleq \{a_i|a_i$ 着 $k$ 色 $i\leq n\}, k=1,2,3,4$

$q_\frak{M} =\{<a_i,a_j>|<i,j>\in Q\}$ 从而 $\mathfrak{M} \vDash S$

由 compactness 知有 $\mathfrak{M}$ 使 $\mathfrak{M}\vDash \Gamma$即 $MAP$ 可 $4$ 染色.


PS: Exercise 6 和 Exercise 9 的证明来源于网络.

