# %% [markdown]
# ![](image/2021-04-18-14-39-14.png)
# ![](image/2021-04-18-15-44-41.png)

# %%
import numpy as np
import os
import matplotlib.pyplot as plt
from tqdm import tqdm

from typing import Tuple, List


def read_libsvm(name: str) -> Tuple[np.ndarray, np.ndarray]:
    '''
    Read libsvm file and return data.

    Parameters
    ----------
    name : str
        the file name of libsvm file

    Returns
    -------
    x : 2-dimension array
        the parameters
    y : 1-dimension array
        the values
    '''
    current_path = os.path.dirname(__file__)
    data_path = os.path.join(current_path, name)

    # 读取文件
    with open(data_path, "r", encoding="utf-8") as data_file:
        data = [line.strip().split() for line in data_file.readlines()]
        x = []
        y = []
        for line in data:
            x.append([float(variable.split(':')[1]) for variable in line[1:]])
            y.append(float(line[0]))
    return np.array(x), np.array(y)


x_array, y_array = read_libsvm('train.txt')


# %%
print(x_array.shape, y_array.shape)


# %%
class LinearModel(object):

    def __init__(self, weights: List[float]) -> None:
        '''
        Initiate weights list 'w' and the number of traits 'd'
        '''
        self.weights: np.ndarray = np.array(weights)

    def forcast(self, x: np.ndarray) -> float:
        '''
        Forcast the value

        math function: $h(x)=\sum_{i=1}^n w_i * x_i$
        '''
        return sum([self.weights[i] * x[i] for i in range(len(self.weights))])

    def loss(self, x_array: np.ndarray, y_array: np.ndarray) -> float:
        '''
        Get the loss

        math function:

        $f(x)=\\frac{1}{2}\sum_{i=1}^m(\sum_{j=1}^n w_j * x_j^i-y^i)^2$
        '''
        sum_value = 0
        for i in range(len(y_array)):
            sum_value += (self.forcast(x_array[i]) - y_array[i]) ** 2
        return 0.5 * sum_value

    def average_loss(self, x_array: np.ndarray, y_array: np.ndarray) -> float:
        '''
        Get the average loss
        '''
        return (1 / len(y_array)) * 2 * self.loss(x_array, y_array)

    def update(self, x_array: np.ndarray, y_array: np.ndarray, learning_rate: float) -> None:
        '''
        Update weights by gradient
        '''
        new_weights = self.weights.copy()
        for j in range(len(self.weights)):
            new_weights[j] -= learning_rate * sum([(self.forcast(
                x_array[i]) - y_array[i]) * x_array[i][j] for i in range(len(y_array))])
        self.weights = new_weights


# %%
print('--------------------')
print('Test for LinearModel')
print('--------------------')
model = LinearModel([1] * 13)
print('w =', model.weights)
test_x = np.array([1] * 13)
print('x =', test_x)
print('h(x) =', model.forcast(test_x))
print('f(x) =', model.loss(x_array, y_array))
model.update(x_array, y_array, 0.001)
print('update 1')
print('w =', model.weights)
print('f(x) =', model.loss(x_array, y_array))
model.update(x_array, y_array, 0.001)
print('update 2')
print('w =', model.weights)
print('f(x) =', model.loss(x_array, y_array))
print('--------------------\n')


# %%
print('Initial Model')
model = LinearModel([0.0] * 13)
print('w =', model.weights)

idx = [0]
mses = [model.loss(x_array, y_array)]
learning_rate = 0.001
start = 1

# %%
batch = 200
for i in tqdm(range(start, start + batch)):
    model.update(x_array, y_array, learning_rate)
    idx.append(i)
    mses.append(model.average_loss(x_array, y_array))
start += batch

plt.plot(idx, mses)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.xlabel('迭代次数')
plt.ylabel('预测误差')
plt.show()

print('Average Loss:', model.average_loss(x_array, y_array))


# %%
print(model.loss(x_array, y_array))
print(model.weights)


# %%
