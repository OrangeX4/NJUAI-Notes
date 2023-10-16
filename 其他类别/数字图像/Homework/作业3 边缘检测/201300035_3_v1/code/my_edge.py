import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from typing import Callable


# 梯度阈值化边缘检测
def my_gradient_thresholding(img: np.ndarray, threshold=200):
    '''
    梯度阈值化边缘检测    
    :param img: 灰度图像
    :param threshold: 阈值, 范围为 [0, 255]
    '''
    img = img.astype(np.float32)
    # 通过 Sobel 算子计算水平和垂直方向的梯度
    img_gx = cv.Sobel(img, cv.CV_32F, 1, 0, ksize=3)
    img_gy = cv.Sobel(img, cv.CV_32F, 0, 1, ksize=3)
    img_g = np.sqrt(img_gx ** 2 + img_gy ** 2)
    img_g[img_g < threshold] = 0
    img_g[img_g >= threshold] = 255
    return img_g.astype(np.uint8)


# 均值滤波器平滑处理后阈值化边缘检测
def my_filtering_gradient_thresholding(img: np.ndarray, kernel_size=5, threshold=100):
    '''
    均值滤波器平滑处理边缘检测
    :param img: 灰度图像
    :param kernel_size: 卷积核大小, 范围为 [3, 7]
    :param threshold: 阈值, 范围为 [0, 255]
    '''
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)
    img = cv.filter2D(img, -1, kernel)
    img_gx = cv.Sobel(img, cv.CV_32F, 1, 0, ksize=3)
    img_gy = cv.Sobel(img, cv.CV_32F, 0, 1, ksize=3)
    img_g = np.sqrt(img_gx ** 2 + img_gy ** 2)
    img_g[img_g < threshold] = 0
    img_g[img_g >= threshold] = 255
    return img_g.astype(np.uint8)


# marr-hildreth 算法边缘检测
def my_marr_hildreth(img: np.ndarray, sigma=4.0, threshold=0.04):
    '''
    marr-hildreth 算法边缘检测
    :param img: 灰度图像
    :param sigma: 高斯滤波器的标准差
    :param threshold: 阈值, 范围为 [0.01, 0.1], 默认值为 0.04
    '''
    # 转换到 [0, 1] 范围
    img = img.astype(np.float32) / 255
    # 通过 sigma 获取高斯滤波器的大小
    n = int(6 * sigma)
    n = n if n % 2 == 1 else n + 1
    # 使用 n * n 的高斯滤波器对图像进行滤波
    kernel = cv.getGaussianKernel(n, sigma)
    kernel = kernel * kernel.T
    img = cv.filter2D(img, -1, kernel)
    # 使用拉普拉斯算子计算图像的二阶导数
    img_lap = cv.Laplacian(img, -1)
    # 找到图像的零交叉, 以每个像素为中心的 3 * 3 邻域内的像素值
    # 有 4 种要测试的情况: 左右, 上下, 左上右下, 左下右上
    # 如果至少有两种情况满足, 则认为该像素是边缘像素
    img_g = np.zeros(img.shape, np.uint8)
    # 阈值为最大值的相应倍数
    threshold = threshold * np.abs(img_lap).max()
    # 四个方向
    direction = [(0, 1), (1, 0), (1, 1), (1, -1)]
    # # 循环形式
    # for i in range(1, img.shape[0] - 1):
    #     for j in range(1, img.shape[1] - 1):
    #         count = 0
    #         # 四个方向
    #         for dx, dy in direction:
    #             if img_lap[i - dy, j - dx] * img_lap[i + dy, j + dx] < 0:
    #                 if abs(img_lap[i, j - 1] - img_lap[i, j + 1]) > threshold:
    #                     count += 1
    #             if count >= 2:
    #                 img_g[i, j] = 255
    #                 break
    # 非循环形式改写
    counts = np.zeros(img.shape, np.uint8)
    for dx, dy in direction:
        imgA = img_lap[1 - dy: None if -1 - dy == 0 else -1 - dy, 1 - dx: None if -1 - dx == 0 else -1 - dx]
        imgB = img_lap[1 + dy: None if -1 + dy == 0 else -1 + dy, 1 + dx: None if -1 + dx == 0 else -1 + dx]
        counts[1:-1, 1:-1] += (imgA * imgB < 0).astype(np.uint8) * (np.abs(imgA - imgB) > threshold).astype(np.uint8)
    img_g[counts >= 2] = 255
    return img_g


# canny 算法边缘检测
def my_canny(img: np.ndarray, sigma=4.0, threshold1=0.05, threshold2=0.15):
    '''
    canny 算法边缘检测
    :param img: 灰度图像
    :param sigma: 高斯滤波器的标准差
    :param threshold1: 阈值 1, 默认值为 0.05
    :param threshold2: 阈值 2, 默认值为 0.15
    '''
    # 转换到 [0, 1] 范围
    img = img.astype(np.float32) / 255
    # 通过 sigma 获取高斯滤波器的大小
    n = int(6 * sigma)
    n = n if n % 2 == 1 else n + 1
    # 使用 n * n 的高斯滤波器对图像进行滤波
    kernel = cv.getGaussianKernel(n, sigma)
    kernel = kernel * kernel.T
    img = cv.filter2D(img, -1, kernel)
    # 计算梯度幅度和方向
    img_gx = cv.Sobel(img, -1, 1, 0)
    img_gy = cv.Sobel(img, -1, 0, 1)
    img_g = np.sqrt(img_gx ** 2 + img_gy ** 2)
    img_theta = np.arctan2(img_gy, img_gx)
    # 将角度转换到 [-180, 180) 范围
    img_theta = np.rad2deg(img_theta)
    # 转换到四个方向
    img_theta[(img_theta >= -22.5) & (img_theta < 22.5)] = 0
    img_theta[(img_theta >= 157.5) | (img_theta < -157.5)] = 0
    img_theta[(img_theta >= 22.5) & (img_theta < 67.5)] = 45
    img_theta[(img_theta >= -157.5) & (img_theta < -112.5)] = 45
    img_theta[(img_theta >= 67.5) & (img_theta < 112.5)] = 90
    img_theta[(img_theta >= -112.5) & (img_theta < -67.5)] = 90
    img_theta[(img_theta >= 112.5) & (img_theta < 157.5)] = 135
    img_theta[(img_theta >= -67.5) & (img_theta < -22.5)] = 135
    # 方向映射到 dx, dy
    directions = {
        0: (1, 0),
        45: (1, 1),
        90: (0, 1),
        135: (1, -1)
    }
    # 非极大值抑制
    img_gn = np.zeros(img_g.shape, np.float32)
    # # 循环形式
    # for i in range(1, img_gn.shape[0] - 1):
    #     for j in range(1, img_gn.shape[1] - 1):
    #         # 如果小于其中一个邻居, 则抑制 gn(x, y) = 0
    #         # 否则 gn(x, y) = g(x, y)
    #         dx, dy = directions[img_theta[i, j]]
    #         value1 = img_g[i - dy, j - dx]
    #         value2 = img_g[i + dy, j + dx]
    #         if img_g[i, j] < value1 or img_g[i, j] < value2:
    #             img_gn[i, j] = 0
    #         else:
    #             img_gn[i, j] = img_g[i, j]
    # 非循环形式
    for theta, (dx, dy) in directions.items():
        imgA = img_g[1 - dy: None if -1 - dy == 0 else -1 - dy, 1 - dx: None if -1 - dx == 0 else -1 - dx]
        imgB = img_g[1 + dy: None if -1 + dy == 0 else -1 + dy, 1 + dx: None if -1 + dx == 0 else -1 + dx]
        img_gn[1: -1, 1: -1] = img_gn[1: -1, 1: -1] + \
            ((img_g[1: -1, 1: -1] >= imgA) & (img_g[1: -1, 1: -1] >= imgB) & \
                (img_theta[1: -1, 1: -1] == theta)) * img_g[1: -1, 1: -1]
    # 对阈值进行处理
    threshold1 = threshold1 * np.max(img_gn)
    threshold2 = threshold2 * np.max(img_gn)
    # 进行双阈值处理, 减少伪边缘点
    img_gnh = np.zeros(img_g.shape, np.uint8)
    img_gnh[img_gn >= threshold2] = 1
    img_gnl = np.zeros(img_g.shape, np.uint8)
    img_gnl[img_gn >= threshold1] = 1
    # 相减得到弱边缘点
    img_gnl = img_gnl - img_gnh
    # 遍历 gnh 中的每一个点 p, 保留与 gnh 8 连通的 gnl 点
    img_merged = img_gnh.copy()
    # 8 连通方向
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    # # 循环形式
    # for i in range(1, img_merged.shape[0] - 1):
    #     for j in range(1, img_merged.shape[1] - 1):
    #         if img_merged[i, j] == 1:
    #             for dx, dy in directions:
    #                 if img_gnl[i + dy, j + dx] == 1:
    #                     img_merged[i + dy, j + dx] = 1
    # 非循环形式
    for dx, dy in directions:
        img_merged[1 + dy: None if -1 + dy == 0 else -1 + dy, 1 + dx: None if -1 + dx == 0 else -1 + dx] = \
            img_merged[1 + dy: None if -1 + dy == 0 else -1 + dy, 1 + dx: None if -1 + dx == 0 else -1 + dx] | \
            img_gnl[1 + dy: None if -1 + dy == 0 else -1 + dy, 1 + dx: None if -1 + dx == 0 else -1 + dx] * \
            img_gnh[1: -1, 1: -1]
    return img_merged * 255


# 边缘检测测试
def test_edge(filename: str, edge_func: Callable, *, args={}, title='Edge Image') -> None:
    '''
    边缘检测测试
    :param filename: 图像文件名
    :param edge_func: 边缘检测函数
    :param args: 边缘检测函数的参数
    :param title: 边缘检测图像的标题
    '''
    img = cv.imread(filename)
    img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_edge = edge_func(img_grey, **args)

    plt.subplot(121)
    plt.imshow(img_grey, cmap = 'gray')
    plt.title('Original Image')

    plt.subplot(122)
    plt.imshow(img_edge, cmap = 'gray')
    plt.title(title)

    plt.show()


if __name__ == '__main__':

    filename = '../asset/image/rubberband_cap.png'
    # filename = '../asset/image/building_original.jpg'
    # filename = '../asset/image/ayu.jpg'
    # filename = '../asset/image/giraffe.jpg'
    # filename = '../asset/image/leaf.jpg'
    # filename = '../asset/image/noise.jpg'

    test_edge(filename, my_gradient_thresholding,
        args={'threshold': 200}, title='Gradient Thresholding Edge Image')

    test_edge(filename, my_filtering_gradient_thresholding,
        args={'kernel_size': 5, 'threshold': 100}, title='Mean Filtering Edge Image')

    test_edge(filename, my_marr_hildreth,
        args={'sigma': 4.0, 'threshold': 0.08}, title='Marr-Hildreth Edge Image')

    test_edge(filename, my_canny,
        args={'sigma': 4.0, 'threshold1': 0.04, 'threshold2': 0.10}, title='Canny Edge Image')

