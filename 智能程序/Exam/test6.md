``` python
from typing import List

class CustomError(Exception):
    def __str__(self):
        return '调用异常'
        
class Package:

    def __init__ (self, package_id: str):
        """
        初始化函数, 初始化Package对象
        1) package_id表示包裹id
        2) 不同的包裹的id是不同的
        """
        self.id = package_id

    def GetPackageID(self) -> str:
        '''
        实例⽅法, 返回该包裹的id
        '''
        return self.id
    
    # 实例⽅法, 计算包裹的运送费⽤并返回
    # 在基类Package中不需要具体实现计算,
    # 但是需要抛出⾃定义异常 CustomError,
    # 并设定异常描述为"调⽤异常"
    def ComputeDeliverPrice(self, dist: int) -> int:
        """
        说明
        dist为运送距离
        """
        raise CustomError('调⽤异常')


class RegularPackage(Package):
    
    # 实例⽅法, 计算该包裹的运送费⽤并返回
    def ComputeDeliverPrice(self, dist: int) -> int:
        """
        说明
        运送费⽤ = 运送距离 * 1
        """
        return dist


class ValuablePackage(Package):
 
    # 实例⽅法, 计算该包裹的运送费⽤并返回
    def ComputeDeliverPrice(self, dist: int) -> int:
        """
        说明
        运送费⽤ = 运送距离 * 5
        """
        return dist * 5



class CourierPoint:
    # 保存着所有的快递点的列表
    CourierPointList = []

    # 初始化函数, 初始化CourierPoint对象
    def __init__(self, x: int, y: int):
        """
        说明
        1) (x, y)为该快递点的坐标位置, x和y均⼤于等于0
        2) 不⽤考虑在同⼀坐标位置有多个快递点的情况
        3) 快递点的仓库最多可存储的10个包裹
        """
        self.x = x
        self.y = y
        self.packages: List[Package] = []
        CourierPoint.CourierPointList.append(self)

    # 静态⽅法, 计算曼哈顿距离并返回
    @staticmethod
    def ComputeManhhanDistance(start_x: int, start_y: int, target_x: int, target_y: int) -> int:
        return abs(target_x - start_x) + abs(target_y - start_y)


    # 实例⽅法, 寄包裹并返回运送费⽤
    def Send(self, package: Package, dest_x: int, dest_y: int) -> int:
        """
        说明
        1) (dest_x, dest_y)为寄送⽬的地的坐标位置.
        2) 假设包裹需要从起始快递点(start_x, start_y)寄往⽬的地(dest_x, dest_y),
        则⾸先需要从已有的快递点集合中寻找距离⽬的地最近的快递点(target_x,target_y), 
        计算出起始快递点(start_x, start_y)到⽬标快递点(target_x, target_y)之间的曼哈顿距离, 
        再将曼哈顿距离作为参数传⼊包裹的计算运费函数, 得出运送费⽤.
        3) 以下情况视为寄送失败, 返回"-1": 
            1. 若距离⽬的地最近的快递点就是起始快递点;
            2. ⽬标快递点容量已满;
        4) 如果没有发⽣错误, 则将该包裹投递到⽬标快递点. 
        5) 不需要考虑以下特殊情况: 距离⽬的地最近的快递点除了起始快递点以外, 
        还有两个及以上的快递点距离⽬的地最近且距离相同.
        """

        # 找出最近的快递点
        CourierPointList = CourierPoint.CourierPointList
        min = CourierPoint.ComputeManhhanDistance(CourierPointList[0].x, CourierPointList[0].y, dest_x, dest_y)
        index = 0
        for i in range(1, len(CourierPointList)):
            currentPoint = CourierPointList[i]
            dis = CourierPoint.ComputeManhhanDistance(currentPoint.x, currentPoint.y, dest_x, dest_y)
            if dis < min:
                min = dis
                index = i
        destPoint: CourierPoint = CourierPointList[index]

        # 计算价格
        dis = CourierPoint.ComputeManhhanDistance(self.x, self.y, destPoint.x, destPoint.y)
        cost = package.ComputeDeliverPrice(dis)

        # 移除
        self.Pick(package)

        # 送快递, 并处理失败情况
        if destPoint == self or not destPoint.Receive(package):
            # 失败
            return -1
        else:
            # 成功
            return cost        


    # 实例⽅法, 包裹⼊库并返回执⾏状态
    def Receive(self, package: Package) -> bool:
        """
        说明
        当仓库容量已满时, 则⼊库失败, 仓库中已有包裹保持不变, 返回False; 当仓库容量仍有
        剩余时, 则⼊库成功, 返回True
        """
        if len(self.packages) < 10:
            # 仓库未满
            if self.Find(package.GetPackageID()):
                # 仓库中已有该包裹
                return False
            else:
                # 入库成功
                self.packages.append(package)
                return True
        else:
            # 仓库已满
            return False


    # 实例⽅法, 查询仓库中的包裹并返回包裹对象
    def Find(self, package_id: str) -> Package:
        """
        说明
        若未找到包裹id为package_id的包裹, 则返回None; 若找到包裹id为package_id的包
        裹, 则返回包裹
        """
        pac = None
        for package in self.packages:
            if package.GetPackageID() == package_id:
                pac = package
                break
        return pac
        

    # 实例⽅法, 取出包裹并返回执⾏状态
    def Pick(self, package_id: str) -> bool:
        """
        说明
        若仓库中没有包裹id为package_id的包裹, 则取件失败, 返回False; 若仓库中有包裹
        id为package_id的包裹, 则取件成功, 将此包裹从仓库中移出, 返回True
        """
        pac = self.Find(package_id)
        if pac:
            self.packages.remove(pac)
            return True
        else:
            return False


while True:
    exec(input())
```