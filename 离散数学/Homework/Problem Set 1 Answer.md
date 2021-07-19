# Problem 1

## a)

$$
r \land \neg p
$$

## b)

$$
p \land q \land r
$$

## c)

$$
r \to (q \leftrightarrow p)
$$

## d)

$$
\neg q \land \neg p \land r
$$

## e)

$$
q \to (\neg r \land \neg p)
$$

## f)

$$
(p \land r) \to \neg q
$$


# Problem 2

|p |q |r |s |$p \to q$|$(p \to q)\to r$|$((p \to q)\to r)\to s$|
|--|--|--|--|---------|----------------|-----------------------|
|F |F |F |F |T        |F               |T                      |
|F |F |F |T |T        |F               |T                      |
|F |F |T |F |T        |T               |F                      |
|F |F |T |T |T        |T               |T                      |
|F |T |F |F |T        |F               |T                      |
|F |T |F |T |T        |F               |T                      |
|F |T |T |F |T        |T               |F                      |
|F |T |T |T |T        |T               |T                      |
|T |F |F |F |F        |T               |F                      |
|T |F |F |T |F        |T               |T                      |
|T |F |T |F |F        |T               |F                      |
|T |F |T |T |F        |T               |T                      |
|T |T |F |F |T        |F               |T                      |
|T |T |F |T |T        |F               |T                      |
|T |T |T |F |T        |T               |F                      |
|T |T |T |T |T        |T               |T                      |


# Problem 3

## a)

Jennifer和Teja不是朋友.

## b)

并非面包师说的一打有13个.

## c)

Abby没有每天发送100多条文本信息.

## d)

121不是一个完全平方数.


# Problem 4

## c)是命题, 命题为假. F

## e)是命题, 命题为假. F


# Problem 5

$a) \ F \qquad b) \ T \qquad c) \ T \qquad d) \ T$


# Problem 6

$a) \ F \qquad b) \ T \qquad c) \ T \qquad d) \ T \qquad e) \ T$


# Problem 7

## a)

选举还没有结果

## b)

选举已经有了结果, 或者选票已经计数完毕

## c)

选举还没有结果, 但是选票已经计数完毕

## d)

如果选票已经计数完毕, 那么选举就有了结果

## e)

如果选票还没计数完毕, 那么选举就还没有结果

## f)

如果选举还没有结果, 那么选票一定还没计数完毕

## g)

选举要有结果, 仅当选票计数完毕之时

## h)

选票还没计数完毕, 或者说, 虽然选票已经计数完毕, 但是选举还没有结果


# Problem 8

$$
e \leftrightarrow (a \land (b \lor (p \land r)))
$$

或

$$
e \leftrightarrow a \land (b \lor p \land r)
$$


# Problem 9

若定义:

* $p$: 第一扇门的房间里有美女
* $q$: 第二扇门的房间里有美女
* $r$: 第一扇门的房间里有老虎
* $s$: 第二扇门的房间里有老虎 

则题目转化为:

已知 $p \land s$ 与 $(p \land s) \lor (q \land r)$ 中只有一个为T, 求$p, q$的真值

解:

若 $p \land s = T$, 则 $(p \land s) \lor (q \land r)$ 必定也为T, 与题设不符, 舍去

若 $p \land s = F$,

要使 $(p \land s) \lor (q \land r) = T$

则要 $q \land r = T$

则要 $q = T$ 且 $r = T$

即 $q = T$

综上, 第二扇门背后是美女


# Problem 10

$$
\begin{aligned}
& \ \quad(p \lor q \lor r) \land (\neg p \lor \neg q \lor \neg r) \\
&= (p \lor q \lor r) \land (\neg (p \land q) \lor \neg r) &(德摩根律) \\
&= (p \lor q \lor r) \land \neg (p \land q \land r) &(德摩根律) \\
\end{aligned}
$$

若 $p, q, r$ 不同值时, $p \lor q \lor r = T, \quad \neg (p \land q \land r) = T, 则(p \lor q \lor r) \land \neg (p \land q \land r) = T$

若 $p, q, r = F$ 时, $p \lor q \lor r = F, \quad \neg (p \land q \land r) = T, 则(p \lor q \lor r) \land \neg (p \land q \land r) = F$

若 $p, q, r = T$ 时, $p \lor q \lor r = T, \quad \neg (p \land q \land r) = F, 则(p \lor q \lor r) \land \neg (p \land q \land r) = F$

则说明题目成立.