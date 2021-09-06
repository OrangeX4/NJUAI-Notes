from typing import Tuple
from sklearn import datasets  # 读取 sklearn 自带的数据集
from sklearn.decomposition import PCA  # PCA 降维
import matplotlib.pyplot as plt  # 用于可视化分析
import numpy as np

iris = datasets.load_iris()  # 读取 iris 数据集
X = iris.data 
y = iris.target

# 归一化
X = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))

# 取欧式距离
def get_distance(first_sample: np.ndarray, second_sample: np.ndarray):
        return ((first_sample - second_sample) ** 2).sum()

# 生成随机的 k 个样本, 用于 k-means 初始化
def generate_X_samples(k: int, X: np.ndarray):
    return X[[np.random.randint(0, X.shape[0]) for _ in range(k)]]
centers = generate_X_samples(3, X)

# 第一次样本分类
def get_sample_class(sample: np.ndarray, centers: np.ndarray):
    distances = [get_distance(sample, center) for center in centers]
    return distances.index(max(distances))

predict_y = np.array([get_sample_class(sample, centers) for sample in X])

# 重新计算中心
old_centers = generate_X_samples(3, X)
index_dict = {}
def recalculate_centers(X: np.ndarray, last_predict_y: np.ndarray) -> Tuple[np.ndarray]:
    index_dict = {}
    for i in range(len(last_predict_y)):
        if last_predict_y[i] in index_dict:
            index_dict[last_predict_y[i]].append(i)
        else:
            index_dict[last_predict_y[i]] = [i]
    return np.array([X[index].sum(axis=0) / len(X[index]) for index in index_dict.values()]), index_dict

# 一直计算直至稳定
while not np.allclose(old_centers[:len(centers)], centers):
    old_centers = centers
    centers, index_dict = recalculate_centers(X, predict_y)
    predict_y = np.array([get_sample_class(sample, centers) for sample in X])

# 可视化
# 降维
pca=PCA(n_components=2)
new_X = pca.fit_transform(X)

# 画图
for index in index_dict.values():
    part = new_X[index]
    x = part[:, 0]
    y = part[:, 1]
    plt.scatter(x, y, alpha=0.6)
plt.show()


