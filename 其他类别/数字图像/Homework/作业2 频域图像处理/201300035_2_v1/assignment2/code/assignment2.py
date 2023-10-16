from __future__ import annotations
from typing import Iterable
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


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


def show_one_padded(f: np.ndarray, M: int, N: int, left=True):
    '''
    显示 1 填充图像
    '''
    if left:
        _f = np.pad(f, ((0, M), (0, N)), 'constant', constant_values=f.max())
    else:
        _f = np.pad(f, ((0, M), (N, 0)), 'constant', constant_values=1.)
    plt.imshow(_f, cmap='gray')
    plt.axis('off')


def show_zero_padded(f: np.ndarray, M: int, N: int):
    '''
    显示 0 填充图像
    '''
    # 将矩阵中小于零的数变为零
    _f = np.where(f < 0, 0, f)
    _f = np.pad(_f, ((0, M), (0, N)), 'constant')
    plt.imshow(_f, cmap='gray')
    plt.axis('off')


def show_fourier_spectrum(F: np.ndarray):
    '''
    显示傅里叶谱
    '''
    # 取傅里叶谱
    F = np.abs(F)
    # 取对数
    F = np.log(1 + F)
    # 显示图像
    plt.imshow(F, cmap='gray')
    plt.axis('off')


def main():
    use_numpy = True
    # 1. 加载 ../asset/image/436.tif
    #    并得到输入图像的大小
    f = mpimg.imread('../asset/image/436.tif')
    # 归一化
    f = f / 256
    M, N = f.shape
    # 显示九张图像
    plt.subplots_adjust(wspace=0, hspace=0.1, left=0.1,
                        right=0.9, bottom=0.1, top=0.9)
    # 在第一张图像中显示原图像于右上角, 因此 1 填充
    plt.subplot(3, 3, 1)
    show_one_padded(f, M, N, left=False)

    # 0 填充
    plt.subplot(3, 3, 2)
    show_zero_padded(f, M, N)

    # 进行零填充
    P, Q = 2 * M, 2 * N
    H = fspecial_gaussian((P, Q), 20)
    g_zero_padded = my_imfilter(f, P, Q, H, use_numpy=use_numpy)
    plt.subplot(3, 3, 8)
    # 显示最后结果图像
    show_one_padded(g_zero_padded, M, N)

    # 获取最后组合图像并保存
    plt.savefig('../asset/result/436_processed.jpg', dpi=300)

    plt.show()


def my_imfilter(f: np.ndarray, P: int, Q: int, H: np.ndarray, use_numpy=False) -> np.ndarray:
    # 2. 为 f(x,y) 添加必要数量的 0, 此处省略
    M, N = f.shape
    # 3. 用 (-1)^(x+y) 乘以 f(x,y) 移到变换中心
    x = np.arange(M)[:, None]
    y = np.arange(N)[None, :]
    f = f * (-1) ** (x + y)
    # 显示乘以 (-1)^(x+y) 后的图像
    plt.subplot(3, 3, 3)
    show_zero_padded(f, M, N)
    # 4. 计算 f(x,y) 的傅里叶变换得到 F(u,v)
    if use_numpy:
        F = np.fft.fft2(f, (P, Q))
    else:
        F = fft2(f, (P, Q))
    # 显示傅里叶谱
    plt.subplot(3, 3, 4)
    show_fourier_spectrum(F)
    # 显示高斯滤波器傅里叶谱
    plt.subplot(3, 3, 5)
    show_fourier_spectrum(H)
    # 5. 生成一个频域滤波器 H(u,v),
    #    并用阵列相乘形成 G(u,v) = H(u,v) * F(u,v)
    G = H * F
    # 显示滤波后结果
    plt.subplot(3, 3, 6)
    show_fourier_spectrum(G)
    # 6. 得到 g_p(x,y), 即 G(u,v) 的傅里叶逆变换,
    #    转换为实部, 并乘上 (-1)^(x+y)
    x = np.arange(P)[:, None]
    y = np.arange(Q)[None, :]
    if use_numpy:
        g_p = np.fft.ifft2(G).real * (-1) ** (x + y)
    else:
        g_p = ifft2(G).real * (-1) ** (x + y)
    # 显示 g_p(x,y)
    plt.subplot(3, 3, 7)
    plt.imshow(g_p, cmap='gray')
    plt.axis('off')
    # 7. 截取 g_p(x,y) 的左上部分 (M x N), 得到 g(x,y)
    return g_p[:M, :N]


if __name__ == '__main__':
    test_fft()
    main()
