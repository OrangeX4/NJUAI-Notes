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
        plt.subplots_adjust(wspace=0.2, hspace=1.0)
        # 显示两张图像
        plt.subplot(1, 2, 1)
        plt.title('Before')
        plt.imshow(before.get_image(),
                   cmap='gray' if before._is_gray_image else None)
        plt.subplot(1, 2, 2)
        plt.title('After')
        plt.imshow(self.get_image(),
                   cmap='gray' if self._is_gray_image else None)
        plt.show()

    @staticmethod
    def get_hist_from_gray_image(gray_image: np.ndarray, *, gray_level=256) -> np.ndarray:
        '''
        获取灰度图像的直方图, 返回一个一维数组, 灰阶默认为 256, 数组的每个元素对应图像的每个灰度级的像素个数
        '''
        # 循环版本 (速度慢)
        # hist = np.zeros(gray_level)
        # for i in range(gray_image.shape[0]):
        #     for j in range(gray_image.shape[1]):
        #         hist[gray_image[i][j]] += 1

        # 矩阵版本 (速度快)
        hist = np.bincount(gray_image.flatten(), minlength=gray_level)
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
            self._hist = self.get_hist_from_gray_image(
                self._image, gray_level=self._gray_level)
        else:
            # RGB 分别处理
            self._hist = []
            for i in range(3):
                self._hist.append(self.get_hist_from_gray_image(
                    self._image[:, :, i], gray_level=self._gray_level))
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
        s = (((gray_level - 1) /
             (image.shape[0] * image.shape[1])) * cum_hist).astype(np.uint8)
        # 映射
        new_image = np.zeros(
            image.shape, dtype=np.uint8 if gray_level <= 256 else np.uint16)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                new_image[i][j] = s[image[i][j]]
        return new_image

    @staticmethod
    def RGB2HSI(image: np.ndarray, *, gray_level=256) -> np.ndarray:
        '''
        将 RGB 图像矩阵转换为 HSI 图像矩阵 (强度和饱和度会被转化为 0 到 1 之间的浮点数)
        1. H = theta if B <= G else 360 - theta
           theta = arccos(0.5 * (R - G + R - B) / sqrt((R - G)^2 + (R - B) * (G - B)))
        2. S = 1 - 3 / (R + G + B) * min(R, G, B)
        3. I = (R + G + B) / 3
        '''
        # RGB 矩阵
        R, G, B = image[:, :, 0] / (gray_level - 1), image[:, :, 1] / \
            (gray_level - 1), image[:, :, 2] / (gray_level - 1)
        # 1. 计算 Hue 色调分量, 分母加上一个小分量避免除 0
        theta = np.arccos(0.5 * (R - G + R - B) /
                          (np.sqrt((R - G) ** 2 + (R - B) * (G - B)) + 1e-10))
        H = np.where(B <= G, theta, 2 * np.pi - theta)
        # 2. 计算 Saturation 饱和度分量
        S = 1 - 3 / (R + G + B + 1e-10) * np.min([R, G, B], axis=0)
        # 3. 计算 Intensity 强度分量
        I = (R + G + B) / 3
        # 综合
        HSI = np.dstack([H, S, I])
        return HSI

    @staticmethod
    def HSI2RGB(image: np.ndarray, *, gray_level=256) -> np.ndarray:
        '''
        将 HSI 图像矩阵转换为 RGB 图像矩阵
        1. 位于 RG 扇区 (0 <= H < 120) 时:
           B = I * (1 - S)
           R = I * (1 + S * cos(H) / cos(60 - H))
           G = 3 * I - (R + B)
        2. 位于 GB 扇区 (120 <= H < 240) 时:
           R = I * (1 - S)
           G = I * (1 + S * cos(H - 120) / cos(180 - H))
           B = 3 * I - (R + G)
        3. 位于 BR 扇区 (240 <= H < 360) 时:
           G = I * (1 - S)
           B = I * (1 + S * cos(H - 240) / cos(300 - H))
           R = 3 * I - (G + B)
        '''
        # 矩阵版本 (速度快)
        # HSI 矩阵
        H, S, I = image[:, :, 0], image[:, :, 1], image[:, :, 2]
        # 计算 RGB 分量
        R = np.where(H < 2 / 3 * np.pi, I * (1 + S * np.cos(H) / (np.cos(np.pi / 3 - H) + 1e-10)),
                     np.where(H < 4 / 3 * np.pi, I * (1 - S),
                              3 * I - (I * (1 - S) + I * (1 + S * np.cos(H - 4 / 3 * np.pi) / (np.cos(5 * np.pi / 3 - H) + 1e-10)))))
        G = np.where(H < 2 / 3 * np.pi, 3 * I - (I * (1 - S) + I * (1 + S * np.cos(H) / (np.cos(np.pi / 3 - H) + 1e-10))),
                     np.where(H < 4 / 3 * np.pi, I * (1 + S * np.cos(H - 2 / 3 * np.pi) / (np.cos(np.pi - H) + 1e-10)),
                              I * (1 - S)))
        B = np.where(H < 2 / 3 * np.pi, I * (1 - S),
                     np.where(H < 4 / 3 * np.pi, 3 * I - (I * (1 - S) + I * (1 + S * np.cos(H - 2 / 3 * np.pi) / (np.cos(np.pi - H) + 1e-10))),
                              I * (1 + S * np.cos(H - 4 / 3 * np.pi) / (np.cos(5 * np.pi / 3 - H) + 1e-10))))
        # 截断到 0 和 1 之间
        RGB = np.dstack([R, G, B])
        RGB = np.where(RGB < 0, 0, RGB)
        RGB = np.where(RGB > 1, 1, RGB)
        RGB = (RGB * (gray_level - 1)
               ).astype(np.uint8 if gray_level <= 256 else np.uint16)

        # # 循环版本 (速度慢)
        # # HSI 矩阵
        # H, S, I = image[:, :, 0], image[:, :, 1], image[:, :, 2]
        # RGB = np.zeros(
        #     image.shape, dtype=np.uint8 if gray_level <= 256 else np.uint16)
        # for i in range(image.shape[0]):
        #     for j in range(image.shape[1]):
        #         if H[i][j] < 2 / 3 * np.pi:
        #             _H = H[i][j]
        #             B = I[i][j] * (1 - S[i][j])
        #             R = I[i][j] * (1 + S[i][j] * np.cos(_H) /
        #                            (np.cos(np.pi / 3 - _H) + 1e-10))
        #             G = 3 * I[i][j] - (R + B)
        #         elif H[i][j] < 4 / 3 * np.pi:
        #             _H = H[i][j] - 2 / 3 * np.pi
        #             R = I[i][j] * (1 - S[i][j])
        #             G = I[i][j] * (1 + S[i][j] * np.cos(_H) /
        #                            (np.cos(np.pi / 3 - _H) + 1e-10))
        #             B = 3 * I[i][j] - (R + G)
        #         else:
        #             _H = H[i][j] - 4 / 3 * np.pi
        #             G = I[i][j] * (1 - S[i][j])
        #             B = I[i][j] * (1 + S[i][j] * np.cos(_H) /
        #                            (np.cos(np.pi / 3 - _H) + 1e-10))
        #             R = 3 * I[i][j] - (G + B)
        #         # 预防溢出
        #         R = max(0, min(R, 1))
        #         G = max(0, min(G, 1))
        #         B = max(0, min(B, 1))
        #         # 最后统合
        #         RGB[i][j][:] = np.array([R, G, B]) * (gray_level - 1)
        return RGB

    def histeq(self, *, method='gray') -> Image:
        '''
        进行图像直方图均衡化, 计算公式为 s = T(r) = round((L-1) * sum(p[0:r]) / N * M)
        对彩色图像进行直方图均衡化的方法有两种:
            1. 分通道灰度图像直方图均衡化
            2. HSI 空间直方图均衡化
        '''
        if self._is_gray_image:
            new_image = self.histeq_for_gray_image(
                self._image, gray_level=self._gray_level)
        else:
            if method == 'gray':
                # 1. 分通道灰度图像直方图均衡化
                new_image = np.zeros(
                    self._image.shape, dtype=np.uint8 if self._gray_level <= 256 else np.uint16)
                for i in range(3):
                    new_image[:, :, i] = self.histeq_for_gray_image(
                        self._image[:, :, i], gray_level=self._gray_level)
            elif method == 'hsi':
                # 2. HSI 空间直方图均衡化
                HSI = self.RGB2HSI(self._image)
                H, S, I = HSI[:, :, 0], HSI[:, :, 1], HSI[:, :, 2]
                # 单独对 Intensity 强度分量进行直方图均衡化
                # 转换为整数灰阶图像矩阵
                I = (I * (self._gray_level - 1)
                     ).astype(np.uint8 if self._gray_level <= 256 else np.uint16)
                I = self.histeq_for_gray_image(I, gray_level=self._gray_level)
                # 转换为浮点数强度图像矩阵
                I = I / (self._gray_level - 1)
                # 恢复 HSI 矩阵
                HSI = np.dstack([H, S, I])
                new_image = self.HSI2RGB(HSI)
            else:
                raise ValueError('method must be "gray" or "hsi"')
        return Image(new_image, gray_level=self._gray_level)


if __name__ == '__main__':

    # 灰色图像直方图均衡化
    # 图像加载
    img = Image(mpimg.imread('../asset/image/gray.jpg'))
    # 显示直方图
    img.show_hist()
    # 比较图像
    img.histeq().compare_with(img)
    # 比较直方图
    img.histeq().compare_hist_with(img)

    # 彩色图像直方图均衡化
    img = Image(mpimg.imread('../asset/image/color.jpg'))
    img.histeq().compare_with(img)
    img.histeq().compare_hist_with(img)
    # 基于 HSI 色彩空间的直方图均衡化
    img.histeq(method='hsi').compare_with(img)
    img.histeq(method='hsi').compare_hist_with(img)

    # 实验介绍文档中使用的图片
    img = Image(mpimg.imread('../asset/image/boat.jpg'))
    img.histeq().compare_with(img)
    img.histeq().compare_hist_with(img)
    img.histeq(method='hsi').compare_with(img)
    img.histeq(method='hsi').compare_hist_with(img)

    ############################################################

    # 其他图片
    img = Image(mpimg.imread('../asset/image/genshin.jpg'))
    img.histeq().compare_with(img)
    img.histeq().compare_hist_with(img)
    img.histeq(method='hsi').compare_with(img)
    img.histeq(method='hsi').compare_hist_with(img)

    img = Image(mpimg.imread('../asset/image/night.jpg'))
    img.histeq().compare_with(img)
    img.histeq().compare_hist_with(img)
    img.histeq(method='hsi').compare_with(img)
    img.histeq(method='hsi').compare_hist_with(img)

    # Debug 时使用的单像素图片
    # img = np.array([[[3.91174, 0.08026, 0.94510]]])
    # Image(img).HSI2RGB(img)
