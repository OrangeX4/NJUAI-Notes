# Problem Set 13

# Problem 1

A B


# Problem 2

$\because ea=ae=a$

$\therefore e\in N(a)$

$\therefore N(a)\neq \empty$

$对于\forall x\in N(a),$

$\because xa=ax$

$\therefore a^{-1}x^{-1}=x^{-1}a^{-1}$

$\therefore aa^{-1}x^{-1}a=ax^{-1}a^{-1}a$

$\therefore x^{-1}a=ax^{-1}$

$\therefore x^{-1}\in N(a)$

$对于\forall x,y\in N(a)$

$\because xa=ax, ya=ay$

$\therefore xay=axy, xya=xay$

$\therefore xya=axy$

$\therefore xy\in N(a)$

$\therefore N(a)是G的子群$


# Problem 3

$\because 单位元e\in H, xex^{-1}=xx^{-1}=e$

$\therefore e\in xHx^{-1}, xHx^{-1}\neq\empty$

$对于\forall a,b\in H, 有xax^{-1}, xbx^{-1}\in xHx^{-1}$

$\therefore xax^{-1}(xbx^{-1})^{-1}=xax^{-1}xb^{-1}x^{-1}=xab^{-1}x^{-1}, ab^{-1}\in H$

$\therefore xab^{-1}x^{-1}\in xHx^{-1}$

$\therefore xHx^{-1}是G的子群$


# Problem 4

$\because e\in H, e\in K$

$\therefore e\in H\cap K$

$对于\forall a,b\in H\cap K$

$\because H, K都是群$

$\therefore ab^{-1}\in H, ab^{-1}\in K$

$\therefore ab^{-1}H\cap K$

$\therefore H\cap K也是一个群, 且是H和K的子群$

$设H\cap K的阶为p$

$\therefore 由Lagrange定理可知, p|r,p|s$

$\because r和s互素$

$\therefore p=1$

$\therefore H\cap K为平凡群$

$\therefore H\cap K=\{e\}$

# Problem 5

$\because G中只有一个2阶元, 设为a$

$对\forall x\in G$

$若xax^{-1}=e, 则xa=x \Rightarrow a=e矛盾$

$\therefore xax^{-1}\neq e$

$\because (xax^{-1})^2=xax^{-1}xax^{-1}=xa ax^{-1}=xx^{-1}=e$

$\therefore xax^{-1}也是二阶元$

$\therefore xax^{-1}=a$

$\therefore xa=ax$

# Problem 6

$即需证, 若aH\cap bH\neq\empty, 则aH=bH$

$\because aH\cap bH\neq\empty$

$\therefore 有h_1,h_2\in H, 使得ah_1=bh_2$

$\therefore a=bh_2h_1^{-1}$

$\therefore 对于任意h\in H, ah=bh_2h_1^{-1}h\in bH$

$\therefore aH\subseteq bH$

$同理有bH\subseteq aH$

$\therefore aH=bH$

$\therefore 原命题得证$


# Problem 7

$令f:H\to Ha, f(h)=ha$

$若f非单射, 即存在h_1, h_2\in H,h_1\neq h_2, 使得f(h_1)=h_1a=f(h_2)=h_2a$

$\therefore h_1a=h_2a$

$\therefore 由消去律可知h_1=h_2, 与h_1\neq h_2矛盾$

$\therefore f为单射函数$

$\because |Ha|\leq |H|$

$\therefore 易知f为满射函数$

$\therefore H\approx Ha$

$同理可知 H\approx aH$

$\therefore H\approx Ha \approx aH$

$\therefore H的任意陪集的大小是相等的$


# Problem 8

$对于充分性:$

$\because b\in aH$

$\therefore \exist h\in H, b=ah$

$\therefore a^{-1}b=a^{-1}ah=h\in H$

$对于必要性:$

$\because a^{-1}b\in H$

$\therefore 假设a^{-1}b=h$

$\therefore aa^{-1}b=ah$

$\therefore \exist h\in H, b=ah$

$\therefore b\in aH$

