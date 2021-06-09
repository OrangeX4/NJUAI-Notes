# %%
from sklearn import datasets  # 读取 sklearn 自带的数据集
import matplotlib.pyplot as plt  # 用于可视化分析
import numpy as np

iris = datasets.load_iris()  # 读取 iris 数据集
X = iris.data 
y = iris.target

print(X, y)


# %%
def get_distance(first_sample: np.ndarray, second_sample: np.ndarray):
        return ((first_sample - second_sample) ** 2).sum()

        
# %%
def generate_X_samples(k: int, X: np.ndarray):
    return np.random.rand(k, X.shape[-1])

generate_X_samples(X, 10)