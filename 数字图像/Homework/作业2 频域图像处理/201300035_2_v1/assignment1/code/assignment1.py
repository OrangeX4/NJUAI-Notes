from __future__ import annotations
# import iterable
from typing import Iterable
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

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


def show_fourier_spectrum(F):
    '''
    显示傅里叶谱
    '''
    # 取傅里叶谱
    F = np.abs(F)
    # 取对数
    F = np.log(1 + F)
    # 归一化
    F = F / F.max()
    # 显示图像
    plt.imshow(F, cmap='gray')


def main():
    # 1. 加载 ../asset/image/432.tif
    #    并得到输入图像的大小
    f = mpimg.imread('../asset/image/432.tif')
    # 归一化
    f = f / 256
    # 显示三张图像
    plt.subplot(1, 3, 1)
    plt.imshow(f, cmap='gray')
    M, N = f.shape

    # 不进行零填充
    P, Q = M, N
    H = fspecial_gaussian((P, Q), 10)
    g_no_zero_filled = my_imfilter(f, P, Q, H)
    plt.subplot(1, 3, 2)
    plt.imshow(g_no_zero_filled, cmap='gray')

    # 进行零填充
    P, Q = 2 * M, 2 * N
    H = fspecial_gaussian((P, Q), 10)
    g_zero_filled = my_imfilter(f, P, Q, H)
    plt.subplot(1, 3, 3)
    plt.imshow(g_zero_filled, cmap='gray')

    plt.show()
    


def my_imfilter(f: np.ndarray, P: int, Q: int, H: np.ndarray) -> np.ndarray:
    # 2. 为 f(x,y) 添加必要数量的 0, 此处省略
    M, N = f.shape
    # 3. 用 (-1)^(x+y) 乘以 f(x,y) 移到变换中心
    x = np.arange(M)[:, None]
    y = np.arange(N)[None, :]
    f = f * (-1) ** (x + y)
    # 4. 计算 f(x,y) 的傅里叶变换得到 F(u,v)
    F = np.fft.fft2(f, (P, Q))
    # show_fourier_spectrum(F)
    # 5. 生成一个频域滤波器 H(u,v),
    #    并用阵列相乘形成 G(u,v) = H(u,v) * F(u,v)
    G = H * F
    # 6. 得到 g_p(x,y), 即 G(u,v) 的傅里叶逆变换,
    #    转换为实部, 并乘上 (-1)^(x+y)
    x = np.arange(P)[:, None]
    y = np.arange(Q)[None, :]
    g_p = np.fft.ifft2(G).real * (-1) ** (x + y)
    # 7. 截取 g_p(x,y) 的左上部分 (M x N), 得到 g(x,y)
    return g_p[:M, :N]

    

if __name__ == '__main__':
    main()