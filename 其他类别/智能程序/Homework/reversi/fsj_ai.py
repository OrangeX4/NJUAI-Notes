from math import inf
from random import randint
from copy import deepcopy
from typing import List


def fsj_ai(board: List[List[int]], current: int, newest: List[int], reversal: List[List[int]], prompt) -> List[int]:
    '''
    输入参数:
    board: 二维数组, 8 x 8 的棋盘数据, 0 代表空, 1 代表黑棋, 2 代表白棋.
    current: 当前你的棋子颜色, 1 代表黑棋, 2 代表白棋.
    最重要的就是上面两个, 其他输入无关紧要.
    newest: 对方下的最后一个棋子位置.
    reversal: 对方上一次翻转的棋子.
    prompt: 当前你可以下的位置, 即提示. 一般来说你并不需要它.

    返回:
    返回你要下的位置, 例如 [2, 1] 或 (2, 1), 要注意是从 0 开始的.
    '''

    # 获取可放置位置的数据
    board = [[-1 if piece == 2 else piece for piece in line] for line in board]
    current = -1 if current == 2 else current

    # 如果可以放角点, 直接放角点
    movables = get_movables(board, current)
    # for corner in [(0, 0), (0, 7), (7, 0), (7, 7)]:
    #     if corner in movables.keys():
    #         return corner
    
    # alpha-beta 剪枝
    # 可行点的个数到迭代深度的映射
    movables_number = len(movables.keys())
    if movables_number < 5:
        return alpha_beta(board, current, -10000, 10000, 6)[1]
    elif movables_number < 10:
        return alpha_beta(board, current, -10000, 10000, 5)[1]
    else:
        return alpha_beta(board, current, -10000, 10000, 4)[1]

def get_movables(board, current):
    # 对于一个方向是否可以放置, 比如向右边是 dy = 0, dx = 1 的情况
    def get_movable_by_step(i, j, dy, dx):
        result = []
        isEnd = False
        while True:
            i += dy
            j += dx
            if 0 > i or i > 7 or 0 > j or j > 7 or board[i][j] == 0:
                break
            elif board[i][j] == -current:
                result.append((i, j))
                isEnd = True
            elif board[i][j] == current and isEnd == False:
                break
            elif board[i][j] == current and isEnd == True:
                return result
        return []

    # 八个不同的方向是否可行
    def get_movable_for_all_direction(i, j):
        result = []
        for dy, dx in [(dy, dx) for dy in range(-1, 2) for dx in range(-1, 2) if dy != 0 or dx != 0]:
            result += get_movable_by_step(i, j, dy, dx)
        return result

    # 对棋盘的每一个空格进行判断
    result = {}
    for i in range(8):
        for j in range(8):
            lst = get_movable_for_all_direction(i, j)
            if board[i][j] == 0 and len(lst) > 0:
                result[(i, j)] = lst
    return result
    

def get_new_board(board, current, newest, reversals):
    board = deepcopy(board)
    board[newest[0]][newest[1]] = current
    for reversal in reversals:
        board[reversal[0]][reversal[1]] = current
    return board


def evaluate(board, current):
    '''
    评估函数, 用于评估当前局面.
    常用策略有角点, 稳定子, 前沿子, 行动力.
    '''
    # 行动力, 即可以走的步数
    mobility = len(get_movables(board, current).keys())

    # 前沿子, 即周围至少有一个空格的棋子, 这种棋子容易被吃掉
    frontier = 0
    def is_frontier(i, j):
        for dy, dx in [(dy, dx) for dy in range(-1, 2) for dx in range(-1, 2) if dy != 0 or dx != 0]:
            if board[i + dy][j + dx] != 0:
                return True
        return False
    # 遍历时可以去掉边缘
    for i in range(1, 7):
        for j in range(1, 7):
            # 棋盘上的棋子不为空时, 判断前沿子
            if not board[i][j] == 0 and is_frontier(i, j):
                # 容易被吃掉, 所以应该要取反
                frontier -= board[i][j] * current

    # 角点和稳定子
    corner = 0
    steady = 0
    corner_map = [
        # 角点 i, j, 偏移方向 dy, dx
        [0, 0, 1, 1],
        [0, 7, 1, -1],
        [7, 0, -1, 1],
        [7, 7, -1, -1]
    ]
    for corner_i, corner_j, dy, dx in corner_map:
        if board[corner_i][corner_j] == 0:
            # 角点为空时, 如果下了临角点或对角点, 这些点很危险
            corner += board[corner_i][corner_j + dx] * current * -3
            corner += board[corner_i + dy][corner_j] * current * -3
            corner += board[corner_i + dy][corner_j + dx] * current * -6
            # 角点为空时, 如果下了隔角点, 这些点很好
            corner += board[corner_i][corner_j + 2 * dx] * current * 4
            corner += board[corner_i + 2 * dy][corner_j] * current * 4
            corner += board[corner_i + dy][corner_j + 2 * dx] * current * 2
            corner += board[corner_i + 2 * dy][corner_j + dx] * current * 2
        else:
            i, j = corner_i, corner_j
            # 角点的权值
            corner += board[corner_i][corner_j] * current * 15
            # 角点不为空时, 处理稳定子, 为了简化运算, 仅仅考虑边稳定子
            current_color = board[corner_i][corner_j]
            while 0 <= i <= 7 and board[i][corner_j] == current_color:
                steady += current * current_color
                i += dy
            while 0 <= j <= 7 and board[corner_i][j] == current_color:
                steady += current * current_color
                j += dx
    
    
    # 以一定的权重相乘之后返回
    return 8 * corner + 12 * steady + 8 * mobility + 4 * frontier


def get_score(board, current):
    black_count = 0
    white_count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                black_count += 1
            elif board[i][j] == -1:
                white_count += 1
    # 反正赢了就不用考虑比分来估值了
    return (black_count - white_count) * current * 10000


# 进行 Hash 缓存
hash_board_map = {}
def set_hash_board(board, current, depth, alpha, beta, value, pos):
    hash_board_map[tuple([tuple([0 if piece == 0 else (1 if piece == current else -1) for piece in line]) for line in board] + [depth, alpha, beta])] = (value, pos)

def get_hash_board(board, current, depth, alpha, beta):
    key = tuple([tuple([0 if piece == 0 else (1 if piece == current else -1) for piece in line]) for line in board] + [depth, alpha, beta])
    return hash_board_map.get(key)


def alpha_beta(board, current, alpha, beta, depth, is_pass = False):
    '''
    alpha-beta 剪枝算法
    参数:
    board: 棋盘数据, 0 代表空格, 1 代表黑棋, -1 代表白棋;
    current: 当前是谁下, 传入 1 或 -1;
    alpha: 区间 [alpha, beta] 中的下限 alpha, 通过 -alpha 变成下层的 beta;
    beta: 区间 [alpha, beta] 中的上限 beta, 用于判断是否剪枝;
    depth: 深度, 一般设为 4 ~ 6;
    is_pass: 用于判断上次是否也无子可下, 上次和这次均无子可下的话, 游戏结束.
    返回值:
    best_value: 评分;
    best_position: 对应的位置, 如 (0, 2).
    '''
    # 查看缓存中有没有, 有就直接返回
    cache = get_hash_board(board, current, depth, alpha, beta)
    if cache:
        return cache
    # 保存好 alpha, beta, 便于后续缓存
    saved_alpha = alpha
    saved_beta = beta
    
    # 开始递归判断
    best_value = -inf
    best_position = (-1, -1)
    movables = get_movables(board, current)
    for movable, reversals in movables.items():
        # 初始化
        value = 0
        new_board = get_new_board(board, current, movable, reversals)
        if depth == 0:
            # 深度为 0 时, 评估当前局面, 并且取反以表示当前分数
            value = -evaluate(new_board, -current)
        else:
            # 深度不为 0 时, 递归调用
            value = -alpha_beta(new_board, -current, -beta, -alpha, depth - 1)[0]
        # 如果触发剪枝
        if value >= beta:
            return value, movable
        # 如果优于前面的下法
        if value > best_value:
            best_position = movable
            best_value = value
            # 更新下限
            if value > alpha:
                alpha = value
    # 无子可下的情况
    if len(movables) == 0:
        if is_pass:
            # 游戏结束, 直接获取最后结果, 并且得分是像 10000 这种极端分数
            best_value = get_score(board, current)
        else:
            # 没结束的话, 就继续呗
            best_value = -alpha_beta(board, -current, -beta, -alpha, depth, True)[0]
    
    # 处理意外情况, 随便选一个
    if best_position == (-1, -1) and len(movables.keys()) > 0:
        movables.keys()[randint(0, len(movables) - 1)]
    set_hash_board(board, current, depth, saved_alpha, saved_beta, best_value, best_position)
    return best_value, best_position
