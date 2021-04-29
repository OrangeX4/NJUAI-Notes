# 测试

## [Python]找出丢失的数字

题目描述：

输入一个n个不相同的整数（以空格分隔），其中每个数都在[1,n+1]内，输出[1, n+1]内没有出现在输入中的那个整数，不要输出额外的空格和换行。

样例输入：
```
6 5 3 1 2
```

样例输出：
```
4
```

实现:
``` python
inputs = [int(v) for v in input().split()]

print(*set(range(1, len(inputs) + 2)) - set(inputs))
```


## [Python] 快递管理系统

题目描述：

本题要求你实现一个快递管理系统，实现入库功能。为了实现这些功能，你需要实现两个类：包裹(Package)类，快递点(CourierPoint)类。其中Package类对象表示不同的包裹，CourierPoint类对象表示不同的快递点。

你需要在自己定义的Package类中至少实现以下接口：
__init__(self, package_id)：接受package_id作为参数，初始化数据成员“包裹编号”为package_id，初始化数据成员“包裹入库地址横坐标”为-1, 初始化数据成员“包裹入库地址纵坐标”为-1
get_id(self): 获取包裹编号，并返回(return)
get_destination(self): 获取包裹入库地址，并以(横坐标,纵坐标)的格式输出
change_destination(self, x, y): 接收x, y作为参数，修改包裹入库地址横坐标为x，纵坐标为y

你需要在自己定义的CourierPoint类中至少实现以下接口：
__init__(self, x, y)：接收x, y作为参数，初始化数据成员快递点地址横坐标为x，纵坐标为y。
receive(self, package)：接收Package作为参数，调用你已经实现的接口修改包裹的入库地址，使其与快递点地址一致。
show_storage_info(self): 按照字符序升序，输出该快递点入库的所有快递的编号(以空格间隔开不同的编号)

while(True):
    exec(input())

参考样例：
1. 
输入：
package1=Package("1024")
package1_id = package1.get_id()
print(package1_id)
package1.get_destination()
exit()

输出：
1024
(-1,-1)

2. 
输入:
package1=Package("1024")
point1 = CourierPoint(3, 5)
point1.receive(package1)
package1.get_destination()
exit()
输出：
(3,5)

3. 
输入：
package1=Package("1024")
package2 = Package("1022")
package3 = Package("1025")
point1 = CourierPoint(3, 5)
point1.receive(package1)
point1.receive(package2)
point1.receive(package3)
point1.show_storage_info()
exit()
输出：
1022 1024 1025

实现:

``` python
class Package:

    def __init__(self, package_id) -> None:
        self.package_id = int(package_id)
        self.x = -1
        self.y = -1
    
    def get_id(self) -> int:
        return self.package_id

    def get_destination(self):
        print(f'({self.x},{self.y})')
        return (self.x, self.y)

    def change_destination(self, x: int, y: int):
        self.x = x
        self.y = y

class CourierPoint:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.packages = []

    def receive(self, package: Package):
        package.change_destination(self.x, self.y)
        self.packages.append(package)

    def show_storage_info(self):
        print(' '.join([str(package.get_id()) for package in sorted(self.packages, key=lambda package: package.get_id())]))

while True:
    exec(input())
```


## [Python] 矩阵

题目描述：

请你实现一个矩阵类(Matrix)，矩阵只有二维，包含行数、列数以及填充值等属性，实例化矩阵类的对象为n*m维值为f的矩阵(n、m、f分别为行数、列数和填充值，填充值是一个数字，矩阵所有元素值初始化为填充值f)。此外，该矩阵类还包括包含如下功能：

1.transpose(): 返回转置后的矩阵；

2.set_value((r, c), value):设置矩阵的值，r、c、value表示将矩阵第r行的第c列元素值设为value；(1<=r<=n, 1<=c<=m，若r、c超出范围，则打印"设置元素下标越界")

3.get_value((r, c)): 输出矩阵第r行第c列元素的值；1<=r<=n, 1<=c<=m，若r、c超出范围，则打印"获取元素下标越界"

4.reshape((r,c)): 返回r行c列形状的矩阵，这里仅考虑将二维矩阵转为二维矩阵的情况，且按照行的索引顺序读取原矩阵元素并按行顺序将元素放入新矩阵；此外，若新形状与原形态不兼容(新矩阵行数和列数相乘后的结果不等于原矩阵中元素的数量)，则输出"不能将该矩阵转为目标形状"，并返回None。


样例输入：
m=Matrix(2,3,2.0);m.set_value((1,2),3.0);m.set_value((2,2),4.0);m.get_value((2,2));mt=m.transpose();mt.get_value((3,1));mt.get_value((2,1));mts=mt.reshape((2,3));mts.get_value((2,3))

样例输出：
4.0
2.0
3.0
2.0

实现:

``` python
class Matrix:

    def __init__(self, n, m, fill=0, matrix=None, stroke=(0, 0)) -> None:
        self.shape_r = n
        self.shape_c = m
        if matrix:
            self.matrix = matrix
            self.stroke_r = stroke[0]
            self.stroke_c = stroke[1]
        else:
            self.matrix = [fill] * (n * m)
            self.stroke_r = m
            self.stroke_c = 1

    def print(self):
        print('--------')
        print('matrix', self.matrix)
        print('Stroke:', self.stroke_r, self.stroke_c)
        for r in range(self.shape_r):
            for c in range(self.shape_c):
                print(self.matrix[(r) * self.stroke_r +
                              (c) * self.stroke_c], end=' ')
            print('')
        print('--------')

    def set_value(self, pos, value):
        try:
            r, c = pos
            if r > self.shape_r or r < 1 or c > self.shape_c or c < 1:
                raise ValueError('越界')
            self.matrix[(r - 1) * self.stroke_r +
                        (c - 1) * self.stroke_c] = value
        except Exception as e:
            print('设置元素下标越界')

    def get_value(self, pos):
        try:
            r, c = pos
            if r > self.shape_r or r < 1 or c > self.shape_c or c < 1:
                raise ValueError('越界')
            print(self.matrix[(r - 1) * self.stroke_r +
                              (c - 1) * self.stroke_c])
        except Exception as e:
            print('获取元素下标越界')

    def transpose(self):
        return Matrix(self.shape_c, self.shape_r, matrix=self.matrix.copy(), stroke=(self.stroke_c, self.stroke_r))

    def reshape(self, shape):
        r, c = shape
        if self.shape_r * self.shape_c != r * c:
            print('不能将该矩阵转为目标形状')
            return(None)
        if self.stroke_c == 1:
            return Matrix(r, c, matrix=self.matrix.copy(), stroke=(c, 1))
        else:
            m = Matrix(r, c)
            for i in range(self.shape_r):
                for j in range(self.shape_c):
                    m.matrix[i * self.shape_c + j] = self.matrix[i * self.stroke_r + j * self.stroke_c]
            return m


exec(input())
```
