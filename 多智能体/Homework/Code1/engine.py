'''
尝试使用组件化编程模式实现一个简易的游戏引擎, 以实现解耦合的游戏逻辑

文件划分标准是: engine.py 与过于具体的游戏逻辑无关, 只提供基础的网格地图的游戏逻辑

Doc: https://gpp.tkchu.me/component.html
'''

from abc import ABCMeta, abstractmethod
from typing import Any, List, Callable, Iterable
from functools import partial



# -------------------------------------------------------------------------
#   Component 部分
# -------------------------------------------------------------------------


class PositionComponent:
    '''
    位置组件, 一个不可变对象, 用于给对象提供位置属性
    不可变的原因是, 我们后续可以通过哈希来进行索引对象
    在对象中加入这个组件时, 用法为:

    self.position = PositionComponent(x, y)

    Attributes:
        x: 只读 int 类型, x 坐标
        y: 只读 int 类型, y 坐标
    '''

    # 用于标识 component 名称的属性
    component_name = 'position'

    def __init__(self, x=0, y=0) -> None:
        '''
        初始化位置组件, 返回一个不可变对象, 用于给对象提供位置属性.
        在对象中加入这个组件时, 用法为:

        self.position = PositionComponent(x, y)

        Args:
            x: int 类型, 初始化 x 坐标
            y: int 类型, 初始化 y 坐标
        '''
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def __hash__(self) -> int:
        return hash(('my_engine', self.component_name, (self._x, self._y)))

    def __eq__(self, __value: object) -> bool:
        return (self.component_name, (self._x, self._y)) \
            == (getattr(__value, 'component_name', None),
                (getattr(__value, '_x', None), getattr(__value, '_y', None)))

    def __repr__(self) -> str:
        return f'PositionComponent({self._x}, {self._y})'


class RigidbodyComponent:
    '''
    刚体组件, 一个不可变对象, 用于给对象提供刚体属性
    在对象中加入这个组件时, 用法为:

    self.rigidbody = RigidbodyComponent()

    Attributes:
        x: 只读 int 类型, x 坐标
        y: 只读 int 类型, y 坐标
    '''

    # 用于标识 component 名称的属性
    component_name = 'rigidbody'

    def __init__(self) -> None:
        '''
        初始化位置组件, 返回一个不可变对象, 用于给对象提供刚体属性.
        在对象中加入这个组件时, 用法为:

        self.rigidbody = RigidbodyComponent()
        '''
        pass

    def __hash__(self) -> int:
        return hash(('my_engine', self.component_name, ()))

    def __eq__(self, __value: object) -> bool:
        return self.component_name == getattr(__value, 'component_name', None)

    def __repr__(self) -> str:
        return f'RigidbodyComponent()'




# -------------------------------------------------------------------------
#   Layout 部分
# -------------------------------------------------------------------------


class HashableLayout:
    '''
    通过 Hashable 的类型来实现游戏对象 O(1) 时间的查询和 O(n) 时间的遍历功能的布局对象
    '''

    def __init__(self, type, objects: Iterable = []) -> None:
        '''
        初始化 HashableLayout

        Args:
            type: 一个 Hashable 的类
            objects: 可选, 一个可迭代的初始游戏对象列表
        '''
        # 自动注入的属性
        # 自动注入的父对象
        self.parent = None
        # 自动注入的世界对象
        self._world = None
        # 自动注入的 GamePlay 对象
        self._gameplay = None
        # Hashable 的 component 类型
        self.type = type
        # 用于保存的字典
        self.dict = {}
        self.add(objects)

    def autowire(self, child):
        # 进行自动注入
        child.parent = self
        child.world = self.world
        child.gameplay = self.gameplay

    def autowire_all(self):
        for child in self.dict.values():
            self.autowire(child)

    def append(self, child):
        assert hasattr(child, self.type.component_name)
        hashable_component = getattr(child, self.type.component_name)
        assert hashable_component not in self.dict
        self.dict[hashable_component] = child
        # 进行自动注入
        self.autowire(child)

    def remove(self, component):
        assert component in self.dict
        del self.dict[component]

    def add(self, children):
        for child in children:
            self.append(child)

    def get(self, args: Iterable, default=None):
        component = self.type(*args)
        if component in self.dict:
            return self.dict[component]
        else:
            return default

    def handle_replace_with(self, old_component, child):
        '''
        处理子对象的组件更换事件
        '''
        if isinstance(old_component, self.type):
            self.remove(old_component)
            self.append(child)

    @property
    def world(self):
        return self._world
    
    @world.setter
    def world(self, new_world):
        self._world = new_world
        self.autowire_all()

    @property
    def gameplay(self):
        return self._gameplay
    
    @gameplay.setter
    def gameplay(self, new_gameplay):
        self._gameplay = new_gameplay
        self.autowire_all()

    def keys(self):
        return self.dict.keys()

    def values(self):
        return self.dict.values()

    def __repr__(self) -> str:
        return repr(self.dict)


# 通过偏函数将 PositionComponent 绑定到 HashableLayout 以生成 PositionLayout
PositionLayout = partial(HashableLayout, PositionComponent)



# -------------------------------------------------------------------------
#   GameObject 部分
# -------------------------------------------------------------------------

class GameObject:

    def __init__(self) -> None:
        # 自动注入的父对象
        self._parent = None
        # 自动注入的世界对象
        self._world = None
        # 自动注入的 GamePlay 对象
        self._gameplay = None
        # 是否需要清除
        self.deleted = False

    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent
        if new_parent and hasattr(self, 'bind_parent'):
            if isinstance(getattr(self, 'bind_parent'), Callable):
                getattr(self, 'bind_parent')(new_parent)

    @property
    def world(self):
        return self._world
    
    @world.setter
    def world(self, new_world):
        self._world = new_world
        if new_world and hasattr(self, 'bind_world'):
            if isinstance(getattr(self, 'bind_world'), Callable):
                getattr(self, 'bind_world')(new_world)

    @property
    def gameplay(self):
        return self._gameplay
    
    @gameplay.setter
    def gameplay(self, new_gameplay):
        self._gameplay = new_gameplay
        if new_gameplay and hasattr(self, 'bind_gameplay'):
            if isinstance(getattr(self, 'bind_gameplay'), Callable):
                getattr(self, 'bind_gameplay')(new_gameplay)


    def replace_with(self, new_component):
        '''
        更换对应的组件
        会通过 self.parent.handle_replace_with(old_component, child) 事件通知父对象
        '''
        assert hasattr(new_component, 'component_name')
        component_name = getattr(new_component, 'component_name')
        assert hasattr(self, component_name)
        old_component = getattr(self, component_name)
        setattr(self, component_name, new_component)
        if self.parent and hasattr(self.parent, 'handle_replace_with'):
            getattr(self.parent, 'handle_replace_with')(old_component, self)
    
    def delete(self):
        '''
        清除自身, 会在一次游戏循环后清除
        '''
        self.deleted = True



# -------------------------------------------------------------------------
#   World 部分
# -------------------------------------------------------------------------


class TileWorld:

    def __init__(self, size, children={}) -> None:
        '''
        一个瓦片世界

        Args:
            size: 瓦片世界的尺寸, 可以传入 N: int 或 (N, M), 且对应顺序为 (x, y)
            children: 子节点, 可以传入字典, Layout, 数组以及其他可迭代对象, 并且支持嵌套
        '''
        if isinstance(size, Iterable):
            size = tuple(size)
            assert len(size) == 2
            self.N = size[0]
            self.M = size[1]
        else:
            self.N = size
            self.M = size
        # 加入子对象
        self.children = children
        # 自动注入的 gameplay
        self._gameplay = None
        # 进行自动注入
        self.autowire_all(self.children)
    
    @staticmethod
    def manhattan_distance(pos1: Iterable[int], pos2: Iterable[int]) -> int:
        pos1 = tuple(pos1)
        pos2 = tuple(pos2)
        assert len(pos1) == 2
        assert len(pos2) == 2
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) 

    @property
    def gameplay(self):
        return self._gameplay
    
    @gameplay.setter
    def gameplay(self, new_gameplay):
        self._gameplay = new_gameplay
        self.autowire_all(self.children)
    
    def autowire(self, child):
        child.world = self
        child.gameplay = self._gameplay

    def autowire_all(self, node):
        if isinstance(node, GameObject):
            self.autowire(node)
        elif hasattr(node, 'values'):
            values = getattr(node, 'values')
            if isinstance(node, HashableLayout):
                self.autowire(node)
            if isinstance(values, Callable):
                values = values()
                for value in values:
                    self.autowire_all(value)
        elif isinstance(node, Iterable):
            for value in node:
                self.autowire_all(value)
        else:
            raise ValueError('不合法的子节点.')

    def get_by_position(self, x, y, all=False):
        '''
        找到位于 (x, y) 位置的对象, 如果设置 all=True 则会返回一个对象数组
        '''
        result = None
        result_list = []

        def traverse(node):
            nonlocal result
            if not all and result:
                return
            if isinstance(node, GameObject):
                if hasattr(node, PositionComponent.component_name) and \
                        getattr(node, 'position').x == x and getattr(node, 'position').y == y:
                    result = node
                    result_list.append(node)
            elif isinstance(node, HashableLayout) and node.type == PositionComponent:
                node_with_position = node.get((x, y))
                if node_with_position:
                    result = node_with_position
                    result_list.append(node_with_position)
            elif hasattr(node, 'values'):
                values = getattr(node, 'values')
                if isinstance(values, Callable):
                    values = values()
                    for value in values:
                        traverse(value)
            elif isinstance(node, Iterable):
                for value in node:
                    traverse(value)
            else:
                raise ValueError('不合法的子节点.')
        traverse(self.children)
        if all:
            return result_list
        else:
            return result

    def is_empty(self, x: int, y: int, all=False) -> bool:
        '''
        位置 (x, y) 是否为空, 越界时返回 False

        其中 all 默认为 False, 代表只查询该位置的第一个对象
        '''
        if x < 0 or y < 0 or x >= self.N or y >= self.M:
            return False
        return not self.get_by_position(x, y, all)

    def is_rigidbody(self, x: int, y: int, all=False) -> bool:
        '''
        位置 (x, y) 是否存在刚体, 越界时返回 True

        其中 all 默认为 False, 代表只查询该位置的第一个对象
        '''
        if x < 0 or y < 0 or x >= self.N or y >= self.M:
            return True
        return hasattr(self.get_by_position(x, y, all), RigidbodyComponent.component_name)

    def render(self, transpose=False) -> List[List[Any]]:
        '''
        返回一个经过转置的数组, (x, y) 对应第 y 行第 x 个元素,
        该元素要么是一个 GameObject 对象, 要么是一个 GameObject 数组.
        '''
        board = [[None] * self.M for _ in range(self.N)]
        def push(x, y, obj):
            if transpose:
                x, y = y, x
            if board[x][y]:
                if not isinstance(board[x][y], List):
                    board[x][y] = [board[x][y]]
                board[x][y].append(obj)
            else:
                board[x][y] = obj
        def traverse(node):
            if isinstance(node, GameObject):
                if hasattr(node, PositionComponent.component_name):
                    pos = getattr(node, 'position')
                    push(pos.x, pos.y, node)
            elif hasattr(node, 'values'):
                values = getattr(node, 'values')
                if isinstance(values, Callable):
                    values = values()
                    for value in values:
                        traverse(value)
            elif isinstance(node, Iterable):
                for value in node:
                    traverse(value)
            else:
                raise ValueError('不合法的子节点.')
        traverse(self.children)
        return board
    
    def call(self, method_name: str) -> None:
        '''
        对子节点调用一次 child.method_name()
        '''
        def traverse(node):
            if isinstance(node, GameObject):
                if hasattr(node, method_name):
                    getattr(node, method_name)()
            elif hasattr(node, 'values'):
                values = getattr(node, 'values')
                if isinstance(values, Callable):
                    values = values()
                    for value in values:
                        traverse(value)
            elif isinstance(node, Iterable):
                for value in node:
                    traverse(value)
            else:
                raise ValueError('不合法的子节点.')
        traverse(self.children)

    def start(self) -> None:
        '''
        对子节点调用一次开始
        '''
        self.call('start')

    def update(self) -> None:
        '''
        对子节点调用一次更新
        '''
        self.call('update')

    def end(self) -> None:
        '''
        对子节点调用一次终止
        '''
        self.call('end')
    
    def clear(self) -> None:
        '''
        清除所有被标记为 deleted 的子节点
        '''
        def traverse(node):
            if isinstance(node, HashableLayout):
                deleted_list = []
                for value in node.values():
                    assert isinstance(value, GameObject)
                    if value.deleted:
                        deleted_list.append(value)
                for value in deleted_list:
                    node.remove(getattr(value, node.type.component_name))
            elif isinstance(node, dict):
                key_list = []
                for key in node:
                    if isinstance(node[key], GameObject):
                        if node[key].deleted:
                            key_list.append(key)
                    else:
                        traverse(node[key])
                for key in key_list:
                    del node[key]
            elif isinstance(node, Iterable):
                node = list(node)
                key_list = []
                for key in range(len(node)):
                    if isinstance(node[key], GameObject):
                        if node[key].deleted:
                            key_list.append(key)
                    else:
                        traverse(node[key])
                for key in key_list:
                    del node[key]
            else:
                raise ValueError('不合法的子节点.')
        traverse(self.children)
    
    def __repr__(self) -> str:
        return 'TileWorld'



# -------------------------------------------------------------------------
#   Gameplay 部分
# -------------------------------------------------------------------------

class EventBus:

    '''
    实现一个中心化的消息总线, 以实现观察者模式 (以及我们不记录发布者)

    https://refactoringguru.cn/design-patterns/observer
    '''

    def __init__(self) -> None:
        self.bus = {}
    
    def subscribe(self, event_name: str, callback: Callable):
        if event_name not in self.bus:
            self.bus[event_name] = []
        self.bus[event_name].append(callback)

    def publish(self, event_name: str, *args):
        if event_name not in self.bus:
            return
        for callback in self.bus[event_name]:
            callback(*args)


class DiscreteTimeGameplay(metaclass=ABCMeta):
    '''
    time 是离散的 Gameplay 模式
    '''

    def __init__(self, world) -> None:
        # 一个中心化的消息总线, 以实现观察者模式
        self.event_bus = EventBus()
        # 用来计数的时间, 离散的
        self._time = 0
        self.world = world
        world.gameplay = self

    @property
    def time(self):
        return self._time

    def update(self) -> None:
        '''
        进行一次更新
        '''
        # 对世界进行更新
        assert hasattr(self.world, 'update')
        self.world.update()
        # 对世界中需要清除的对象进行清除
        self.world.clear()
        # 计数时间自增 1
        self._time += 1

    @abstractmethod
    def terminate(self) -> bool:
        '''
        应该被实现的抽象函数, 用于返回当前游戏是否应该终止
        '''
        return False

    def start(self) -> None:
        '''
        当前游戏开始时被调用
        '''
        assert self.world
        self.world.start()

    def end(self) -> None:
        '''
        当前游戏终止时被调用
        '''
        assert self.world
        self.world.end()

    def run(self) -> None:
        '''
        开始执行, 直到终止
        '''
        self.start()
        while not self.terminate():
            self.update()
        self.end()

    def __repr__(self) -> str:
        return f'DiscreteTimeGameplay {{ time: {self._time} }}'


class IterativeGameplay(DiscreteTimeGameplay):

    '''
    满 iterations 次迭代就终止.

    可以重写的方法有 update 和 terminate.

    需要实现 end 抽象方法.
    '''

    def __init__(self, world, iterations) -> None:
        super().__init__(world)
        self.iterations = iterations

    def terminate(self) -> bool:
        return self.time == self.iterations


