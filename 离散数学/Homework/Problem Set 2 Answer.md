# Problem 1

* a) 化简
* b) 析取三段式
* c) 假言三段论
* d) 附加
* e) 假言三段论

# Problem 2

$$
\begin{aligned}
    &p \leftrightarrow q \\
    &\underline{q \leftrightarrow r} \\
    \therefore \ &p \leftrightarrow r
\end{aligned}
$$

# Problem 3

$$
\begin{aligned}
    &(p \to q) \to r \\
    \equiv&\lnot(\lnot p \lor q) \lor r \\
    \equiv&(p \land \lnot q) \lor r
\end{aligned}
$$
$$
\begin{aligned}
    &p \to (q \to r) \\
    \equiv&\lnot p \lor (\lnot q \lor r) \\
    \equiv&(\lnot p \lor \lnot q) \lor r \\
\end{aligned}
$$

因为

|p |q |$p \land \lnot q$|$\lnot p \lor \lnot q$ |
|--|--|--|--|
|F |F |F |T |
|F |T |F |T |
|T |F |T |T |
|T |T |F |F |

$$
p \land \lnot q \not \equiv \lnot p \lor \lnot q
$$

所以

$$
(p \to q) \to r \not \equiv p \to (q \to r)
$$

# Problem 4

$$
\begin{aligned}
    &(p \to q) \to (r \to s) \\
    \equiv&\lnot(\lnot p \lor q) \lor (\lnot r \lor s) \\
    \equiv&(p \land \lnot q) \lor \lnot r \lor s \\
    \equiv&(p \lor \lnot r) \land (\lnot q \lor \lnot r) \lor s \\
\end{aligned}
$$
$$
\begin{aligned}
    &(p \to r) \to (q \to s) \\
    \equiv&\lnot(\lnot p \lor r) \lor (\lnot q \lor s) \\
    \equiv&(p \land \lnot r) \lor \lnot q \lor s \\
    \equiv&(p \lor \lnot q) \land (\lnot q \lor \lnot r) \lor s \\
\end{aligned}
$$
因为
$$
r \not \equiv q
$$

所以

$$
(p \to q) \to (r \to s) \not \equiv (p \to r) \to (q \to s)
$$

# Problem 5

## a)

|p |q |$(p\lor \lnot q)\land (\lnot p \lor q)\land(\lnot p \lor \lnot q)$ |
|--|--|--|
|F |F |T |
|F |T |F |
|T |F |F |
|T |T |F |

所以该式是可满足的.

## b)

当$p=F, q=F,r=F$时, 该式为$T$, 说明该式是可满足的.

## c)

该式包含了$p, q, s$三个命题所组成的所有八个析取式,  

且这八个析取式不同时为T,  

所以这八个析取式组成的合取范式不可能为T,

所以该式是不可满足的.

# Problem 6

即判断$((p \to r) \land (q \to r) \land (p \lor q)) \to \lnot r$是否为重言式.

|p |q |r |$((p \to r) \land (q \to r) \land (p \lor q)) \to \lnot r$ |
|--|--|--|--|
|F |F |F |T |
|F |F |T |T |
|F |T |F |T |
|F |T |T |F |
|T |F |F |T |
|T |F |T |F |
|T |T |F |T |
|T |T |T |F |

因为该式不是重言式, 所以原论证无效.

# Problem 7

定义$p$: 天下雨.  

定义$q$: 天起雾.

定义$r$: 帆船比赛举行.

定义$s$: 救生表演进行.

定义$t$: 比赛颁发奖杯.

则原题转换为证明: 

$$
\begin{aligned}
    &\lnot t \\
    &r \to t\\
    &\underline{\lnot p \lor \lnot q \to r \land s } \\
    \therefore \ &p
\end{aligned}
$$

## 证明:

(1) $\lnot t$ (前提)

(2) $r \to t$ (前提)

(3) $\lnot r$ (拒取式, 由(1)(2))

(4) $\lnot p \lor \lnot q \to r \land s$ (前提)

(5) $\lnot p \lor \lnot q \to r$ (化简, 自(1))

(6) $p \land q$ (拒取式, 由(3)(5))

(7) $p$ (化简, 由(6))