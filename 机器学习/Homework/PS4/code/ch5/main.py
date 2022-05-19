import numpy as np
import time
from tqdm import tqdm

def plain_distance_function(X):
    # 直观的距离计算实现方法
    # 首先初始化一个空的距离矩阵D
    D = np.zeros((X.shape[0], X.shape[0]))
    # 循环遍历每一个样本对
    for i in range(X.shape[0]):
        for j in range(X.shape[0]):
            # 计算样本i和样本j的距离
            D[i, j] = np.sqrt(np.sum((X[i] - X[j])**2))
    return D


def plain_permutation_function(X, p):
    # 初始化结果矩阵, 其中每一行对应一个样本
    permuted_X = np.zeros_like(X)
    for i in range(X.shape[0]):
        # 采用循环的方式对每一个样本进行重排列
        permuted_X[i] = X[p[i]]
    return permuted_X


def tensor_distance_function(X: np.ndarray):
    return np.sqrt(((X[:, np.newaxis, :] - X[np.newaxis, :, :])**2).sum(axis=-1))


def matrix_distance_function(X: np.ndarray):
    # (xi - xj)^2 = xi^2 + xj^2 - 2 xi * xj
    ones = np.ones(X.shape).T
    M_xi_2 = np.square(X) @ ones
    M_xj_2 = M_xi_2.T
    M_xi_xj = X @ X.T
    # add a small number 1e-14 to avoid negative number
    M = M_xi_2 + M_xj_2 - 2 * M_xi_xj + 1e-10
    return np.sqrt(M)


def matrix_permutation_function(X: np.ndarray, p: np.ndarray):
    # matrix of permutation from p
    M_p = np.zeros((X.shape[0], X.shape[0]))
    for i in range(X.shape[0]):
        M_p[i, p[i]] = 1
    return M_p @ X
    

def test_distance_function_for_correctness(m: int, d: int, n: int):
    '''
    m: max number of vectors
    d: dimension of vector
    n: times of test
    '''
    for _ in tqdm(range(n)):
        # random matrix with shape (m, d)
        X = np.random.rand(m, d)
        plain_distance_matrix = plain_distance_function(X)
        tensor_distance_matrix = tensor_distance_function(X)
        matrix_distance_matrix = matrix_distance_function(X)
        assert np.allclose(plain_distance_matrix, tensor_distance_matrix, atol=1e-4)
        assert np.allclose(plain_distance_matrix, matrix_distance_matrix, atol=1e-4)


def test_permutation_function_for_correctness(m: int, d: int, n: int):
    '''
    m: max number of vectors
    d: dimension of vector
    n: times of test
    '''
    for _ in tqdm(range(n)):
        # random matrix with shape (m, d)
        X = np.random.rand(m, d)
        p = np.random.permutation(m)
        plain_permutation_matrix = plain_permutation_function(X, p)
        matrix_permutation_matrix = matrix_permutation_function(X, p)
        assert np.allclose(plain_permutation_matrix, matrix_permutation_matrix)


def test_distance_function_for_speed(m: int, d: int, n: int, distance_function):
    '''
    m: max number of vectors
    d: dimension of vector
    n: times of test
    distance_function: one of distance functions
    '''
    # record elapsed time
    start_time = time.time()
    for _ in tqdm(range(n)):
        # random matrix with shape (m, d)
        X = np.random.rand(m, d)
        distance_function(X)
    end_time = time.time()
    return end_time - start_time


def test_permutation_function_for_speed(m: int, d: int, n: int, permutation_function):
    '''
    m: max number of vectors
    d: dimension of vector
    n: times of test
    permutation_function: one of permutation functions
    '''
    # record elapsed time
    start_time = time.time()
    for _ in tqdm(range(n)):
        # random matrix with shape (m, d)
        X = np.random.rand(m, d)
        p = np.random.permutation(m)
        permutation_function(X, p)
    end_time = time.time()
    return end_time - start_time


def main():

    # test for correctness
    test_distance_function_for_correctness(m=10, d=10, n=10)
    test_permutation_function_for_correctness(m=10, d=10, n=10)

    # test elapsed time for distance function
    elapsed_time_for_small_and_plain = test_distance_function_for_speed(m=10, d=10, n=10000, distance_function=plain_distance_function)
    elapsed_time_for_small_and_matrix = test_distance_function_for_speed(m=10, d=10, n=10000, distance_function=matrix_distance_function)
    elapsed_time_for_small_and_tensor = test_distance_function_for_speed(m=10, d=10, n=10000, distance_function=tensor_distance_function)
    elapsed_time_for_large_and_plain = test_distance_function_for_speed(m=1000, d=1000, n=10, distance_function=plain_distance_function)
    elapsed_time_for_large_and_matrix = test_distance_function_for_speed(m=1000, d=1000, n=10, distance_function=matrix_distance_function)
    elapsed_time_for_large_and_tensor = test_distance_function_for_speed(m=1000, d=1000, n=10, distance_function=tensor_distance_function)

    print('elapsed time for small scale and plain function:', elapsed_time_for_small_and_plain)
    print('elapsed time for small scale and matrix function:', elapsed_time_for_small_and_matrix)
    print('elapsed time for small scale and tensor function:', elapsed_time_for_small_and_tensor)
    print('elapsed time for large scale and plain function:', elapsed_time_for_large_and_plain)
    print('elapsed time for large scale and matrix function:', elapsed_time_for_large_and_matrix)
    print('elapsed time for large scale and tensor function:', elapsed_time_for_large_and_tensor)

    # test elapsed time for permutation function
    elapsed_time_for_small_and_plain = test_permutation_function_for_speed(m=10, d=10, n=100000, permutation_function=plain_permutation_function)
    elapsed_time_for_small_and_matrix = test_permutation_function_for_speed(m=10, d=10, n=100000, permutation_function=matrix_permutation_function)
    elapsed_time_for_large_and_plain = test_permutation_function_for_speed(m=1000, d=1000, n=1000, permutation_function=plain_permutation_function)
    elapsed_time_for_large_and_matrix = test_permutation_function_for_speed(m=1000, d=1000, n=1000, permutation_function=matrix_permutation_function)

    print('elapsed time for small scale and plain function:', elapsed_time_for_small_and_plain)
    print('elapsed time for small scale and matrix function:', elapsed_time_for_small_and_matrix)
    print('elapsed time for large scale and plain function:', elapsed_time_for_large_and_plain)
    print('elapsed time for large scale and matrix function:', elapsed_time_for_large_and_matrix)


if __name__ == '__main__':
    main()