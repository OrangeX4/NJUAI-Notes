from sklearn import datasets  # 读取 sklearn 自带的数据集
from sklearn.model_selection import KFold  # 使用 sklearn 内含的 k 折函数
from collections import Counter  # 用于后续投票
import matplotlib.pyplot as plt  # 用于可视化分析
import numpy as np

iris = datasets.load_iris()  # 读取 iris 数据集
X = iris.data 
y = iris.target

class knn_classifier:

    def __init__(self, X_train: np.ndarray, y_train: np.ndarray, k: int):
        '''
        初始化 kNN 模型. 
        X_train: 训练数据的特征;
        y_train: 训练数据的标签;
        k: kNN 中 k 的取值, 即选取多少个邻居.
        '''

        # 进行数据归一化
        # 计算公式 x' = (x - min(x)) / (max(x) - min(x))
        self._min = X_train.min(axis=0)
        self._max = X_train.max(axis=0)
        self._X_train: np.ndarray = (X_train - self._min) / (self._max - self._min)
        self._y_train: np.ndarray = y_train
        self._k: int = k

    def get_distance(self, first_sample: np.ndarray, second_sample: np.ndarray):
        return ((first_sample - second_sample) ** 2).sum()

    # kNN 分类算法的实现
    def classify_sample(self, X_sample: np.ndarray):
        '''
        给定一个测试样本 X_sample, 通过 kNN 算法来预测它的类别并返回. 
        X_sample: 一个测试样本.
        '''

        # 进行数据归一化
        # 计算公式 x' = (x - min(x)) / (max(x) - min(x))
        X_sample = (X_sample - self._min) / (self._max - self._min)

        # 简单的遍历计算距离, 待优化
        distances = [self.get_distance(X_train_sample, X_sample) for X_train_sample in self._X_train]

        # 从小到大取出前 k 个数据的下标, 使用 np.argsort 函数
        index = np.argsort(distances)[:self._k]
        # 进行投票, 选出出现次数最多的类别
        count = Counter(y[index])
        return count.most_common()[0][0]


# 使用 k 折函数和 knn 的结合
def k_fold_knn(X: np.ndarray, y: np.ndarray, *, k: int, k_fold: int = 5) -> float:
    '''
    使用 k 折交叉验证来计算分类结果准确率, 返回准确率.
    X: 数据集的特征;
    y: 数据集的标签;
    k: kNN 中 k 的取值, 即选取多少个邻居.
    k_fold: 进行多少折验证, 默认为 5 折.
    '''
    # 初始化 k 折函数, 第一个参数是多少折, 第二个参数是随机数种子, 用于生成相同的随机数, 并且要设置 shuffle=True 才能生效
    kf = KFold(n_splits=k_fold, random_state=2021, shuffle=True)
    # 用于保存每一折算出来的正确率
    results = []
    for train_index, test_index in kf.split(X):
        # 每一折的训练集
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        knn = knn_classifier(X_train, y_train, k=k)

        # 获取预测分类结果
        y_predict = [knn.classify_sample(X_test_sample) for X_test_sample in X_test]

        # 将预测分类结果与正确分类数据比对,
        # 正确则为 1.0, 错误则为 0.0, 最后取平均值
        results.append(sum([1.0 if y_predict[i] == y_test[i] else 0.0 for i in range(len(y_test))]) / len(y_test))

    return sum(results) / len(results)

# 进行超参数 k 的 5 折交叉验证测试
k_values = range(1, 30, 2)
k_accuracy = [k_fold_knn(X, y, k=k) for k in k_values]

# 输出最优的 k 值
print('The best k is', k_values[k_accuracy.index(max(k_accuracy))])
print('The best accuracy is', max(k_accuracy))

# 生成折线图, 用于分析
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 'b': 颜色蓝色, 'o': 点形圆形, '-': 线形实线, 线条宽度为 2
plt.plot(k_values, k_accuracy, 'bo-', linewidth=2)
plt.xlabel('k')  # 横坐标轴的标题
plt.ylabel('accurate')  # 纵坐标轴的标题
plt.grid()  # 显示网格
plt.title('不同的 k 值的 kNN 分类准确率') # 图形的标题

# 显示图形
plt.show()

