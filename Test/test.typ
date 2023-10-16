#import "../Typst/typst-sympy-calculator.typ": *

#set text(24pt)

#let add = math.op("+")
#hidden[
```typst-calculator
@additive_op()
def convert_add(a, b):
    return a + b
```
]

$x + hat(alpha)$

$integral x dif x$

$sin pi/2 = 1$

$lim_(x -> oo) 1/x = 0$

$1 add 1$

$cmat(1, 2; 3, 4) = mat(1, 3; 2, 4)$

$sum_(j=1)^(n) binom(j - 1, j - m) =  binom(n, m)$

$integral_(0)^(z) lambda_1 e^(-lambda_1 x) lambda_2 e^(-lambda_2 (z - x)) dif x = \ cases((lambda_1 lambda_2 1 / (lambda_1 - lambda_2) (exp(lambda_1 z) - exp(lambda_2 z)) exp(-z (lambda_1 + lambda_2)), (lambda_1 != lambda_2)), (lambda_1 lambda_2 z exp(-lambda_2 z), top))$