from __future__ import annotations
from typing import Iterable
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy


def dft(a: np.ndarray, n=None, inverse=False):
    '''
    discrete fourier transform
    '''
    if n is None:
        n = a.shape[0]
    # crop or pad
    if n > a.shape[0]:
        a = np.pad(a, (0, n - a.shape[0]), 'constant')
    elif n < a.shape[0]:
        a = a[:n]
    if inverse:
        return np.array([
            np.sum(a * np.exp(2j * np.pi * k * np.arange(n) / n))
            for k in range(n)])
    else:
        return np.array([
            np.sum(a * np.exp(-2j * np.pi * k * np.arange(n) / n))
            for k in range(n)])


def fft(a: np.ndarray, n=None, inverse=False) -> np.ndarray:
    '''
    a: array_like (n = 2^k)
    Input array, can be complex.

    n: int, optional
    Length of the transformed axis of the output.

    If n is smaller than the length of the input,
    the input is cropped.

    If it is larger, the input is padded with zeros.

    If n is not given, the length of the input
    along the axis specified by axis is used.

    inverse: bool, optional
    If True, compute the inverse FFT (n times).
    If False, compute the forward FFT.
    '''
    if n is None:
        n = a.shape[0]
    # crop or pad
    if n > a.shape[0]:
        a = np.pad(a, (0, n - a.shape[0]), 'constant')
    elif n < a.shape[0]:
        a = a[:n]
    # fft
    if n == 1:
        return a
    # 解决非 2 的幂次的问题
    if n % 2 != 0:
        return dft(a, n, inverse)
    else:
        # 分奇偶
        a_even = a[::2]
        a_odd = a[1::2]
        # 递归
        A_even = fft(a_even, n // 2, inverse)
        A_odd = fft(a_odd, n // 2, inverse)
        # 把所有的项相乘
        if inverse:
            W = np.exp(2j * np.pi * np.arange(n) / n)
        else:
            W = np.exp(-2j * np.pi * np.arange(n) / n)
        # W = W.reshape(-1, 1)
        return np.concatenate([A_even + W[:n // 2] * A_odd,
                               A_even + W[n // 2:] * A_odd])


def ifft(a: np.ndarray, n=None):
    '''
    a: array_like
    Input array, can be complex.

    n: int, optional
    Length of the transformed axis of the output.

    If n is smaller than the length of the input,
    the input is cropped.

    If it is larger, the input is padded with zeros.

    If n is not given, the length of the input
    along the axis specified by axis is used.
    '''
    if n is None:
        n = a.shape[0]
    return fft(a, n, inverse=True) / n


def fft2(a: np.ndarray, s: Iterable = (None, None), inverse=False) -> np.ndarray:
    '''
    2d fft
    a: array_like

    s: Iterable, optional
    Shape tuple (M, N) giving the size of the Fourier transform.

    If given, the input is either zero-padded or cropped to this size,
    before computing the Fourier transform.
    If not given, the size is inferred from a.

    inverse: bool, optional
    If True, compute the inverse FFT (n x m times).
    If False, compute the forward FFT.
    '''
    # 行变换
    F = np.array([fft(a[i], s[0], inverse) for i in tqdm(range(a.shape[0]))])
    # 列变换
    F = np.array([fft((F.T)[i], s[1], inverse)
                 for i in tqdm(range((F.T).shape[0]))]).T
    return F


def ifft2(a: np.ndarray, s: Iterable = (None, None)) -> np.ndarray:
    '''
    2d ifft
    a: array_like

    s: Iterable, optional
    Shape tuple (M, N) giving the size of the Fourier transform.

    If given, the input is either zero-padded or cropped to this size,
    before computing the Fourier transform.
    If not given, the size is inferred from a.
    '''
    s = (s[0] or a.shape[0], s[1] or a.shape[1])
    return fft2(a, s, inverse=True) / (s[0] * s[1])


def test_fft():
    a = np.arange(6)
    # print(fft(a))
    # print(np.fft.fft(a))
    assert np.allclose(fft(a), np.fft.fft(a))
    assert np.allclose(ifft(fft(a)), np.fft.ifft(np.fft.fft(a)))
    a = np.random.randn(6)
    assert np.allclose(fft(a), np.fft.fft(a))
    assert np.allclose(ifft(fft(a)), np.fft.ifft(np.fft.fft(a)))


def fspecial_gaussian(shape: Iterable, sigma: float) -> np.ndarray:
    """Generate a Gaussian filter.

    Args:
        shape (Iterable): The shape of the filter like ().
        sigma (float): The standard deviation of the Gaussian function.

    Returns:
        np.ndarray: The Gaussian filter.
    """
    m, n = [(ss - 1.) / 2. for ss in shape]
    y, x = np.ogrid[-m:m + 1, -n:n + 1]
    h = np.exp(-(x * x + y * y) / (2. * sigma * sigma))
    h[h < np.finfo(h.dtype).eps * h.max()] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h


# 填充 h(x,y) 到 h_p(x,y)
def pad_filter(h: np.ndarray, shape: Iterable) -> np.ndarray:
    """Pad the filter to the shape.

    Args:
        h (np.ndarray): The filter.
        shape (Iterable): The shape of the filter like ().

    Returns:
        np.ndarray: The padded filter.
    """
    if h.shape == shape:
        return h
    h_p = np.zeros(shape, dtype=h.dtype)
    # 将 h 放在 h_p 中心
    left = (shape[0] - h.shape[0]) // 2
    right = left + h.shape[0]
    top = (shape[1] - h.shape[1]) // 2
    bottom = top + h.shape[1]
    h_p[left:right, top:bottom] = h
    return h_p


# 在空间域执行卷积操作
def conv2(f: np.ndarray, h: np.ndarray) -> np.ndarray:
    """Convolve the filter h to the image f.

    Args:
        f (np.ndarray): The image.
        h (np.ndarray): The filter.

    Returns:
        np.ndarray: The convolved image.
    """
    # return np.array([[np.sum(
    #     f * np.roll(np.roll(h, i, axis=0), j, axis=1))
    #     for j in range(f.shape[1])]
    #     for i in tqdm(range(f.shape[0]))])
    N, M = f.shape
    n, m = h.shape
    # 填充 f(x,y) 到 f_p(x,y)
    f_p = np.pad(f, ((n - 1, n - 1), (m - 1, m - 1)), 'constant')
    g = np.zeros((N, M), dtype=f.dtype)
    for i in tqdm(range(N)):
        for j in range(M):
            g[i, j] = np.sum(f_p[i:i + n, j:j + m] * h)
    return g


# 空间滤波器转频率域滤波器
def freqz2(h: np.ndarray, use_numpy=False) -> np.ndarray:
    """Convert a 2D filter to the frequency domain.

    Args:
        h (np.ndarray): The 2D filter.

    Returns:
        np.ndarray: The 2D filter in the frequency domain.
    """
    # 1. 用 (-1)^(x+y) 来中心化
    x = np.arange(h.shape[0])
    y = np.arange(h.shape[1])
    h = h * (-1) ** (x[:, None] + y[None, :])
    # 2. 计算对应 DFT
    if use_numpy:
        H = np.fft.fft2(h)
    else:
        H = fft2(h)
    # 3. 用 (-1)^(u+v) 来中心化
    u = np.arange(H.shape[0])
    v = np.arange(H.shape[1])
    H = H * (-1) ** (u[:, None] + v[None, :])
    return H


def show_fourier_spectrum(F):
    '''
    显示傅里叶谱
    '''
    # 取傅里叶谱
    F = np.abs(F)
    # 取对数
    F = np.log(1 + F)
    # 显示图像
    plt.imshow(F, cmap='gray')


def show_matrix(h: np.ndarray):
    '''
    显示矩阵
    '''
    # show the matrix with a color map and numbers
    plt.imshow(h, cmap='gray')
    if h.shape[0] < 4 and h.shape[1] < 4:
        for i in range(h.shape[0]):
            for j in range(h.shape[1]):
                # 如果是整数, 显示整数, 否则显示小数点后 4 位
                if h[i, j] == int(h[i, j]):
                    plt.text(j, i, h[i, j], ha='center', va='center',
                         color='w' if h[i, j] < h.mean() else 'k')
                else:
                    plt.text(j, i, f'{h[i, j]:.4f}', ha='center', va='center',
                         color='w' if h[i, j] < h.mean() else 'k')


def my_imfilter(f: np.ndarray, P: int, Q: int, H: np.ndarray, use_numpy=False) -> np.ndarray:
    # 2. 为 f(x,y) 添加必要数量的 0, 此处省略
    M, N = f.shape
    # 3. 用 (-1)^(x+y) 乘以 f(x,y) 移到变换中心
    x = np.arange(M)[:, None]
    y = np.arange(N)[None, :]
    f = f * (-1) ** (x + y)
    # 4. 计算 f(x,y) 的傅里叶变换得到 F(u,v)
    if use_numpy:
        F = np.fft.fft2(f, (P, Q))
    else:
        F = fft2(f, (P, Q))
    # 5. 生成一个频域滤波器 H(u,v),
    #    并用阵列相乘形成 G(u,v) = H(u,v) * F(u,v)
    G = H * F
    # 6. 得到 g_p(x,y), 即 G(u,v) 的傅里叶逆变换,
    #    转换为实部, 并乘上 (-1)^(x+y)
    x = np.arange(P)[:, None]
    y = np.arange(Q)[None, :]
    if use_numpy:
        g_p = np.fft.ifft2(G).real * (-1) ** (x + y)
    else:
        g_p = ifft2(G).real * (-1) ** (x + y)
    # 7. 截取 g_p(x,y) 的左上部分 (M x N), 得到 g(x,y)
    return g_p[:M, :N]


def test_operator(
        img_name: str,
        operator_name: str,
        f: np.ndarray,
        h: np.ndarray,
        use_numpy=True,
        use_scipy=False,
        is_save=True,
        is_show=True):
    '''
    测试不同的算子 (空间域和频率域)
    '''
    # plt 清屏
    plt.clf()
    plt.subplots_adjust(wspace=0.4, hspace=0.2)
    # 显示六张图像
    plt.subplot(2, 3, 1)
    plt.imshow(f, cmap='gray')
    plt.title('f(x,y)')
    M, N = f.shape

    # 空间滤波器转频率域滤波器
    P, Q = M + h.shape[0] - 1, N + h.shape[1] - 1
    # 显示算子
    plt.subplot(2, 3, 2)
    show_matrix(h)
    # 显示标题
    plt.title(operator_name)
    # 获取填充后的滤波器
    h_p = pad_filter(h, (P, Q))
    # 转换到频域
    H = freqz2(h_p, use_numpy=use_numpy)
    # 显示滤波器
    plt.subplot(2, 3, 3)
    show_fourier_spectrum(H)
    plt.title('H(u,v)')

    # 进行频域滤波
    g = my_imfilter(f, P, Q, H, use_numpy=use_numpy)
    plt.subplot(2, 3, 4)
    plt.imshow(g, cmap='gray')
    plt.title('imfilter')

    # 进行空间滤波
    if use_scipy:
        # 2d convolution for f and h with scipy
        _g = scipy.signal.convolve2d(f, h, mode='same')
    else:
        _g = conv2(f, h)
    plt.subplot(2, 3, 5)
    plt.imshow(_g, cmap='gray')
    plt.title('spfilter')

    # 保存图像
    if is_save:
        plt.savefig(
            f'../asset/result/{img_name}_{operator_name}.jpg',
            dpi=300)

    if is_show:
        plt.show()


def main():
    # 控制各类参数
    use_numpy = True
    use_scipy = False
    is_save = True
    is_show = False
    # 所有图像名称
    images = ['3_3', 'blown_ic', 'blurry_moon']
    # 所有的算子
    operators = {
        'sobel': np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]),
        'laplacian': np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]),
        'gaussian': np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16,
        'unsharp': np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4],
                             [6, 24, -476, 24, 6], [4, 16, 24, 16, 4],
                             [1, 4, 6, 4, 1]]) / 256,
        'prewitt': np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]]),
        'roberts': np.array([[1, 0], [0, -1]]),
        'log': np.array([[0, 0, -1, 0, 0], [0, -1, -2, -1, 0],
                         [-1, -2, 16, -2, -1], [0, -1, -2, -1, 0],
                         [0, 0, -1, 0, 0]]) / 9,
        'median': np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9,
        'max': np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
        'min': np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
    }

    for img_name in images:
        # 加载图像
        f = mpimg.imread(f'../asset/image/{img_name}.jpg')
        # 归一化
        f = f / 256
        for operator_name, h in operators.items():
            test_operator(img_name, operator_name, f, h,
                          use_numpy=use_numpy, use_scipy=use_scipy,
                          is_save=is_save, is_show=is_show)


if __name__ == '__main__':
    test_fft()
    main()
