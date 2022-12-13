import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def main():
    img = cv.imread('rubberband_cap.png')
    img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_edge = cv.Canny(img_grey, 200, 500)

    plt.subplot(121)
    plt.imshow(img_grey, cmap = 'gray')
    plt.title('Original Image')

    plt.subplot(122)
    plt.imshow(img_edge, cmap = 'gray')
    plt.title('Edge Image')

    plt.show()


if __name__ == '__main__':
    main()