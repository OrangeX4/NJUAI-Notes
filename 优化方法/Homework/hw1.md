<style>
.title-box {
    border-style: solid;
    border-width: 1px;
    padding: 16px;
    padding-bottom: 32px;
}
</style>

<div class="title-box">
    <div>
        <b style="float: left;">Optimization Methods</b>
        <b style="float: right;">Fall 2021</b>
    </div>
    <h1 style="text-align: center;">Homework 1</h1>
    <div>
        <span style="float: left;"><i>Instructor:</i> Lijun Zhang</span>
        <span style="float: right;"><i>Name:</i> 方盛俊, <i>StudentId:</i> 201300035</span>
    </div>
</div>

## Notice

- The submission email is: **zhangzhenyao@lamda.nju.edu.cn**.
- Please use the provided Latex file as a template.
- If you are not familiar with LaTeX, you can also use Word to generate a **PDF** file.


## Problem 1: Inequalities

**(a)**

由内积的性质我们可知 $\|x\|\|y\|\geqslant x\cdot y$

$\because \displaystyle \|x+y\|^{2}=\|x\|^{2}+2x\cdot y+\|y\|^{2}\leqslant \|x\|^{2}+2\|x\|\|y\|+\|y\|^{2}=(\|x\|+\|y\|)^{2}$

$\therefore \displaystyle \|x+y\|\leqslant \|x\|+\|y\|$

**(b)**

$\because \displaystyle \epsilon\|x\|^{2}+\frac{1}{\epsilon}\|y\|^{2}\geqslant 2\sqrt{\epsilon\|x\|^{2}\cdot \frac{1}{\epsilon}\|y\|^{2}}=2\|x\|\|y\|\geqslant 2x\cdot y$

$\therefore \displaystyle 2x\cdot y\leqslant \epsilon\|x\|^{2}+\frac{1}{\epsilon}\|y\|^{2}$

$\therefore \displaystyle \|x+y\|^{2}=\|x\|^{2}+2x\cdot y+\|y\|^{2}\leqslant (1+\epsilon)\|x\|^{2}+(1+\frac{1}{\epsilon})\|y\|^{2}$


## Problem 2: Convex sets

**(a)**

对于 $P$ 内的任意两个点 $x_1, x_2$, 我们有 $Ax_1\leqslant b$ 和 $Ax_2\leqslant b$

$\therefore A(\theta x_1+(1-\theta)x_2)=\theta Ax_1+(1-\theta)Ax_2\leqslant \theta b+(1-\theta)b=b$

$\therefore \theta x_1+(1-\theta)x_2\in P$

$\therefore$ $P$ 是一个凸集.

**(b)**

$\because S$ 是凸集.

$\therefore \forall x_1, x_2\in S, 0\leqslant \theta\leqslant 1$, 我们有 $\theta x_1+(1-\theta)x_2\in S$

$\therefore \forall Ax_1, Ax_2\in A(S), 0\leqslant \theta\leqslant 1$, 我们有 $A(\theta x_1+(1-\theta)x_2)=\theta Ax_1+(1-\theta)Ax_2\in A(S)$

因为由 $A(S)=\{Ax|x\in S\}$ 我们知道, $Ax_1$ 和 $Ax_2$ 可以是 $A(S)$ 里的任意一个元素, 我们用 $y_1, y_2$ 将其代换.

$\therefore \forall y_1, y_2\in A(S), 0\leqslant \theta\leqslant 1$, 我们有 $\theta y_1+(1-\theta)y_2\in S$

$\therefore A(S)$ 是凸集.

Correct:

有 $x_1\in S, x_2\in S$, 求证 $\theta Ax_1+(1-\theta)Ax_2\in A(S)$

**(c)**

$\because S$ 是凸集.

$\therefore \forall x_1, x_2\in S, 0\leqslant \theta\leqslant 1$, 我们有 $\theta x_1+(1-\theta)x_2\in S$

我们令 $x_1=Ay_1, x_2=Ay_2$ (对于存在 $y_1, y_2$ 满足该条件的情况)

$\therefore \forall Ay_1, Ay_2\in S, 0\leqslant \theta\leqslant 1$, 我们有 $\theta Ay_1+(1-\theta)Ay_2=A(\theta y_1+(1-\theta)y_2)\in S$

$\because A^{-1}(S)=\{x| Ax \in S\}$

$\therefore \forall y_1, y_2\in A^{-1}(S), 0\leqslant \theta\leqslant 1$, 我们有 $\theta y_1+(1-\theta)y_2\in A^{-1}(S)$

Correct:

有 $Ax_1\in S, Ax_2\in S$, 求证 $A(\theta x_1+(1-\theta)x_2)\in S$


## Problem 3: Hyperplane

我们先将两个超平面改写成 $\{x|a^{T}(x-x_1)=0\}$ 和 $\{x|a^{T}(x-x_2)=0\}$

即我们有 $b=a^{T}x_1, c=a^{T}x_2$

由超平面的几何意义, 以及点乘的几何意义: $a\cdot b$ 的几何意义是 $a$ 到 $b$ 的投影长度乘以 $b$ 的长度, 我们可知

距离 $\displaystyle d=\frac{\|a^{T}(x_1-x_2)\|}{\|a\|}=\frac{|a^{T}x_1-A^{T}x_2|}{\|a\|}=\frac{|b-c|}{\|a\|}$


## Problem 4: Examples

**(a)**

$\because A\succeq 0$

$\therefore 0\leqslant  (x_1-x_2)^{T}A(x_1-x_2)$

$\therefore 0\leqslant  x_1^{T}A(x_1-x_2)+x_2^{T}A(x_2-x_1)$

$\therefore x_2^{T}Ax_1+x_1^{T}Ax_2\leqslant  x_1^{T}Ax_1+x_2^{T}Ax_2$

$\therefore \theta(1-\theta)x_2^{T}Ax_1+\theta(1-\theta)x_1^{T}Ax_2\leqslant \theta(1-\theta) x_1^{T}Ax_1+\theta(1-\theta)x_2^{T}Ax_2$

$\therefore (\theta x_1+(1-\theta)x_2)^{T}A(\theta x_1+(1-\theta)x_2)\leqslant \theta x_1^{T}Ax_1+(1-\theta)x_2^{T}Ax_2$

$\because \forall x_1, x_2\in C, 0\leqslant \theta\leqslant 1$, 我们有 $x_1^{T}Ax_1+b^{T}x_1+c\leqslant 0, x_2^{T}Ax_2+b^{T}x_2+c\leqslant 0$

$\therefore (\theta x_1+(1-\theta)x_2)^{T}A(\theta x_1+(1-\theta)x_2)+b^{T}(\theta x_1+(1-\theta)x_2)+c\leqslant \theta(x_1^{T}Ax_1+b^{T}x_1+c)+(1-\theta)(x_2^{T}Ax_2+b^{T}x_2+c)=\theta x_1^{T}Ax_1+(1-\theta)x_2^{T}Ax_2+b^{T}(\theta x_1+(1-\theta)x_2)+c\leqslant 0$

$\therefore \theta x_1+(1-\theta)x_2\in C$

$\therefore C$ 是凸集

**(b)**

这个表述正确.

$C$ 和该超平面的交集为 $\{x\in \mathbb{R}^{n}|x^{T}Ax+b^{T}x+c\leqslant 0 \ \text{and} \ g^{T}x+h=0 \}$

$\because g^{T}x+h=0$

$\therefore \lambda x^{T}gg^{T}x=\lambda h^{2}, \lambda hg^{T}x=-\lambda h^{2}$

$\therefore \lambda x^{T}gg^{T}x+\lambda hg^{T}x=\lambda h^{2}-\lambda h^{2}=0$

$\therefore x^{T}Ax+b^{T}x+c=x^{T}Ax+b^{T}x+c+\lambda x^{T}gg^{T}x+\lambda hg^{T}x=x^{T}(A+\lambda gg^{T})x+(b^{T}+\lambda hg^{T})x+c$

即该交集可以表示为 $\{x\in \mathbb{R}^{n}|x^{T}(A+\lambda gg^{T})x+(b^{T}+\lambda hg^{T})x+c\leqslant 0\}\cap \{x \in \mathbb{R}^{n}|g^{T}x+h=0\}$

如果有 $A+\lambda gg^{T}\succeq 0$ 对于某些 $\lambda \in \mathbb{R}$, 由 (a) 的结论可知

$\{x\in \mathbb{R}^{n}|x^{T}(A+\lambda gg^{T})x+(b^{T}+\lambda hg^{T})x+c\leqslant 0\}$ 是凸集, 交上另一个凸集 $\{x \in \mathbb{R}^{n}|g^{T}x+h=0\}$, 结果还是凸集.

所以该表述正确.


## Problem 5: Generalized Inequalities

**(a)**

$\because \displaystyle K^*=\{y|x^{T}y\geqslant 0, \forall x\in K\}$

$\therefore \forall y_1, y_2\in S$, 我们有 $x^{T}y_1\geqslant 0, x^{T}y_2\geqslant 0$, 对于 $\forall x\in K$

$\therefore 0\leqslant \theta\leqslant 1$, 我们有 $\theta x^{T}y_1+(1-\theta)x^{T}y_2=x^{T}(\theta y_1+(1-\theta)y_2)\geqslant 0$

$\therefore \theta y_1+(1-\theta)y_2\in K^*$

$\therefore K^*$ 是一个凸锥.

**(b)**

$\because K^*=\{y|x^{T}y\geqslant 0, \forall x\in K\}$

$\therefore K_2^*=\{y|x^{T}y\geqslant 0, \forall x\in K_2\}$

$\therefore$ 对于 $\forall x \in K_2$, 我们都有 $y\in K_2^*\Rightarrow x^{T}y\geqslant 0$

$\because K_1\subseteq K_2$

$\therefore$ 对于 $\forall x \in K_1$, 我们都有 $y\in K_2^*\Rightarrow x^{T}y\geqslant 0$

$\because K_1^*=\{y|x^{T}y\geqslant 0, \forall x\in K_1\}$

$\therefore$ 对于上文出现过的 $y$ 都有 $y\in K_1^*$

$\therefore K_1^*\subseteq K_2^*$
