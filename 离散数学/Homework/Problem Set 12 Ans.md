# Problem Set 12

# Problem 1

(1) 构成半群, 独异点, 群

(2) 构成半群, 独异点, 群

(3) 构成半群, 不构成独异点, 群

(4) 构成半群, 不构成独异点, 群

(5) 构成半群, 独异点, 不构成群

(6) 构成半群, 独异点, 群


# Problem 2

## (1)

$易知x*y=x\in S, 即(S,*)满足封闭性, 构成一个代数系统$

$\because 对于\forall x,y,z\in S, 都有(x*y)*z=x*z=x, x*(y*z)=x*y=x$

$\therefore (x*y)*z=x*(y*z)$

$\therefore S关于*运算满足结合性$

$\therefore S关于*运算构成半群$

## (2)

$\because (S,*)是半群, 要成为独异点, 则需有单位元$

$假设\exist e\in S 对于\forall x\in S满足e*x=x*e=x$

$不妨设e=a, 若单位元e为b或c同理.$

$\therefore a*a=a, a为单位元对a满足$
$\quad a*b=a=b, b*a=b, a为单位元对b满足, 则需a=b$
$\quad a*c=a=c, c*a=c, a为单位元对c满足, 则需a=c$

$\therefore 称为独异点的条件是a=b=c$


# Problem 3

$易知a\circ b=a\in A, 即\langle A,\circ\rangle满足封闭性, 构成一个代数系统$

$\because 对于\forall a,b,c\in A, 都有(a\circ b)\circ c=a\circ c=a, a\circ (b\circ c)=a\circ b=a$

$\therefore (a\circ b)\circ c=a\circ (b\circ c)$

$\therefore A关于\circ 运算满足结合性$

$\therefore \langle A,\circ\rangle是一个半群$


# Problem 4

$\because x a x b a = x b c$

$\therefore 由左消去律可知 a x b a = b c$

$\therefore a^{-1} (a x b a) = a^{-1}(b c)$

$\therefore (a^{-1} a) x b a = a^{-1} b c$

$\therefore x (b a) = a^{-1} b c$

$\therefore 该方程在群G中仅有一个解$


# Problem 5

$\because a是群\langle G,\circ\rangle的幂等元$

$\therefore a\circ a=a$

$对于\forall x\in G,$

$\because a\circ x=(a\circ a)\circ x=a\circ (a\circ x)$

$\therefore 由左消去律得x=a\circ x$

$\therefore a是x的左单位元$

$\because x\circ a=x\circ (a\circ a)=(x\circ a)\circ a$

$\therefore 由右消去律得x=x\circ a$

$\therefore a也是x的右单位元$

$\therefore a是单位元$


# Problem 6

$(abc)^{n+1}=abcabc\cdots abc$

$当abc的阶有穷, 设为r$

$\therefore (abc)^{n+1}=a(bca)^nbc$

$\therefore abc=a(bca)^nbc$

$\therefore (bca)^n=e$

$\therefore bca阶有穷, 设为r', 可知r'|r$

$\therefore 同理 |bca|=r'时|abc|有穷为r, 有r|r'$

$\therefore |abc|=|bca|$

$同理可知 |abc|=|cab|$

$\therefore |abc|=|bca|=|cab|=r$

$当abc的阶无穷,$

$假设|bca|有穷, 由前面的论述可知会使|abc|有穷, 与|abc|无穷矛盾$

$\therefore |bca|无穷$

$同理可知|cab|无穷$

$\therefore |abc|=|bca|=|cab|=\infty$

$综上|abc|=|bca|=|cab|$


# Problem 7

$法一:$

$已知G为偶数阶群, 设阶数为2k$

$可知存在a\in G, a\neq e, 有a^{2k}=e$

$\because a^k\in G$

$\therefore (a^k)^2=a^{2k}=e$

$\therefore 存在二阶元a^k$

$法二:$

$已知G为偶数阶群, 设阶数为2k$

$对于a\in G, 若|a|>2, 则a\neq a^{-1}$

$若不然, 则a=a^{-1}, 从而a^2=e, |a|\leq 2与|a|>2矛盾$

$\therefore G中阶大于2的元素a与其逆a^{-1}成对出现, 所以个数是偶数个$

$\therefore G中阶小于等于2的元素a个数也是偶数个, 最少也有两个$

$\because 只有|e|=1$

$\therefore 必定存在一个元素a, 使得|a|=2$

# Problem 8

$对于一个不等于单位元e的元a, 可知它有逆元a^{-1},$
$且易知a^{-1}也不是单位元$

$当a\neq a^{-1}时, 令b=a^{-1}, 则满足ab=ba=e$

$当a=a^{-1}时,$

$则此时我们可知对于\forall a\in G, 都有a=a^{-1}$

$\therefore ab=(ab)^{-1}=b^{-1}a^{-1}=ba, 其中a,b\in G, a\neq b$

$\therefore G中存在非单位元a和b, a\neq b, 且ab=ba$

# Problem 9

|      | $1$  | $-1$ | $i$  | $-i$ |
| ---- | ---- | ---- | ---- | ---- |
| $1$  | $1$  | $-1$ | $i$  | $-i$ |
| $-1$ | $-1$ | $1$  | $-i$ | $i$  |
| $i$  | $i$  | $-i$ | $-1$ | $1$  |
| $-i$ | $-i$ | $i$  | $1$  | $-1$ |

$通过观察易知\langle S,*\rangle与\langle \mathbb{Z_4},\oplus_4\rangle同构$

$\therefore \langle S,*\rangle构成群$

# Problem 10

$对于充分性:$

$\because G为交换群$

$\therefore \forall a,b\in G, ab=ba$

$\therefore (ab)^2=abab=a(ba)b=a(ab)b=aabb=a^2b^2$

$对于必要性:$

$\therefore a^2b^2=aabb=(ab)^2=abab$

$\therefore a(ab)b=a(ba)b$

$\therefore ab=ba$

$\therefore G为交换群$