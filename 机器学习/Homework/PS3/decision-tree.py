import numpy as np
from typing import Any, Callable, Counter, List, Dict

# # 第二题

# config = {
#     'attr_names': ['X', 'Y', 'Z', 'f'],
#     'attr_ranges': [[0, 1], [0, 1], [0, 1], [0, 1]],
# }

# raw_attr = [0, 1, 2]

# raw_data = np.array([
#     [1, 0, 1, 1],
#     [1, 1, 0, 0],
#     [0, 0, 0, 0],
#     [0, 1, 1, 1],
#     [0, 1, 0, 0],
#     [0, 0, 1, 0],
#     [1, 0, 0, 0],
#     [1, 1, 1, 0],
# ])

# # 第三题

# config = {
#     'attr_names': ['X', 'Y', 'f'],
#     'attr_ranges': [[0, 1], [0, 1], [0, 1]],
# }

# raw_attr = [0, 1]

# raw_data = np.array([
#     [1, 1, 1],
#     [0, 1, 1],
#     [1, 0, 0],
#     [1, 0, 0],
#     [0, 0, 1],
# ])

# 第四题
# 缺失值默认为 -1

config = {
    'attr_names': ['X', 'Y', 'Z', 'f'],
    'attr_ranges': [[0, 1], [0, 1], [0, 1], [0, 1]],
}

raw_attr = [0, 1, 2]

raw_data = np.array([
    [1, 0, -1, 1],
    [-1, 1, 0, 0],
    [0, -1, 0, 0],
    [0, 1, 1, 1],
    [-1, 1, 0, 0],
    [0, 0, -1, 0],
    [1, -1, 0, 0],
    [1, 1, 1, 0],
])


class DecisionTree:

    def __init__(self, data: np.ndarray, attr: List[int], config: Dict[str, Any] = None, weights: Dict = None, before_generate: Callable = None) -> None:
        '''
        :param data: 数据集
        :param attr: 属性集
        :param config: 配置
        '''
        self.config = {
            'label_index': -1,
            # 'decision_fn': 'gain',
            # 'decision_fn': 'gini',
            'decision_fn': 'gain_with_weight',
        }
        self.data = data
        self.attr = attr
        self.config.update(config)
        self.children = {}
        self.label = None
        self.is_leaf = False
        if weights == None:
            self.init_weights()
        else:
            self.weights = weights.copy()
        if before_generate:
            before_generate(self)
        self.tree_generate()

    def init_weights(self) -> None:
        '''
        为 data 的每个值初始化权重为 1
        '''
        self.weights = {}
        for x in self.data:
            self.set_weight(x, 1.0)

    def weight(self, x) -> float:
        '''
        取权重
        '''
        return self.weights[tuple(x)]

    def set_weight(self, x, w) -> float:
        '''
        置权重
        '''
        self.weights[tuple(x)] = w

    def rho(self, data, raw_data):
        '''
        无缺失值样本所占比例
        '''
        return sum([self.weight(x) for x in data]) / sum([self.weight(x) for x in raw_data])

    def p_k(self, data, k):
        '''
        无缺失值样本中第 k 类所占比例
        '''
        return sum([self.weight(x) for x in data[data[:, -1] == k]]) / sum([self.weight(x) for x in data])

    def r_v(self, data, attr, v):
        '''
        无缺失值样本中属性 attr 的值为 v 的样本所占比例
        '''
        return sum([self.weight(x) for x in data[data[:, attr] == v]]) / sum([self.weight(x) for x in data])

    def entropy_with_weight(self, data: np.ndarray, label_index=-1) -> float:
        '''
        带权重计算熵
        :param data: 数据集
        :return: 熵
        '''
        # count the number of each label
        label_counts = Counter(data[:, label_index])
        # calculate the entropy
        entropy = -sum([(self.p_k(data, label)) *
                        np.log2(self.p_k(data, label)) for label in label_counts])
        return entropy

    def gain_with_weight(self, raw_data: np.ndarray, attr: int, attr_range: List[int] = None, label_index=-1) -> float:
        '''
        带权重计算信息增益
        :param data: 数据集
        :param attr: 属性
        :return: 信息增益
        '''
        # init data by remove value -1
        data = raw_data[raw_data[:, attr] != -1]
        # set default attr_range
        if attr_range is None:
            # remove duplicates
            attr_range = np.unique(data[:, attr])
        # calculate the entropy
        entropy = self.entropy_with_weight(data, label_index)
        # convert value_counts to a vector in order of attr_range
        value_vector = np.array([self.r_v(data, attr, val)
                                 for val in attr_range])
        # calculate the entropy of each attribute value
        attr_entropies = np.array([self.entropy_with_weight(
            data[data[:, attr] == val], label_index) for val in attr_range])
        # calculate the sum of attr_entropies with ratio of value_vector
        attr_entropy = value_vector @ attr_entropies
        # calculate the information gain
        gain = self.rho(data, raw_data) * (entropy - attr_entropy)
        return gain

    @staticmethod
    def entropy(data: np.ndarray, label_index=-1) -> float:
        '''
        计算熵
        :param data: 数据集
        :return: 熵
        '''
        # count the number of each label
        label_counts = Counter(data[:, label_index])
        # calculate the entropy
        entropy = -sum([(label_counts[label] / len(data)) *
                        np.log2(label_counts[label] / len(data)) for label in label_counts])
        return entropy

    @staticmethod
    def gain(data: np.ndarray, attr: int, attr_range: List[int] = None, label_index=-1) -> float:
        '''
        计算信息增益
        :param data: 数据集
        :param attr: 属性
        :return: 信息增益
        '''
        # set default attr_range
        if attr_range is None:
            # remove duplicates
            attr_range = np.unique(data[:, attr])
        # calculate the entropy
        entropy = DecisionTree.entropy(data, label_index)
        # count the number of each label
        value_counts = Counter(data[:, attr])
        # convert value_counts to a vector in order of attr_range
        value_vector = np.array([value_counts[val] for val in attr_range])
        # calculate the entropy of each attribute value
        attr_entropies = np.array([DecisionTree.entropy(
            data[data[:, attr] == val], label_index) for val in attr_range])
        # calculate the sum of attr_entropies with ratio of value_vector
        attr_entropy = (value_vector / data.shape[0]) @ attr_entropies
        # calculate the information gain
        gain = entropy - attr_entropy
        return gain

    @staticmethod
    def gain_cont_with_mid_val(data: np.ndarray, attr: int, mid_val: float, label_index=-1) -> float:
        '''
        计算连续属性的信息增益
        :param data: 数据集
        :param attr: 连续属性
        :param mid_val: 中点划分值
        :return: 信息增益
        '''
        # calculate the entropy
        entropy = DecisionTree.entropy(data, label_index)
        # negative data
        neg_data = data[data[:, attr] <= mid_val]
        # positive data
        pos_data = data[data[:, attr] > mid_val]
        # convert value_counts to a vector in order of attr_range
        value_vector = np.array([len(neg_data), len(pos_data)])
        # calculate the entropy of each attribute value
        attr_entropies = np.array([DecisionTree.entropy(
            cur_data) for cur_data in [neg_data, pos_data]])
        # calculate the sum of attr_entropies with ratio of value_vector
        attr_entropy = (value_vector / data.shape[0]) @ attr_entropies
        # calculate the information gain
        gain = entropy - attr_entropy
        return gain

    @staticmethod
    def gain_cont(data: np.ndarray, attr: int, label_index=-1) -> float:
        # calculate mid_vals from data
        sorted_vals = sorted(data[:, attr])
        mid_vals = [(sorted_vals[i] + sorted_vals[i + 1]) /
                    2 for i in range(len(sorted_vals) - 1)]
        # get the best mid_val
        gains = [(mid_val, DecisionTree.gain_cont_with_mid_val(data, attr, mid_val, label_index))
                 for mid_val in mid_vals]
        return gains

    def gain_fn(self):
        # get the best attribute
        self.gains = [(attr, self.gain(self.data, attr, self.config['attr_ranges'][attr],
                                       self.config['label_index'])) for attr in self.attr]
        return max(self.gains, key=lambda x: x[1])[0]

    def gain_with_weight_fn(self):
        # get the best attribute
        self.gains = [(attr, self.gain_with_weight(self.data, attr, self.config['attr_ranges'][attr],
                                                   self.config['label_index'])) for attr in self.attr]
        return max(self.gains, key=lambda x: x[1])[0]

    @staticmethod
    def gini(data: np.ndarray, label_index=-1) -> float:
        '''
        计算基尼系数
        :param data: 数据集
        :return: 基尼系数
        '''
        # count the number of each label
        label_counts = Counter(data[:, label_index])
        # calculate the gini
        gini = 1 - sum([(label_counts[label] / len(data))
                        ** 2 for label in label_counts])
        return gini

    @staticmethod
    def gini_index(data: np.ndarray, attr: int, label_index=-1):
        '''
        计算基尼指数
        :param data: 数据集
        :param attr: 属性
        :return: 基尼指数
        '''
        # count the number of each value of attr
        value_counts = Counter(data[:, attr])
        # calculate the gini index
        gini_index = sum([(value_counts[val] / data.shape[0]) *
                          DecisionTree.gini(data[data[:, attr] == val]) for val in value_counts])
        return gini_index

    def gini_fn(self):
        # get the best attribute
        self.ginis = [(attr, self.gini_index(self.data, attr,
                                             self.config['label_index'])) for attr in self.attr]
        return min(self.ginis, key=lambda x: x[1])[0]

    @property
    def decision_fn(self) -> Callable[[], int]:
        '''
        决策函数, 返回 index
        '''
        # type is function
        if self.config['decision_fn'] is not None and callable(self.config['decision_fn']):
            return self.config['decision_fn']
        elif type(self.config['decision_fn']) == str:
            if self.config['decision_fn'] == 'gain':
                return self.gain_fn
            elif self.config['decision_fn'] == 'gini':
                return self.gini_fn
            elif self.config['decision_fn'] == 'gain_with_weight':
                return self.gain_with_weight_fn
            else:
                raise ValueError('decision_fn must be gain or gini')
        else:
            raise ValueError('decision_fn must be gain or gini')

    def tree_generate(self):
        '''
        根据数据集生成决策树
        '''
        attr = self.attr
        data = self.data
        if len(data) == 0:
            self.is_leaf = True
            self.label = None
            return
        labels = self.data[:, self.config['label_index']]
        if np.all(labels == labels[0]):
            self.is_leaf = True
            self.label = labels[0]
            return
        if len(attr) == 0 or np.all(data[:, attr] == data[:, attr][0]):
            self.is_leaf = True
            self.label = Counter(labels).most_common(1)[0][1]
            return
        self.best_attr = self.decision_fn()
        default_data = data[data[:, self.best_attr] == -1]
        for val in self.config['attr_ranges'][self.best_attr]:
            new_data = data[data[:, self.best_attr] == val]
            if len(default_data) != 0:
                new_data = np.vstack([new_data, default_data])
            new_attr = attr.copy()
            new_attr.remove(self.best_attr)
            if len(new_data) == 0:
                self.children[val] = DecisionTree(
                    new_data, new_attr, config=self.config, weights=self.weights)
                self.children[val].label = Counter(labels).most_common(1)[0][1]
            else:
                def update_weights(this: DecisionTree):
                    for x in default_data:
                        this.set_weight(x, this.r_v(
                            data[data[:, self.best_attr] != -1], self.best_attr, val) * this.weight(x))
                self.children[val] = DecisionTree(
                    new_data, new_attr, config=self.config, weights=self.weights, before_generate=update_weights)

    def print(self, indent=0):
        '''
        打印决策树
        '''
        print(' ' * indent + 'data: ' + str(self.data).replace('\n', '', -1))
        print(' ' * indent + 'entropy: ' + str(self.entropy(self.data)))
        if self.is_leaf:
            print(' ' * indent + 'label: ' + str(self.label))
        else:
            if self.config['decision_fn'] == 'gain' or self.config['decision_fn'] == 'gain_with_weight':
                print(' ' * indent + 'gains: ' + str(self.gains))
            elif self.config['decision_fn'] == 'gini':
                print(' ' * indent + 'ginis: ' + str(self.ginis))
            print(' ' * indent + 'best_attr: ' + str(self.best_attr))
            for val, child in self.children.items():
                print(' ' * indent + 'val: ' + str(val))
                child.print(indent + 4)


tree = DecisionTree(raw_data, raw_attr, config)
tree.print()
