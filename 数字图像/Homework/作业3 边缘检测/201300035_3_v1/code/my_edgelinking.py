import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from typing import Callable
from my_edge import my_gradient_thresholding, my_filtering_gradient_thresholding, my_marr_hildreth, my_canny


# 边缘连接函数
def edge_link(binary_img: np.ndarray, origin: tuple, k=5) -> np.ndarray:
    '''
    边缘连接函数
    :param binary_img: 二值图像, 0 和 1 或者 0 和 255 均可
    :param origin: 起始点坐标 (y, x), 可以通过 imtool 获取
    :param k: 间断点的最大距离, 默认为 3
    :return: 边缘连接后的二值图像, shape 为 (n, 2)
    '''
    origin = tuple(origin)
    if binary_img[origin] == 0:
        return np.array([])
    # 将二值图像中的 255 转换为 1
    if binary_img[origin] == 255:
        binary_img = binary_img // 255
    # 获取 n
    n = 2 * k + 1
    # 为原图像添加边界, 防止越界
    img = np.pad(binary_img, n, 'constant', constant_values=0)
    # 结果的点集
    result = [origin]
    # 选一个任意的 "上一点"
    last = (origin[0] - 1, origin[1] - 1)
    # 当前点为起始点
    current = origin
    # 构造一个 n * n 的矩阵, 例如为 [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
    mat_dy = np.arange(-k, k + 1).reshape(n, 1)
    mat_dy = np.repeat(mat_dy, n, axis=1)
    mat_dx = mat_dy.T
    # 若当前点与起始点不相等且临近于 k + 1, 则终止循环
    # 用一个循环计数, 终止循环
    loop_count = 0
    while loop_count < 200 and (last == origin or current == origin or (abs(current[0] - origin[0]) + abs(current[1] - origin[1])) > k + 1):
        loop_count += 1
        # 通过向量点乘找到当前点的下一个点, 并且使用原点对结果进行矫正
        dist = mat_dy * (current[0] - last[0]) + mat_dx * (current[1] - last[1])
        # 将 img 中为 0 的部分置为最小值
        dist[img[current[0] + k + 1:current[0] + k + 1 + n, current[1] + k + 1:current[1] + k + 1 + n] == 0] = -256
        # 将 dist 中间 k * k 的矩阵也设为最小值
        dist[k - 1: n - k + 1, k - 1: n - k + 1] = -256
        # 找到 dist 中最大的值的索引
        next = np.unravel_index(np.argmax(dist), dist.shape)
        # 如果最大值为 -256, 则说明没有下一个点, 终止循环
        if dist[next] == -256:
            break
        # 将当前点设为下一个点
        last = current
        current = (current[0] + next[0] - k, current[1] + next[1] - k)
        # 加入结果集
        result.append(current)
    result.append(origin)
    return np.array(result)


def imtool(img):
    '''
    imtool from cv2
    '''
    drawing = False
    ix,iy = -1,-1
    def mouse_event(event, x, y, flags, param):
        nonlocal ix, iy, drawing
        if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv.EVENT_LBUTTONUP:
            print(f'{(iy, ix)}: {img[iy, ix]}')
        # print ix,iy
            drawing = False
    cv.namedWindow('image')
    cv.setMouseCallback('image', mouse_event)
    while(1):
        cv.imshow('image', img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()



# 边缘连接测试
def test_edge_link(filename: str, edge_func: Callable, k=3, *, args={}, title='Edge Image') -> None:
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

    plt.subplot(131)
    plt.imshow(img_grey, cmap = 'gray')
    plt.title('Original Image')

    plt.subplot(132)
    plt.imshow(img_edge, cmap = 'gray')
    plt.title(title)

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

    filename = 'rubberband_cap.png'

    # test_edge_link(filename, my_gradient_thresholding,
    #     args={'threshold': 200}, title='Gradient Thresholding Edge Image')

    # test_edge_link(filename, my_filtering_gradient_thresholding,
    #     args={'kernel_size': 5, 'threshold': 100}, title='Mean Filtering Edge Image')

    # test_edge_link(filename, my_marr_hildreth,
    #     args={'sigma': 4.0, 'threshold': 0.08}, k=5, title='Marr-Hildreth Edge Image')

    test_edge_link(filename, my_canny,
        args={'sigma': 4.0, 'threshold1': 0.04, 'threshold2': 0.10}, title='Canny Edge Image')

