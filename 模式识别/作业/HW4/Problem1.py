# %%
from liblinear.liblinearutil import *

# %%
mnist = svm_read_problem('mnist')
mnist_t = svm_read_problem('mnist.t')

# %%
# 使用默认参数训练模型
default_model = train(mnist[0], mnist[1])

# %%
# 在测试集上的准确率
print("default_model:")
p_label, p_acc, p_val = predict(mnist_t[0], mnist_t[1], default_model)

# %%
# 对每个训练和测试样例的特征值进行开根变换
def sqrt_data(data):
    sqrt_data = ([*data[0]], [*data[1]])
    for i in range(len(sqrt_data[1])):
        sqrt_data[1][i] = {key: sqrt_data[1][i][key] ** 0.5 for key in sqrt_data[1][i]}
    return sqrt_data

sqrt_mnist = sqrt_data(mnist)
sqrt_mnist_t = sqrt_data(mnist_t)

# %%
sqrt_model = train(sqrt_mnist[0], sqrt_mnist[1])

# %%
print("sqrt_model:")
sqrt_p_label, sqrt_p_acc, sqrt_p_val = predict(sqrt_mnist_t[0], sqrt_mnist_t[1], sqrt_model)
# %%
