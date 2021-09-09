# 不知道第几次测试

## 题目: 打印等腰三角形

题目描述:

输入一个整数h, 打印由"*"组成的高为h的等腰三角形.

样例输入:

```
4
```

样例输出:

```
   *
  ***
 *****
*******
```

代码实现:

``` python
n = int(input())

for i in range(1, n + 1):
    print((n - i) * ' ' + (2 * i - 1) * '*')
```

## 题目：整数选择

题目描述：

对于一个十进制的正整数，定义函数f(n)为其各位数字的平方和，如：f(13) = 1 ** 2 + 3 ** 2 = 13，f(207) = 2 ** 2 + 0 ** 2 + 7 ** 2 = 53。

下面给出3个正整数：k、a、b，你需要计算有多少个正整数n满足a<=n<=b，且k*f(n)=n，并且需要从小到大以列表的形式输出这些正整数。

此外，你需将输出结果 (从小到大顺序排列) 分为奇数数组和偶数数组，若两者长度不一致则需将短数组后面填充0补全，然后将两个等长数组按位相加并输出相应的结果(以列表形式输出)。

输入：

第一行包括3个正整数k、a、b(k>=1，a、b<=10**18且a<b)

输出：

输出第一行为满足条件的整数个数，第二行为满足条件的整数，第三行为奇偶数组按位相加的结果

样例输入：

```
51 5000 10000
```

样例输出：

```
3
[7293, 7854, 7905]
[15147, 7905]
```

代码实现:

``` python
def f(n: int):
    sum = 0
    while n != 0:
        digit = n % 10
        sum += digit ** 2
        n = n // 10
    return sum

k, a, b = [int(v) for v in input().strip().split()]

lst = []
for n in range(a, b + 1):
    if k * f(n) == n:
        lst.append(n)

print(len(lst))
print(lst)

odd_lst = [v for v in lst if v % 2 == 1]
even_lst = [v for v in lst if v % 2 == 0]

if len(odd_lst) > len(even_lst):
    even_lst += (len(odd_lst) - len(even_lst)) * [0]
elif len(odd_lst) < len(even_lst):
    odd_lst += (len(even_lst) - len(odd_lst)) * [0]

print([odd_lst[i] + even_lst[i] for i in range(len(odd_lst))])
```


## 题目：用函数装饰函数

题目描述：

请你实现两个函数：mean和mean_decorator，可以使用mean函数计算数据的平均值，用mean_decorator函数装饰mean函数，输出传入mean函数的参数的相关信息。

mean函数的形参包括可变参数和一个关键字参数：其中可变参数为个数不定的一些数字；关键字参数type决定以何种方式计算平均值，当type为'ari'时，计算算数平均数；当type为'geo'时，计算几何平均数。在计算得到结果后，保留两位小数，打印输出。

mean_decorator函数负责装饰mean函数，其接收mean函数作为参数。对于被装饰的mean函数(指参考样例中的mean_func_dec)，它可以和mean函数接收相同形式的参数，并在执行mean函数前，打印可变参数的总数目和关键字参数(以空格分开)。

请按以下模版提交代码：

``` python
# 请在下面填写你的代码

# 请不要改动以下的测试代码
exec(input()) 
```

样例输入：

```
mean_func_dec = mean_decorator(mean); mean_func_dec(1, 2, 3, type='ari')
```

样例输出：

```
3 ari
2.00
```

代码实现:

``` python
from functools import reduce


def mean_decorator(func):
    def mean_decorator_func(*args, **kwargs):
        print(len(args), *kwargs.values())
        func(*args, **kwargs)

    return mean_decorator_func


def mean(*args, type: str):
    if type == 'ari':
        print('%.2f' % (sum(args) / len(args)))
    elif type == 'geo':
        print('%.2f' % (reduce(lambda a, b: a * b, args)) ** (1 / len(args)))

exec(input())
```