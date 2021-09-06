# 第五次测试

## 题目: [Python]多项式运算

### 题目描述: 

输入两个多项式, 计算两个多项式的和差积. 输入多项式时, 首先输入多项式项的数量t, 然后接下来输入t行, 每一行有两个数字（由一个空格分隔）, 第一个数字表示指数, 第二个数字表示系数. 例如样例输入的第一个多项式表示 $4x^2 + 3x + 5$, 第二个多项式表示 $2x^3+x^2+6x+2$. 输出多项式时, 按照指数由大到小, 输出系数非0的项. 每项一行, 输出两个数字（由一个空格分隔）, 第一个数字表示指数, 第二个数字表示系数. 例如样例输出的前四行表示两个输入多项式的和为 $2x^3+5x^2+9x+7$, 五到八行表示两个多项式之差, 九到十四行表示两个多项式之积. 本题输入多项式指数最多为9. 

### 样例输入: 

```
3
1 3
2 4
0 5
4
3 2
2 1
1 6
0 2
```

### 样例输出: 

```
3 2
2 5
1 9
0 7
3 -2
2 3
1 -3
0 3
5 8
4 10
3 37
2 31
1 36
0 10
```

### 代码实现:

``` python
a = [0] * 10
b = [0] * 10

a_len = int(input())
for i in range(a_len):
    item = [int(v) for v in input().split()]
    a[item[0]] = item[1]

b_len = int(input())
for i in range(b_len):
    item = [int(v) for v in input().split()]
    b[item[0]] = item[1]

sum = [a[i] + b[i] for i in range(10)]
sub = [a[i] - b[i] for i in range(10)]
prod = [0] * 20

for i in range(10):
    for j in range(10):
        prod[i + j] += a[i] * b[j]

def print_it(lst: list):
    for i in reversed(range(len(lst))):
        if lst[i] != 0:
            print(i, lst[i])

print_it(sum)
print_it(sub)
print_it(prod)
```

## 题目: [python] 搜索前缀

### 题目描述: 

任意输入一段纯英文的语句s, 并输入n(n>1)个检索词w, 请你先根据n个检索词获取它们对应的最长公共前缀prefix, 之后检查prefix是否为句子s中任意单词的前缀, 如果prefix是语句s中任意一个单词的前缀, 则输出句子s中该单词对应的下标, 请注意语句中单词的下标是从1开始的；此外, 若prefix是语句s中多个单词的前缀, 则输出匹配的语句s中第一个单词的下标；若prefix不是语句s中任意一个单词的前缀, 则输出-1；最后, 若n个检索词中不存在最长公共前缀prefix, 不需要再去查找prefix是否为语句s中任意单词的前缀, 直接输出-2即可. 

**提示:** 

1. 纯英文语句是指语句中仅有英文单词, 且输入语句s和检索词w均小写；
2. 输入第一行为语句s, 第二行为n个检索词, 检索词之间用空格隔开. 

### 样例输入: 

```
it is impossible to believe this immoral things
impartial impart imcredible
```

### 样例输出: 

```
3
```

### 代码实现:

``` python
words = input().split()
searchs = input().split()

if len(words) == 0:
    print(-1)

if len(searchs) == 0:
    print(-2)

prefix = searchs[0][0]

def is_prefix(index):
    current = searchs[0][index]
    _is_prefix = True
    for search in searchs:
        if search[index] != current:
            _is_prefix = False
            break
    return _is_prefix

if not is_prefix(0):
    print(-2)
    exit()

def safe(index):
    is_safe = True
    for search in searchs:
        if len(searchs[0]) <= index:
            is_safe = False
            break
    return is_safe

index = 1
while safe(index) and is_prefix(index):
    prefix += searchs[0][index]
    index += 13

index = -1
for i in range(len(words)):
    if words[i][:len(prefix)] == prefix:
        index = i + 1
        break

print(index)
```


## 题目: [Python]小小空间大大世界2

### 题目描述: 

在计算机中, 所有的量都是有限的, 然而在数学上, 许多量都以无穷的形式出现, 那么如何在有限的空间中表达出无穷的性质呢. 
在Python中, 可以通过range函数得到一个整数序列, 并且可以通过for循环遍历它. 你需要实现一个类"InfSequence", 它是一个有穷序列, 也可以是一个无穷序列. 利用Python的迭代器, 可以实现通过for循环或__next__方法遍历该序列的所有值. 

### 接口定义: 

``` python
InfSequence.__init__(self,start,end,step:int=1)
    start: 整数, 表示序列的初值. 
    end: 整数, 表示序列的结束值（不包括）, 如果是字符串"inf", 则表示为无穷, 如果是字符串"-inf", 则表示为负无穷. 
    step: 整数, 表示步长, 如果step>0, 那么要求start<=end, 如果step<0, 那么要求start>=end, 如果step=0, 且start!=end, 此时InfSequence是所有项均为start的无穷序列. 

InfSequence.__iter__(self)
    迭代器要求实现的方法, 见参考资料. 
InfSequence.__next__(self)
    迭代器要求实现的方法, 见参考资料. 
```

迭代器的使用方法可以参考 https://www.runoob.com/python3/python3-iterator-generator.html

**注意: 请在以下模板中填写代码, 然后复制到OJ中提交.** 

``` python
# 在此处填写代码
# your code here

# 测试用代码, 请不要改动
while True:
    exec(input())
```

### 样例输入: 

``` python
s1 = InfSequence(start=2, end="inf", step=1)
exec_str = "for value in s1:\n    print(value)\n    if value==5:\n        break"
exec(exec_str)
print("----")
s2 = InfSequence(start=2, end=5)
exec_str = "for value in s2:\n    print(value)"
exec(exec_str)
exit()
```

### 样例输出: 

```
2
3
4
5
----
2
3
4
```

### 代码实现:

``` python
class InfSequence:

    def __init__(self, start, end, step: int = 1):
        self._start = start
        self._end = end
        self._step: int = step
        self._current = start - step

    def __iter__(self):
        return self
    
    def __next__(self):
        self._current += self._step
        if self._step == 0 and self._start == self._end:
            raise StopIteration
        elif self._step == 0 and self._start != self._end:
            return self._current
        elif self._step > 0:
            if self._end == 'inf':
                return self._current
            elif self._end == '-inf':
                raise StopIteration
            elif self._current < self._end:
                return self._current
            else:
                raise StopIteration
        else:
            if self._end == '-inf':
                return self._current
            elif self._current > self._end:
                return self._current
            else:
                raise StopIteration


while True:
    exec(input())
```