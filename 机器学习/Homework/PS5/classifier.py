from typing import Counter
from math import log
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from scipy import optimize
from matplotlib import pyplot as plt

# 0. 加载数据
feature, label = datasets.load_iris(return_X_y=True)
feature_train, feature_test, label_train, label_test = \
    train_test_split(feature, label, test_size=0.2, random_state=0)


# 1. 检查训练集上的类别分布情况, 并基于多项式分布假设对 P(y) 做极大似然估计
print("-----------------------------------------------------")
print(Counter(label_train))
# optimize -p_0**39 * p_1**37 * p_2**44 by scipy.optimize.minimize
# and p_0 + p_1 + p_2 = 1, 0 <= p_i <= 1
result = optimize.minimize(
    lambda p: -(39. * log(p[0]) + 37. * log(p[1]) + 44. * log(p[2])),
    x0=(0.33, 0.33, 0.34), bounds=((0., 1.), (0., 1.), (0., 1.)),
    constraints=({'type': 'eq', 'fun': lambda p: 1. - sum(p)}))
print(f"p = {result.x}")
print(f"f = {result.fun}")


# 2. 使用 sklearn 中的 GaussianNB 类构建分类器, 并在测试集上测试性能
print("-----------------------------------------------------")
GNB_classifier = GaussianNB()
GNB_classifier.fit(feature_train, label_train)
print(f"score: {GNB_classifier.score(feature_test, label_test)}")


# 3. 在 GaussianNB 手动指定类别先验为三个类上的均匀分布, 再次测试性能
print("-----------------------------------------------------")
GNB_classifier = GaussianNB(priors=[1./3., 1./3., 1./3.])
GNB_classifier.fit(feature_train, label_train)
print(f"score: {GNB_classifier.score(feature_test, label_test)}")


# 4. 检查每个类别下特征的数值分布, 用以讨论该如何选择类条件概率的形式
#    画 3 x 4 个图像 P_{ij}, 代表着第 i 个类别下第 j 个特征的分布的直方图
print("-----------------------------------------------------")
plt.subplots_adjust(wspace=0.35, hspace=1.0)
for i in range(3):
    for j in range(4):
        # 第 (i, j) 张图
        plt.subplot(3, 4, i * 4 + j + 1)
        plt.hist(feature_train[label_train == i][:, j])
        plt.title(f"P(x{j+1}|{i})")
plt.show()

