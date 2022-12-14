import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from typing import Callable
from my_edge import my_gradient_thresholding, my_filtering_gradient_thresholding, my_marr_hildreth, my_canny
from my_edgelinking import imtool, edge_link


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


def test_edge_link():
    filename = '../asset/image/rubberband_cap.png'
    # 边缘连接间断点的最大距离, 这里设为 3
    k = 3

    img = cv.imread(filename)
    img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_edge = my_canny(img_grey, sigma=4.0, threshold1=0.04, threshold2=0.10)

    plt.subplot(131)
    plt.imshow(img_grey, cmap = 'gray')
    plt.title('Original Image')

    plt.subplot(132)
    plt.imshow(img_edge, cmap = 'gray')
    plt.title('Canny Edge Image')

    # imtool(img_edge)
    # 以下是对 'rubberband_cap.png' 找到的边缘点
    # (157, 388): 255
    # (126, 217): 255
    # (282, 223): 255
    # (204, 63): 255
    # (55, 62): 255
    # (60, 71): 255
    # (30, 264): 255
    # (41, 326): 255

    plt.subplot(133)
    background = np.zeros(img_grey.shape)
    plt.imshow(background, cmap = 'gray')
    bxpc1 = edge_link(img_edge, (131, 377), k=k)
    plt.plot(bxpc1[:, 1], bxpc1[:, 0], 'r-')
    bxpc2 = edge_link(img_edge, (126, 217), k=k)
    plt.plot(bxpc2[:, 1], bxpc2[:, 0], 'g-')
    bxpc3 = edge_link(img_edge, (282, 223), k=k)
    plt.plot(bxpc3[:, 1], bxpc3[:, 0], 'b-')
    bxpc4 = edge_link(img_edge, (204, 63), k=k)
    plt.plot(bxpc4[:, 1], bxpc4[:, 0], 'y-')
    bxpc5 = edge_link(img_edge, (55, 62), k=k)
    plt.plot(bxpc5[:, 1], bxpc5[:, 0], 'c-')
    bxpc6 = edge_link(img_edge, (60, 71), k=k)
    plt.plot(bxpc6[:, 1], bxpc6[:, 0], 'm-')
    bxpc7 = edge_link(img_edge, (30, 264), k=k)
    plt.plot(bxpc7[:, 1], bxpc7[:, 0], '-', color='orange')
    bxpc8 = edge_link(img_edge, (41, 326), k=k)
    plt.plot(bxpc8[:, 1], bxpc8[:, 0], '-', color='olive')
    plt.title('Edge Link Image')

    plt.show()


if __name__ == '__main__':
    # 边缘检测测试
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

    # 边缘连接测试
    test_edge_link()