#import "../Typst/report-template.typ": *
#import "../Typst/typst-sympy-calculator.typ": *
#import "../Typst/tablex.typ": *

// #set heading(numbering: Numbering.with(first-level: "", "1.1"))
#show math.equation.where(block: true): it => display(it)

// apply the template
#show: report.with(
    par-indent: false,
    media: "screen",
    theme: "dark",
)

#let iff = "iff"
#let innerp(x, y) = $lr(angle.l #x, #y angle.r)$

= 第二章 数学背景知识

#image("images/2023-06-07-17-09-26.png", width: 60%)

+ 内积与范数
    - 线性空间 (向量空间, Vector Space): 集合 + 线性结构
        - 加法和数乘, 封闭性
        - 向量, 矩阵, 多项式
    - 度量空间 (Metric Space): 集合 + 拓扑结构 (距离函数)
        - 存在度量函数 $ d: V times V -> R $, 满足
            - $ d(x, y) >= 0 $ (非负性)
            - $ d(x, y) = 0 iff x = y$ (同一性)
            - $ d(x, y) = d(y, x) $ (对称性)
            - $ d(x, z) <= d(x, y) + d(y, z) $ (三角不等式)
    - 赋范向量空间 (Normed Vector Space): 向量空间 + 范数
        - 存在范数: $ norm(dot): V -> R $, 满足
            - $ norm(x) >= 0 $ (非负性), 且 $ norm(x) = 0 iff x = 0 $
            - $ norm(a x) = abs(a) norm(x), a in R $ (齐次性)
            - $ norm(x + y) <= norm(x) + norm(y), x, y in V $ (三角不等式)
        - 根据范数定义距离函数: $ d(x, y) = norm(x - y) $
    - 内积空间 (Inner Product Space): 向量空间 + 内积
        - 存在内积: $ innerp(1, 1): V times V -> R $, 满足
            - $ innerp(x, y) = overline(innerp(y, x)) $ (共轭对称性)
            - $ innerp(a x, y) = a innerp(x, y), innerp(x + y, z) = innerp(x, z) + innerp(y, z) $ (线性)
            - $ innerp(x, x) >= 0, x in V $ (非负性)
            - $ innerp(x, x) = 0 iff x = 0 $ (非退化)
        - 根据内积定义范数: $ norm(x) = sqrt(innerp(x, x)) $
        - 常用内积: $ innerp(x, y) = x^T y $, $ innerp(f(x), g(x)) = integral f(x)g(x) dif x $
        - 性质
            - $ innerp(x, y) <= abs(innerp(x, y)) <= norm(x) norm(y) $
            - $ (sum_(i=1)^(d) x_i y_i)^2 <= (sum_(i=1)^(d) x_i^2) lr((sum_(i=1)^(d) y_i^2)) $ (柯西不等式)
            - $ (integral f(x) g(x) dif x)^2 <= (integral f^2(x) dif x)(integral g^2(x) dif x) $


