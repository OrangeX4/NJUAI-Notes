import numpy as np
from typing import Any, Callable, Counter, List, Dict

config = {
    'attr_names': ['X', 'Y', 'Z', 'f'],
    'attr_ranges': [[0, 1], [0, 1], [0, 1], [0, 1]],
}

raw_attr = [0, 1, 2]

raw_data = np.array([
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0],
])


class DecisionTree:

    def __init__(self, data: np.ndarray, attr: List[int], config: Dict[str, Any] = None) -> None:
        '''
        :param data: 数据集
        :param attr: 属性集
        :param config: 配置
        '''
        self.config = {
            'label_index': -1,
            'decision_fn': 'gain',
            # 'decision_fn': 'gini',
        }
        self.data = data
        self.attr = attr
        self.config.update(config)
        self.children = {}
        self.label = None
        self.is_leaf = False
        self.tree_generate()

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
        entropy = DecisionTree.entropy(data)
        # count the number of each label
        value_counts = Counter(data[:, attr])
        # convert value_counts to a vector in order of attr_range
        value_vector = np.array([value_counts[val] for val in attr_range])
        # calculate the entropy of each attribute value
        attr_entropies = np.array([DecisionTree.entropy(
            data[data[:, attr] == val]) for val in attr_range])
        # calculate the sum of attr_entropies with ratio of value_vector
        attr_entropy = (value_vector / data.shape[0]) @ attr_entropies
        # calculate the information gain
        gain = entropy - attr_entropy
        return gain

    def gain_fn(self):
        # get the best attribute
        self.gains = [(attr, self.gain(self.data, attr, self.config['attr_ranges'][attr],
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
        labels = self.data[:, self.config['label_index']]
        if np.all(labels == labels[0]):
            self.is_leaf = True
            self.label = labels[0]
            return
        if len(attr) == 0 or np.all(data[:, attr] == data[:, attr][0]):
            self.is_leaf = True
            self.label = Counter(labels).most_common(1)[0][1]
        self.best_attr = self.decision_fn()
        for val in self.config['attr_ranges'][self.best_attr]:
            new_data = data[data[:, self.best_attr] == val]
            new_attr = attr.copy()
            new_attr.remove(self.best_attr)
            if len(new_data) == 0:
                self.children[val] = DecisionTree(
                    new_data, new_attr, self.config)
                self.children[val].label = Counter(labels).most_common(1)[0][1]
            else:
                self.children[val] = DecisionTree(
                    new_data, new_attr, self.config)

    def print(self, indent=0):
        '''
        打印决策树
        '''
        print(' ' * indent + 'data: ' + str(self.data).replace('\n', '', -1))
        # print(' ' * indent + 'entropy: ' + str(self.entropy(self.data)))
        if self.is_leaf:
            print(' ' * indent + 'label: ' + str(self.label))
        else:
            if self.config['decision_fn'] == 'gain':
                print(' ' * indent + 'gains: ' + str(self.gains))
            elif self.config['decision_fn'] == 'gini':
                print(' ' * indent + 'ginis: ' + str(self.ginis))
            print(' ' * indent + 'best_attr: ' + str(self.best_attr))
            for val, child in self.children.items():
                print(' ' * indent + 'val: ' + str(val))
                child.print(indent + 4)


tree = DecisionTree(raw_data, raw_attr, config)
tree.print()
