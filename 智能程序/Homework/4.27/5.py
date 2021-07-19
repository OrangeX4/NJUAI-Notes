# 最小二乘法
import numpy as np
from numpy.core.defchararray import array  # 科学计算库
# python中已经有最小二乘方法的函数，只需要按照规定调用即可
from scipy.optimize import least_squares  # 引入最小二乘法算法
import os
from typing import Tuple

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

## 需要拟合的函数func: 指定函数的形状
# def func(p, x):
#     return (x * np.array([p[:-1]])).sum(axis=1) + p[-1]
def func(p, x):
    return (x * np.array([p])).sum(axis=1)

# 偏差函数：x,y都是列表
def loss(p, x, y):
    return func(p, x) - y


# 参数的初始值, 可以任意设定, p0 的值会影响 cost 的值
p0 = [1.0] * 13

# 把 loss 函数中除了p0以外的参数打包到args中(使用要求)
result = least_squares(loss, p0, args=(x_array, y_array))

p = np.array(result.x)

def forecast(x):
    return sum(x * p)

print(p)
print(str(forecast(x_array[0])) + ' ≈ ' + str(y_array[0]))
