# Cheat Sheet

$\displaystyle \sum_{k=0}^{\infty}\frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}x^{k}=\sum_{k=0}^{\infty}\binom{\alpha}{k}x^{k}=(1+x)^{\alpha}$

$\displaystyle \sum_{k=0}^{\infty}\binom{\alpha}{k}x^{k}=(1+x)^{\alpha}$

$\displaystyle \sum_{k=r}^{\infty}\binom{k-1}{r-1}x^{k-r}=(1-x)^{-r}$

$\displaystyle \sum_{k=r}^{\infty}\binom{k-1}{r-1}(1-x)^{k-r}=x^{-r}$

$\displaystyle \sum_{k=0}^{\infty}\frac{1}{q^{k}}=\frac{1}{1-\frac{1}{q}}=\frac{q}{q-1}$

$\displaystyle \sum_{k=0}^{\infty}\frac{\lambda^{k}}{k!}=e^{\lambda}$

$\displaystyle \sum_{k=0}^{\infty}(-1)^{k-1}\frac{x^{k}}{k}=\ln(1+x)$

$\displaystyle \sum_{k=1}^{\infty}nx^{n-1}=\frac{x}{(1-x)^{2}}$

从 $n+1$ 个元素中取出 $r$ 个元素, 可以分为两个方式的和: 选定一个元素 $x$, 第一种方式是从除 $x$ 以外的 $n$ 个元素中取出 $r$ 个元素, 第二种方式是先确定要选取 $x$, 然后从剩下的 $n$ 个元素中取出还需要的 $r-1$ 个元素:

$\displaystyle \binom{n+1}{r}=\binom{n}{r}+\binom{n}{r-1}$

从 $m+n$ 个人中挑出 $r$ 个人, 这件事我们可以分成几件事的和: 先从 $m$ 个人中挑 $i$ 个人, 再从 $n$ 个人中挑还需要的 $r-i$ 个人:

$\displaystyle \binom{m+n}{r}=\sum_{i=0}^{r}\binom{m}{i}\binom{n}{r-i}$

从 $N+1$ 个元素中随机取 $k+1$ 个元素, 等价于按所抽取 $k+1$ 个元素中最大元进行分类选取:

$\displaystyle \binom{n+1}{k+1}=\sum_{i=k}^{n}\binom{i}{k}=\sum_{i=k}^{n}\frac{i}{k}\binom{i-1}{k-1}$

$\displaystyle (n)_{k}= n\cdot (n-1)_{k-1}, \binom{n}{k}=\frac{n}{k}\cdot \binom{n-1}{k-1}$

$\displaystyle \sum_{k=0}^{n}\binom{n}{k}a^{k}b^{n-k}=(a+b)^{n}$

负二项分布, $X$ 为第 $r$ 次成功时进行的试验次数, 设 $q=1-p, k=t+r$, 根据泰勒展开式有

$\displaystyle p^{-r}=(1-q)^{-r}=\sum_{t=0}^{\infty}\binom{t+r-1}{r-1}q^{t}=\sum_{k=r}^{\infty}\binom{k-1}{r-1}(1-p)^{k-r}$

$\displaystyle \sum_{k=r}^{\infty}\binom{k+1-1}{r+1-1}(1-p)^{k-r}=p^{- (r + 1)}$