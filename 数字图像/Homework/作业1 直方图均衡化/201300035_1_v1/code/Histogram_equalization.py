from __future__ import annotations
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


class Image:
    '''
    图像类, 里面包括了图像初始化, 显示, 获取直方图, 直方图均衡化等方法
    '''

    def __init__(self, image: np.ndarray, *, gray_level=256) -> None:
        '''
        初始化图像, 传入图像矩阵 image
        还可以输入灰阶 gray_level, 默认为 256
        '''
        # 保存输入参数
        self._image = image
        self._gray_level = gray_level
        # 是否是灰度图像
        self._is_gray_image = self._image.ndim == 2
        # 如果不是灰度图像, 则保证传入的是彩色图像
        if not self._is_gray_image:
            assert self._image.ndim == 3
        # 初始化其他成员变量
        self._hist = None

    
    def get_image(self) -> np.ndarray:
        '''
        获取图像矩阵
        '''
        return self._image

    
    def show(self) -> None:
        '''
        显示图像
        '''
        plt.figure(figsize=(20, 20))
        plt.imshow(self._image, cmap='gray' if self._is_gray_image else None)
        plt.show()

    
    def compare_with(self, before: Image) -> None:
        '''
        与前一张图像进行对比显示
        '''
        plt.figure(figsize=(20, 20))
        plt.subplots_adjust(wspace=0.5, hspace=1.0)
        # 显示两张图像
        plt.subplot(1, 2, 1)
        plt.title('Before')
        plt.imshow(before.get_image(), cmap='gray' if before._is_gray_image else None)
        plt.subplot(1, 2, 2)
        plt.title('After')
        plt.imshow(self.get_image(), cmap='gray' if self._is_gray_image else None)
        plt.show()


    @staticmethod
    def get_hist_from_gray_image(gray_image: np.ndarray, *, gray_level=256) -> np.ndarray:
        '''
        获取灰度图像的直方图, 返回一个一维数组, 灰阶默认为 256, 数组的每个元素对应图像的每个灰度级的像素个数
        '''
        hist = np.zeros(gray_level)
        for i in range(gray_image.shape[0]):
            for j in range(gray_image.shape[1]):
                hist[gray_image[i][j]] += 1
        return hist


    def hist(self) -> np.ndarray:
        '''
        获取图像的直方图. 如果是灰度图像, 返回一维数组, 如果是彩色图像, 返回二维数组
        '''
        # 返回保存的直方图
        if self._hist is not None:
            return self._hist
        # 如果未初始化, 则进行计算
        if self._is_gray_image:
            self._hist = self.get_hist_from_gray_image(self._image, gray_level=self._gray_level)
        else:
            # RGB 分别处理
            self._hist = []
            for i in range(3):
                self._hist.append(self.get_hist_from_gray_image(self._image[:, :, i], gray_level=self._gray_level))
            self._hist = np.array(self._hist)
        return self._hist


    def show_hist(self) -> None:
        '''
        显示图像的直方图
        '''
        plt.subplots_adjust(wspace=0.5, hspace=1.0)
        # 如果是灰度图像, 显示一维直方图
        if self._is_gray_image:
            plt.bar(range(self._gray_level), self.hist(), color='black')
        # 如果是彩色图像, 显示三个一维直方图
        else:
            # 红色
            plt.subplot(3, 1, 1)
            plt.title('Red')
            plt.bar(range(self._gray_level), self.hist()[0], color='red')
            # 绿色
            plt.subplot(3, 1, 2)
            plt.title('Green')
            plt.bar(range(self._gray_level), self.hist()[1], color='green')
            # 蓝色
            plt.subplot(3, 1, 3)
            plt.title('Blue')
            plt.bar(range(self._gray_level), self.hist()[2], color='blue')
        plt.show()


    def compare_hist_with(self, before: Image):
        '''
        与前一张图的直方图进行对比
        '''
        plt.subplots_adjust(wspace=0.5, hspace=1.0)
        # 如果是灰度图像, 显示一维直方图
        if self._is_gray_image:
            plt.subplot(1, 2, 1)
            plt.title('Before')
            plt.bar(range(self._gray_level), before.hist(), color='black')
            plt.subplot(1, 2, 2)
            plt.title('After')
            plt.bar(range(self._gray_level), self.hist(), color='black')
        # 如果是彩色图像, 显示三个一维直方图
        else:
            # 红色
            plt.subplot(3, 2, 1)
            plt.title('Before Red')
            plt.bar(range(self._gray_level), before.hist()[0], color='red')
            plt.subplot(3, 2, 2)
            plt.title('After Red')
            plt.bar(range(self._gray_level), self.hist()[0], color='red')
            # 绿色
            plt.subplot(3, 2, 3)
            plt.title('Before Green')
            plt.bar(range(self._gray_level), before.hist()[1], color='green')
            plt.subplot(3, 2, 4)
            plt.title('After Green')
            plt.bar(range(self._gray_level), self.hist()[1], color='green')
            # 蓝色
            plt.subplot(3, 2, 5)
            plt.title('Before Blue')
            plt.bar(range(self._gray_level), before.hist()[2], color='blue')
            plt.subplot(3, 2, 6)
            plt.title('After Blue')
            plt.bar(range(self._gray_level), self.hist()[2], color='blue')
        plt.show()

    
    @staticmethod
    def histeq_for_gray_image(image, *, gray_level=256) -> np.ndarray:
        '''
        进行灰度图像直方图均衡化, 计算公式为 s = T(r) = round((L-1) * sum(p[0:r]) / N * M)
        '''
        # 计算直方图
        hist = Image.get_hist_from_gray_image(image, gray_level=gray_level)
        # 计算累积直方图
        cum_hist = np.zeros(gray_level)
        cum_hist[0] = hist[0]
        for i in range(1, gray_level):
            cum_hist[i] = cum_hist[i - 1] + hist[i]
        # 计算映射函数
        s = np.zeros(gray_level)
        for i in range(gray_level):
            s[i] = round((gray_level - 1) * cum_hist[i] / (image.shape[0] * image.shape[1]))
        # 映射
        new_image = np.zeros(image.shape, dtype=np.uint8 if gray_level <= 256 else np.uint16)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                new_image[i][j] = s[image[i][j]]
        return new_image

    
    def histeq(self, *, method='gray') -> Image:
        '''
        进行图像直方图均衡化, 计算公式为 s = T(r) = round((L-1) * sum(p[0:r]) / N * M)
        对彩色图像进行直方图均衡化的方法有两种:
            1. 分通道灰度图像直方图均衡化
            2. HSI 空间直方图均衡化
        '''
        if self._is_gray_image:
            new_image = self.histeq_for_gray_image(self._image, gray_level=self._gray_level)
        else:
            if method == 'gray':
                # 1. 分通道灰度图像直方图均衡化
                new_image = np.zeros(self._image.shape, dtype=np.uint8 if self._gray_level <= 256 else np.uint16)
                for i in range(3):
                    new_image[:, :, i] = self.histeq_for_gray_image(self._image[:, :, i], gray_level=self._gray_level)
            elif method == 'hsi':
                # 2. HSI 空间直方图均衡化
                raise NotImplementedError
            else:
                raise ValueError('method must be "gray" or "hsi"')
        return Image(new_image, gray_level=self._gray_level)


if __name__ == '__main__':

    # 图像加载
    img = Image(mpimg.imread('../asset/image/color.jpg'))

    # 显示直方图
    # img.show_hist()
    # img.histeq().show_hist()

    # 比较直方图
    # img.histeq().compare_hist_with(img)

    # 直方图均衡化
    # img = Image(mpimg.imread('../asset/image/gray.jpg'))
    # img.histeq().compare_with(img)
    # img.histeq().compare_hist_with(img)

    # img = Image(mpimg.imread('../asset/image/color.jpg'))
    # img.histeq().compare_with(img)
    # img.histeq().compare_hist_with(img)

    img = Image(mpimg.imread('../asset/image/boat.jpg'))
    img.histeq().compare_with(img)
    img.histeq().compare_hist_with(img)

    # img = Image(mpimg.imread('../asset/image/genshin.jpg'))
    # img.histeq().compare_with(img)
    # img.histeq().compare_hist_with(img)