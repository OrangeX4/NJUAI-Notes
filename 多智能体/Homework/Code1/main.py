'''
基于 engine.py 提供的基础游戏引擎接口实现的具体的逻辑代码
'''

from math import inf
from typing import Iterable
from matplotlib import colors, pyplot as plt
import numpy as np
from enum import Enum
from tqdm import tqdm
import random

from priority_queue import PriorityQueue
from engine import GameObject, TileWorld, PositionComponent, RigidbodyComponent, PositionLayout, IterativeGameplay

class Hole(GameObject):

    def __init__(self, x: int, y: int, min_life_expectancy: int, max_life_expectancy: int,
                 min_score: int, max_score: int) -> None:
        super().__init__()
        self.position = PositionComponent(x, y)
        # 生成生命预期与得分
        self.life_expectancy = random.randint(min_life_expectancy, max_life_expectancy)
        self.score = random.randint(min_score, max_score)
        self.age = 0

    def start(self):
        '''
        游戏开始后, 发布洞穴出现事件
        '''
        assert self.gameplay
        self.gameplay.event_bus.publish('hole_appear', self)

    def bind_gameplay(self, new_gameplay):
        '''
        绑定 gameplay 后, 发布洞穴出现事件
        '''
        assert new_gameplay
        new_gameplay.event_bus.publish('hole_appear', self)

    def update(self):
        self.age += 1
        # 达到了生命预期, 删除自身
        if self.life_expectancy == self.age:
            self.delete()
            # 发布洞穴消失事件
            assert self.gameplay
            self.gameplay.event_bus.publish('hole_disappear', self)

    def __repr__(self) -> str:
        return f'Hole {{ age: {self.age}, position: ({self.position.x}, {self.position.y}) }}'


class Obstacle(GameObject):

    def __init__(self, x=0, y=0) -> None:
        super().__init__()
        # 绑定位置组件, 标识当前的位置
        self.position = PositionComponent(x, y)
        # 绑定刚体组件, 以实现在这个位置不能存在其他刚体
        self.rigidbody = RigidbodyComponent()

    def __repr__(self) -> str:
        return f'Obstacle {{ position: ({self.position.x}, {self.position.y}) }}'



# 行动的枚举集合
class Action(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Agent(GameObject):

    def __init__(self, x=0, y=0, p=1, k=4, reaction_strategy='blind') -> None:
        super().__init__()
        # 绑定位置组件, 标识当前的位置
        self.position = PositionComponent(x, y)
        # 绑定刚体组件, 以实现在这个位置不能存在其他刚体
        self.rigidbody = RigidbodyComponent()
        # 规划时间
        self.p = p
        # 重新考虑的 k
        self.k = k
        # 反应策略
        assert reaction_strategy in ['blind', 'disappear', 'nearer_hole', 'any_hole']
        self.reaction_strategy = reaction_strategy
        # 设置规划倒计时
        self.planning_count_down = 0

    def bind_gameplay(self, new_gameplay):
        # 当绑定了 gameplay 对象后 (即 self.gameplay 被赋值)
        # 监听 hole_appear 和 hole_disappear 事件
        new_gameplay.event_bus.subscribe('hole_appear', self.handle_hole_appear)
        new_gameplay.event_bus.subscribe('hole_disappear', self.handle_hole_disappear)

    def handle_hole_appear(self, hole):
        '''
        监听洞穴出现事件, 洞穴出现后进行的操作
        '''
        res = False
        if self.reaction_strategy == 'any_hole':
            res = True
        elif self.reaction_strategy == 'nearer_hole' and not self.intention:
            res = True
        elif self.reaction_strategy == 'nearer_hole' and self.intention:
            assert self.world
            dist = self.world.manhattan_distance
            agent_pos = (self.position.x, self.position.y)
            new_hole_pos = (hole.position.x, hole.position.y)
            intention_pos = (self.intention.position.x, self.intention.position.y)
            res = dist(agent_pos, new_hole_pos) < dist(agent_pos, intention_pos)
        if res:
            # 重新进行规划
            desires = self.options()
            # 获取最优目标洞穴
            self.intention = self.filter(desires)
            # 获取对应的规划
            self.pi = self.plan(self.intention)


    def handle_hole_disappear(self, hole):
        '''
        监听洞穴消失事件, 洞穴消失后进行的操作
        '''
        if self.reaction_strategy in ['disappear', 'nearer_hole', 'any_hole']:
            if hole == self.intention:
                # 重新进行规划
                desires = self.options()
                # 获取最优目标洞穴
                self.intention = self.filter(desires)
                # 获取对应的规划
                self.pi = self.plan(self.intention)

    def utility(self, desire):
        '''
        以原论文中的说法, utility 是 score divided by distance
        '''
        if desire.position != self.position:
            desire_pos = (desire.position.x, desire.position.y)
            self_pos = (self.position.x, self.position.y)
            assert self.world
            return desire.score / self.world.manhattan_distance(desire_pos, self_pos)
        else:
            # 返回 0, 以便放弃当前的洞穴
            return 0

    def options(self):
        '''
        BDI 中的 options, 以获取当前的所有洞穴,
        这里返回的是一个列表
        '''
        assert self.world
        assert 'holes' in self.world.children
        return [v for v in self.world.children['holes'].values() if v.position != self.position]

    def filter(self, desires):
        '''
        BDI 中的 filter, 从 desires 中获取最优的一个洞穴作为 intention
        '''
        if len(desires) != 0:
            utilities = [self.utility(desire) for desire in desires]
            return desires[utilities.index(max(utilities))]
        else:
            return None
        
    def a_star(self, intention, heuristic):
        '''
        通过 Astar 算法来寻路
        '''
        # 起点
        s_x, s_y = self.position.x, self.position.y
        # 目标
        t_x, t_y = intention.position.x, intention.position.y
        # 棋盘大小
        assert self.world
        N, M = self.world.N, self.world.M
        # 当前节点到源点 s 的距离
        distance_from_s = {}
        # 当前节点的父节点
        parent = {}
        # 初始化
        for i in range(N):
            for j in range(M):
                distance_from_s[(i, j)] = inf
        # 初始节点
        distance_from_s[(s_x, s_y)] = 0
        metric = distance_from_s[(s_x, s_y)] + heuristic((s_x, s_y), (t_x, t_y))
        # 建一个优先级队列
        queue = PriorityQueue([(metric, (s_x, s_y))])
        while len(queue) != 0:
            elem = queue.pop()
            assert elem
            u = elem[1]
            if u == (t_x, t_y):
                break
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                v = (u[0] + dx, u[1] + dy)
                if not self.world.is_rigidbody(v[0], v[1]) and \
                        distance_from_s[v] > distance_from_s[u] + 1:
                    distance_from_s[v] = distance_from_s[u] + 1
                    metric = distance_from_s[v] + heuristic(v, (t_x, t_y))
                    parent[v] = u
                    queue.put_or_update((metric, v))
        # 获取最终结果
        cur = (t_x, t_y)
        path = [cur]
        while cur in parent:
            cur = parent[cur]
            path.append(cur)
        path.reverse()
        pi = []
        for i in range(len(path) - 1):
            dx, dy = path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1]
            if (dx, dy) == (0, -1):
                pi.append(Action.UP)
            elif (dx, dy) == (0, 1):
                pi.append(Action.DOWN)
            elif (dx, dy) == (-1, 0):
                pi.append(Action.LEFT)
            elif (dx, dy) == (1, 0):
                pi.append(Action.RIGHT)
            else:
                raise ValueError('Invalid (dx, dy): ' + str((dx, dy)))
        return pi

    def plan(self, intention):
        '''
        BDI 中的 plan, 根据世界信息和 intention 得到最优的规划
        '''
        if intention:
            # 设置规划倒计时
            if self.planning_count_down > 0:
                self.planning_count_down = 0
            assert self.world
            self.planning_count_down += self.p
            self.plan_intention = intention
            return self.a_star(intention, self.world.manhattan_distance)
        else:
            # 规划倒计时归零
            self.planning_count_down = 0
            self.plan_intention = None
            return []
        
    def reconsider(self):
        '''
        BDI 中的 reconsider, 判断是否需要重新考虑 desires 和 intention
        '''
        assert self.gameplay
        return (self.gameplay.time + 1) % self.k == 0
        
    def sound(self, intention):
        '''
        BDI 中的 sound, 判断是否需要重新考虑 plan
        '''
        assert self.plan_intention
        return self.plan_intention == intention
    
    def execute(self, action):
        '''
        BDI 中的 action, 执行某个动作
        '''
        # 拆出常用变量
        x, y = self.position.x, self.position.y
        if (action == Action.UP):
            self.replace_with(PositionComponent(x, y - 1))
        elif (action == Action.DOWN):
            self.replace_with(PositionComponent(x, y + 1))
        elif (action == Action.LEFT):
            self.replace_with(PositionComponent(x - 1, y))
        elif (action == Action.RIGHT):
            self.replace_with(PositionComponent(x + 1, y))
        else:
            raise ValueError('Unsupported action: ' + action)

    def start(self):
        '''
        游戏开始
        '''
        # 实用推理 Agent 相关的初始化
        # 不显式存储信念 beliefs, 相关数据从 self.world 中获取
        # 不显式存储信念 desires, 相关数据随时使用随时获取
        desires = self.options()
        # 获取最优目标洞穴
        self.intention = self.filter(desires)
        # 获取对应的规划
        self.pi = self.plan(self.intention)

    def update(self):

        # 拆出常用变量
        x, y = self.position.x, self.position.y
        world = self.world
        gameplay = self.gameplay
        assert world
        assert gameplay
        assert self.pi != None

        # 如果现在在某个洞穴上方
        objects_in_position = world.get_by_position(x, y, all=True)
        hole = None
        for object in objects_in_position:
            if isinstance(object, Hole):
                hole = object
        if hole:
            # 记录得分
            gameplay.score += hole.score
            # 删除该洞穴
            hole.delete()
            # 同时从 intention 中去除
            if self.intention == hole:
                self.intention = None

        # 如果规划倒计时不为零, 则减 1 后跳过, 代表仍在规划
        if self.planning_count_down > 0:
            self.planning_count_down -= 1
            return

        # 如果当前规划为空
        if len(self.pi) == 0:
            # 重新进行规划
            desires = self.options()
            # 获取最优目标洞穴
            self.intention = self.filter(desires)
            # 获取对应的规划
            self.pi = self.plan(self.intention)
            # 规划后应立即结束, 进入倒计时
            if self.planning_count_down >= 0:
                return
        
        # 进行规划的执行
        # alpha := hd(pi)
        action = self.pi[0]
        # execute(alpha)
        self.execute(action)
        # pi := tail(pi)
        self.pi = self.pi[1:]

        # 是否重新考虑
        if self.reconsider():
            # 重新进行规划
            desires = self.options()
            # 获取最优目标洞穴
            self.intention = self.filter(desires)
        
        # 目标和规划是否还相匹配
        # 这里本来应该不注释的, 但是和论文效果不一致, 所以就注释了
        # if not self.sound(self.intention):
            # 不匹配, 重新规划
            self.pi = self.plan(self.intention)
            # 规划后应立即结束, 进入倒计时
            if self.planning_count_down >= 0:
                return


    def __repr__(self) -> str:
        return f'Agent {{ position: ({self.position.x}, {self.position.y}) }}'



class TileWorldGameplay(IterativeGameplay):

    def __init__(self, world, config) -> None:
        super().__init__(world, config['iterations'])
        # 初始化参数
        self.config = config
        self.score = 0
        self.target_score = 0
        self.min_score = config['min_score']
        self.max_score = config['max_score']
        self.visualize = config['visualize']
        self.visualize_result = config['visualize_result']
        # 与世界变化率相关的参数
        self.gamma = config['gamma']
        self.min_life_expectancy = config['min_life_expectancy'] // self.gamma
        self.max_life_expectancy = config['max_life_expectancy'] // self.gamma
        self.min_gestation = config['min_gestation'] // self.gamma
        self.max_gestation = config['max_gestation'] // self.gamma
        # 用于显示进度的 tqdm
        self.is_tqdm = config['is_tqdm']
        if self.is_tqdm:
            self.tqdm_iter = iter(tqdm(range(config['iterations'])))
        # 开启渲染
        if self.visualize or self.visualize_result:
            self.render_on()

    def gen_hole(self):
        '''
        游戏逻辑中的一部分: 动态生成洞穴
        '''
        x = random.randint(0, self.world.N)
        y = random.randint(0, self.world.M)
        while not self.world.is_empty(x, y):
            x = random.randint(0, self.world.N)
            y = random.randint(0, self.world.M)
        # 生成洞穴并加入
        new_hole = Hole(x, y, self.min_life_expectancy, self.max_life_expectancy, self.min_score, self.max_score)
        self.world.children['holes'].append(new_hole)
        # 加入可以达到的最高分数
        self.target_score += new_hole.score

    def start(self) -> None:
        super().start()
        # 生成初始洞穴
        self.gen_hole()
        # 生成初始 gestation_count_down
        self.gestation_count_down = random.randint(self.min_gestation, self.max_gestation)

    def update(self):
        # 生成洞穴
        if self.gestation_count_down > 0:
            self.gestation_count_down -= 1
        else:
            self.gen_hole()
            self.gestation_count_down = random.randint(self.min_gestation, self.max_gestation)
        # 迭代 tqdm 显示进度
        if self.is_tqdm:
            next(self.tqdm_iter)
        # 渲染世界
        if self.visualize:
            self.render_world()
        # 调用父类方法
        super().update()

    def end(self) -> None:
        # 调用父类方法
        super().end()
        # 终止迭代
        if self.is_tqdm:
            try:
                next(self.tqdm_iter)
            except StopIteration:
                pass
        # 结束渲染
        if self.visualize_result:
            self.render_world()
        if self.visualize or self.visualize_result:
            self.render_off()

    def render_on(self):
        # 分别是空格, 洞穴, 障碍物和 Agent 的颜色
        self.cmap = colors.ListedColormap(['white', 'gray', 'red', 'blue'], 'my_cmap')
        self.figure = plt.figure()
        plt.ion()
        
    def render_off(self):
        plt.ioff()
        plt.show()

    def render_world(self):
        '''
        渲染世界
        '''
        # 获取一个 GameObject 对象二维数组
        object_board = self.world.render(transpose=True)
        # x 轴和 y 轴的最大值
        N, M = len(object_board), len(object_board[0])
        # 通过 object_board 获得对应的 board
        board = np.zeros((N, M), dtype=int)
        for x in range(N):
            for y in range(M):
                if isinstance(object_board[x][y], Hole):
                    board[x][y] = 1
                elif isinstance(object_board[x][y], Obstacle):
                    board[x][y] = 2
                elif isinstance(object_board[x][y], Agent):
                    board[x][y] = 3
                elif isinstance(object_board[x][y], list):
                    board[x][y] = 3

        # 开始渲染
        plt.clf()
        ax = self.figure.add_subplot(111)
        ax.matshow(board, cmap=self.cmap)
        # This is very hack-ish
        ax.set_xticks(np.arange(-.5, N, 1), minor='true')
        ax.set_yticks(np.arange(-.5, M, 1), minor='true')
        ax.grid(which='minor', color='black', linewidth=1)
        plt.title("Tile World")
        # 暂停 0.01 秒
        plt.pause(0.01)


def gen_obstacles_and_agent(config):
    if isinstance(config['size'], Iterable):
        N, M = config['size']
    else:
        N, M = config['size'], config['size']
    positions = [(x, y) for x in range(N) for y in range(M)]
    random.shuffle(positions)
    res = []
    for x, y in positions[:config['obstacle_num']]:
        res.append(Obstacle(x, y))
    a_x, a_y = positions[config['obstacle_num']]
    return PositionLayout(res), Agent(a_x, a_y, config['p'], config['k'], config['reaction_strategy'])


def init_config():
    return {
        'seeds': [3, 1, 8],  # 随机数种子
        'size': 30,  # 世界大小
        'iterations': 3000,  # 迭代次数
        'obstacle_num': 100,  # 障碍物个数
        'min_gestation': 60,  # 最小间隔时间
        'max_gestation': 240,  # 最大间隔时间
        'min_life_expectancy': 240,  # 最小生命预期
        'max_life_expectancy': 960,  # 最大生命预期
        'gamma': 1,  # 世界变化率
        'min_score': 1,  # 最小分数
        'max_score': 10,  # 最大分数
        'p': 1,  # 规划时间
        'k': inf,  # 每 k 步重新考虑意图, 设置 1 即为 cautious, 设置 4 即为 normal, 设置 inf 即为 bold
        'reaction_strategy': 'blind',  # 反应策略, 应为 'blind', 'disappear', 'nearer_hole', 'any_hole' 中的一个
        'visualize': False,  # 是否渲染每一步
        'visualize_result': False,  # 是否渲染结果
        'is_tqdm': False,  # 是否开启进度条
        'print_score': True,  # 打印 score
    }


def run(config):
    '''
    带有 seeds 的一次平均运行
    '''
    score = []
    target_score = []
    score_rate = []
    for i in range(len(config['seeds'])):
        seed = config['seeds'][i]
        random.seed(seed)
        hole_layout = PositionLayout()
        obstacle_layout, agent = gen_obstacles_and_agent(config)
        world = TileWorld(size=config['size'], children={'holes': hole_layout, 'obstacles': obstacle_layout, 'agent': agent})
        gameplay = TileWorldGameplay(world, config)
        gameplay.run()
        # 输出分数
        score.append(gameplay.score)
        target_score.append(gameplay.target_score)
        score_rate.append(score[i] / target_score[i])
        if config['print_score']:
            print(f'Iter {i} with seed {seed}: {score[i]} / {target_score[i]} = {score_rate[i]} (score / target_score)')
    epsilon = sum(score_rate) / len(score_rate)
    min_epsilon = min(score_rate)
    max_epsilon = max(score_rate)
    if config['print_score']:
        print(f'Average score rate: {epsilon}')
    return epsilon, min_epsilon, max_epsilon


def exper1():
    # 初始化实验相关配置
    print('------------------------------')
    print('  exper1  ')
    print('------------------------------')
    config = init_config()
    # 最后的保存结果
    epsilons = []
    min_epsilons = []
    max_epsilons = []
    # 世界变化率
    log10gammas = np.linspace(0, 2, 16)
    gammas = 10 ** log10gammas
    for gamma in gammas:
        new_config = {**config, 'gamma': gamma}
        epsilon, min_epsilon, max_epsilon = run(new_config)
        epsilons.append(epsilon)
        min_epsilons.append(min_epsilon)
        max_epsilons.append(max_epsilon)
    plt.plot(gammas, epsilons, linestyle='-', marker='D', 
             markersize=5, linewidth=2, color='cornflowerblue', label='experimental')
    plt.fill_between(gammas, min_epsilons, max_epsilons, color='cornflowerblue', alpha=0.2) # type: ignore
    plt.legend()
    plt.title('Figure 1: Effect of Rate of World Change')
    plt.ylabel(r'$\epsilon$')
    plt.xlabel(r'$\gamma$')
    plt.grid()
    plt.savefig('images/figure1.png', dpi=200)
    # plt.show()
    plt.close()

    plt.plot(log10gammas, epsilons, linestyle='-', marker='D', 
             markersize=5, linewidth=2, color='cornflowerblue', label='experimental')
    plt.fill_between(log10gammas, min_epsilons, max_epsilons, color='cornflowerblue', alpha=0.2) # type: ignore
    plt.legend()
    plt.title('Figure 2: Effect of Rate of World Change (log x-scale)')
    plt.ylabel(r'$\epsilon$')
    plt.xlabel(r'$\log_{10}\gamma$')
    plt.grid()
    plt.savefig('images/figure2.png', dpi=200)
    # plt.show()
    plt.close()

    print('------------------------------')
    print('  exper1 completed  ')
    print('------------------------------')

def exper2():
    # 初始化实验相关配置
    print('------------------------------')
    print('  exper2  ')
    print('------------------------------')
    config = init_config()

    def exper2_with_k(k, title, filename):
        # 最后的保存结果
        epsilons = []
        min_epsilons = []
        max_epsilons = []
        # 世界变化率
        log10gammas = np.linspace(0, 2, 16, endpoint=False)
        gammas = 10 ** log10gammas
        for p in [0.5, 1, 2, 4]:
            epsilons.append([])
            min_epsilons.append([])
            max_epsilons.append([])
            for gamma in gammas:
                new_config = {**config, 'p': p, 'k': k, 'gamma': gamma}
                epsilon, min_epsilon, max_epsilon = run(new_config)
                epsilons[-1].append(epsilon)
                min_epsilons[-1].append(min_epsilon)
                max_epsilons[-1].append(max_epsilon)
        plt.plot(log10gammas, epsilons[0], linestyle='-', marker='D',
                markersize=5, linewidth=2, color='cornflowerblue', label='p = 0.5')
        plt.fill_between(log10gammas, min_epsilons[0], max_epsilons[0], color='cornflowerblue', alpha=0.2) # type: ignore
        plt.plot(log10gammas, epsilons[1], linestyle='--', marker='^',
                markersize=5, linewidth=2, color='brown', label='p = 1.0')
        plt.fill_between(log10gammas, min_epsilons[1], max_epsilons[1], color='brown', alpha=0.2) # type: ignore
        plt.plot(log10gammas, epsilons[2], linestyle='-', marker='s',
                markersize=5, linewidth=2, color='lightseagreen', label='p = 2.0')
        plt.fill_between(log10gammas, min_epsilons[2], max_epsilons[2], color='lightseagreen', alpha=0.2) # type: ignore
        plt.plot(log10gammas, epsilons[3], linestyle='--', marker='v',
                markersize=5, linewidth=2, color='mediumvioletred', label='p = 4.0')
        plt.fill_between(log10gammas, min_epsilons[3], max_epsilons[3], color='mediumvioletred', alpha=0.2) # type: ignore
        plt.legend()
        plt.title(title)
        plt.ylabel(r'$\epsilon$')
        plt.xlabel(r'$\log_{10}\gamma$')
        plt.grid()
        plt.savefig(filename, dpi=200)
        # plt.show()
        plt.close()

    exper2_with_k(k=inf, title='Figure 3: Effect of Planning Time (bold agent)', filename='images/figure3.png')
    exper2_with_k(k=1, title='Figure 4: Effect of Planning Time (cautious agent)', filename='images/figure4.png')

    print('------------------------------')
    print('  exper2 completed  ')
    print('------------------------------')

def exper3():
    # 初始化实验相关配置
    print('------------------------------')
    print('  exper3  ')
    print('------------------------------')
    config = init_config()

    def exper3_with_p(p, title, filename):
        # 最后的保存结果
        epsilons = []
        min_epsilons = []
        max_epsilons = []
        # 世界变化率
        log10gammas = np.linspace(0, 2, 16, endpoint=False)
        gammas = 10 ** log10gammas
        for k in [inf, 4, 1]:
            epsilons.append([])
            min_epsilons.append([])
            max_epsilons.append([])
            for gamma in gammas:
                new_config = {**config, 'p': p, 'k': k, 'gamma': gamma}
                epsilon, min_epsilon, max_epsilon = run(new_config)
                epsilons[-1].append(epsilon)
                min_epsilons[-1].append(min_epsilon)
                max_epsilons[-1].append(max_epsilon)
        plt.plot(log10gammas, epsilons[0], linestyle='-', marker='D',
                markersize=5, linewidth=2, color='cornflowerblue', label='bold')
        plt.fill_between(log10gammas, min_epsilons[0], max_epsilons[0], color='cornflowerblue', alpha=0.2) # type: ignore
        plt.plot(log10gammas, epsilons[1], linestyle='--', marker='^',
                markersize=5, linewidth=2, color='brown', label='normal')
        plt.fill_between(log10gammas, min_epsilons[1], max_epsilons[1], color='brown', alpha=0.2) # type: ignore
        plt.plot(log10gammas, epsilons[2], linestyle='-', marker='s',
                markersize=5, linewidth=2, color='lightseagreen', label='cautious')
        plt.fill_between(log10gammas, min_epsilons[2], max_epsilons[2], color='lightseagreen', alpha=0.2) # type: ignore
        plt.legend()
        plt.title(title)
        plt.ylabel(r'$\epsilon$')
        plt.xlabel(r'$\log_{10}\gamma$')
        plt.grid()
        plt.savefig(filename, dpi=200)
        # plt.show()
        plt.close()

    exper3_with_p(p=4, title='Figure 5: Effect of Degree of Boldness (p = 4)', filename='images/figure5.png')
    exper3_with_p(p=2, title='Figure 6: Effect of Degree of Boldness (p = 2)', filename='images/figure6.png')
    exper3_with_p(p=1, title='Figure 7: Effect of Degree of Boldness (p = 1)', filename='images/figure7.png')

    print('------------------------------')
    print('  exper3 completed  ')
    print('------------------------------')

def exper4():
    # 初始化实验相关配置
    print('------------------------------')
    print('  exper4  ')
    print('------------------------------')
    config = init_config()

    def exper4_with_p(p, title, filename):
        # 最后的保存结果
        epsilons = []
        min_epsilons = []
        max_epsilons = []
        # 世界变化率
        log10gammas = np.linspace(0, 2, 16, endpoint=False)
        gammas = 10 ** log10gammas
        for reaction_strategy in ['blind', 'disappear', 'nearer_hole', 'any_hole']:
            epsilons.append([])
            min_epsilons.append([])
            max_epsilons.append([])
            for gamma in gammas:
                new_config = {**config, 'p': p, 'k': inf, 'gamma': gamma, 'reaction_strategy': reaction_strategy}
                epsilon, min_epsilon, max_epsilon = run(new_config)
                epsilons[-1].append(epsilon)
                min_epsilons[-1].append(min_epsilon)
                max_epsilons[-1].append(max_epsilon)
        plt.plot(log10gammas, epsilons[0], linestyle='-', marker='D',
                markersize=5, linewidth=2, color='cornflowerblue', label='blind commitment')
        plt.fill_between(log10gammas, min_epsilons[0], max_epsilons[0], color='cornflowerblue', alpha=0.2) # type: ignore
        plt.plot(log10gammas, epsilons[1], linestyle='--', marker='^',
                markersize=5, linewidth=2, color='brown', label='notices target disappearance')
        plt.fill_between(log10gammas, min_epsilons[1], max_epsilons[1], color='brown', alpha=0.2) # type: ignore
        plt.plot(log10gammas, epsilons[2], linestyle='-', marker='s',
                markersize=5, linewidth=2, color='lightseagreen', label='target dis. or nearer hole')
        plt.fill_between(log10gammas, min_epsilons[2], max_epsilons[2], color='lightseagreen', alpha=0.2) # type: ignore
        plt.plot(log10gammas, epsilons[3], linestyle='-', marker='v',
                markersize=5, linewidth=2, color='mediumvioletred', label='target dis. or any new hole')
        plt.fill_between(log10gammas, min_epsilons[3], max_epsilons[3], color='mediumvioletred', alpha=0.2) # type: ignore
        plt.legend()
        plt.title(title)
        plt.ylabel(r'$\epsilon$')
        plt.xlabel(r'$\log_{10}\gamma$')
        plt.grid()
        plt.savefig(filename, dpi=200)
        # plt.show()
        plt.close()

    exper4_with_p(p=2, title='Figure 8: Effect of Reaction Strategy (p = 2)', filename='images/figure8.png')
    exper4_with_p(p=1, title='Figure 9: Effect of Reaction Strategy (p = 1)', filename='images/figure9.png')

    # 最后的保存结果
    epsilons = []
    min_epsilons = []
    max_epsilons = []
    # 世界变化率
    log10gammas = np.linspace(0, 2, 16, endpoint=False)
    gammas = 10 ** log10gammas
    for k in [inf, 4, 1]:
        epsilons.append([])
        min_epsilons.append([])
        max_epsilons.append([])
        for gamma in gammas:
            new_config = {**config, 'p': 1, 'k': k, 'gamma': gamma, 'reaction_strategy': 'disappear'}
            epsilon, min_epsilon, max_epsilon = run(new_config)
            epsilons[-1].append(epsilon)
            min_epsilons[-1].append(min_epsilon)
            max_epsilons[-1].append(max_epsilon)
    plt.plot(log10gammas, epsilons[0], linestyle='-', marker='D',
            markersize=5, linewidth=2, color='cornflowerblue', label='bold')
    plt.fill_between(log10gammas, min_epsilons[0], max_epsilons[0], color='cornflowerblue', alpha=0.2) # type: ignore
    plt.plot(log10gammas, epsilons[1], linestyle='--', marker='^',
            markersize=5, linewidth=2, color='brown', label='normal')
    plt.fill_between(log10gammas, min_epsilons[1], max_epsilons[1], color='brown', alpha=0.2) # type: ignore
    plt.plot(log10gammas, epsilons[2], linestyle='-', marker='s',
            markersize=5, linewidth=2, color='lightseagreen', label='cautious')
    plt.fill_between(log10gammas, min_epsilons[2], max_epsilons[2], color='lightseagreen', alpha=0.2) # type: ignore
    plt.legend()
    plt.title('Figure 10: Effect of Boldness (reactive agent, p = 1)')
    plt.ylabel(r'$\epsilon$')
    plt.xlabel(r'$\log_{10}\gamma$')
    plt.grid()
    plt.savefig('images/figure10.png', dpi=200)
    # plt.show()
    plt.close()
    print('------------------------------')
    print('  exper4 completed  ')
    print('------------------------------')


def test():
    config = init_config()
    epsilon, min_epsilon, max_epsilon = run(
        {**config, 'gamma': 15, 'p': 1, 'k': inf, 'visualize': True, 'visualize_result': True, 'is_tqdm': True})
    print(f'{epsilon = }')


if __name__ == '__main__':
    test()
    exper1()
    exper2()
    exper3()
    exper4()