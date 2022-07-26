# 第七次测试

## 单身狗问题

一个大型的派对中来了很多客人, 其中有些客人是已婚的, 而有些客人是单身的. 本题请你从客人中找出落单的客人, 以便给予特殊关爱, 请注意即使有些客人是已婚的, 但若其伴侣没有参加派对, 我们也视其为落单客人. 

输入格式: 第一行为正整数N, 是已知夫妻的对数; 随后N行, 每行为一对夫妻的ID号, 每一个ID号为5位数字(从00000到99999), ID号之间有空格分隔;  之后给出一个正整数M, 表示参数派对的总人数;  随后一行为这M位客人的ID号, ID号用空格隔开. 

输出格式: 输出第一行为落单客人的总人数;  第二行为落单客人的ID号, 按ID号从小到大输出, 中间用空格隔开. 此外, 若无落单客人, 第二行输出为"have fun"

**样例输入:** 

```
3
11111 22222
33333 44444
55555 66666
7
55555 44444 10000 88888 22222 11111 23333
```

**样例输出:** 

```
5
10000 23333 44444 55555 88888
```

**代码实现:**

``` python
n = int(input())
couples = []
for i in range(n):
    couples.append([int(v) for v in input().split()])

m = int(input())
guests = [int(v) for v in input().split()]

single_dogs = []

def is_single_dog(guest):
    for couple in couples:
        if couple[0] == guest and couple[1] in guests:
            return False
        if couple[1] == guest and couple[0] in guests:
            return False
    return True

for guest in guests:
    if is_single_dog(guest):
        single_dogs.append(guest)

if len(single_dogs) > 0:
    print(len(single_dogs))
    print(' '.join([str(v) for v in sorted(single_dogs)]))
else:
    print(0)
    print('have fun')
```


## 击鼓传花

n个人按照顺时针顺序围成一圈, 每个人都有自己的随机正整数编号. 

一朵红花在这n个人手中传递 (从第一个人开始传递), 每次得到红花的人都会出列, 直到所有人都出列. 

假如当前持有红花的人是小明, 则小明先出列, 然后若小明的编号为偶数, 则红花将传递到小明顺时针方向的第m个人 (红花顺时针传递m步); 若小明的编号为奇数, 则红花将传递到小明逆时针方向的第m个人 (红花逆时针传递m步); 

输入两行, 第一行是n和m, 第二行是按照顺时针顺序每个人的编号 (即第二行的第一个数字代表顺时针第一个人的编号, 第二个数字代表顺时针第二个人的编号); 

请输出依次拿到红花的人的顺序. 

**输入:** 

```
5 1
1 2 3 4 5
```

**输出:** 

```
1 5 4 2 3
```

**代码实现:**

``` python
n, m = [int(v) for v in input().split()]
queue = [int(v) for v in input().split()]

index = 0
result = []
while len(queue) != 0:
    result.append(queue[index])
    if queue[index] % 2 == 0:
        del queue[index]
        # del 已经默认顺时针一步了
        index += m - 1
    else:
        del queue[index]
        index -= m
    if len(queue) > 0:
        index %= len(queue)
        
print(' '.join([str(v) for v in result]))
```


## 区块链

1.链表: 链表与作为顺序存储的数组(list)不同, 链表中的数据元素的逻辑顺序是通过链表中的指针链接(引用)次序实现的. 链表中每个节点通过引用指向链表中的下一个节点, 比如一个长度为3的链表: b2->b1->b0. 可以从链表的头节点依次访问链表中的每个元素. 

使用python实现一个简单的链表: 

``` python
class Block:
    def __init__(self, father_block, value):
        self.father_block = father_block
        self.value = value

b0 = Block(None,3)
b1 = Block(b0, 5)
b2 = Block(b1,2)
print("b2:",b2.value)
print("b1:",b2.father_block.value)
print("b0:",b2.father_block.father_block.value)
```

题目要求: 将"Block"改造为一个迭代器(实现"__iter__"和"__next__"方法), 以支持for循环遍历链表. 

迭代器的使用方法可以参考 https://www.runoob.com/python3/python3-iterator-generator.html

样例输入: 

```
b0 = Block(None,3)
b1 = Block(b0, 5)
b2 = Block(b1,2)
print([val for val in b2])
exit()
```

样例输出: 

```
[2, 5, 3]
```

2.区块链: 简单地讲, 区块链是一个能够防止篡改的链表. 在一个区块链中, 比如b2->b1->b0, 当我们保证头节点b2正确时, 任何对中间区块(b1和b0)的篡改都能够被察觉. 
实现方案: 我们在"Block"中额外增加一个成员"check_num", 每当一个新的块被连接到区块链上时, 为这个新的块计算一个"check_num". 
比如, 现在将区块b3连接到b2->b1->b0上:
(1)首先为b3设置引用, b3.father_block=b2
(2)然后为b3设置"check_num", b3.check_num=F(b2.check_num, b3.value)
其中, F是一个函数, 接受两个个整数并输出一个整数. 

在链b2->b1->b0中, 假设"b0.value=0, b1.value=1, b2.value=2", "b0.check_num=0", 函数F为加法, 则"b1.check_num=0+1=1, b2.check_num=1+2=3". 

现在更改b0或b1的"value"或"check_num"都将导致整个链校验错误. 
比如将"b0.value"改为1, 则"F(0,b0.value) = F(0,1) = 1 != b0.check_num = 0"

如果将"b0.check_num"改为1以满足校验, 那么b0与b1之间的校验又将被破坏, 从而保证任何篡改都能被检查. 

**题目要求:**

在 `Block.__init__` 中初始化 `check_num`, 使用加法实现函数F; 在"Block"实现"check"方法, 如果区块链校验正确, 返回"True", 否则返回"False". 

**样例输入:** 

```
b0 = Block(None,3)
b1 = Block(b0, 5)
b2 = Block(b1,2)
print(b2.check())
b1.value = 2
print(b2.check())
exit()
```

**样例输出:**

```
True
False
```

**具体实现:**

``` python
class Block:
    def __init__(self, father_block, value: int):
        self.father_block = father_block
        self.value = value
        self.current_block = self
        if self.father_block:
            self.check_num: int = self.father_block.check_num + self.value
        else:
            self.check_num: int = 0

    def __iter__(self):
        self.current_block = self
        return self

    def __next__(self):
        if self.current_block:
            value = self.current_block.value
            self.current_block = self.current_block.father_block
            return value
        else:
            raise StopIteration()

    def check(self):
        if not self.father_block:
            return True
        if self.father_block.check_num + self.value != self.check_num:
            return False
        return self.father_block.check()
        
# 测试用代码, 请不要改动
while True:
    exec(input())
```