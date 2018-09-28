import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt


temp_path = r'F:\python\StockAnalyzer\test\test.avi'
img_path = r'F:\python\StockAnalyzer\test'
img1_path = r'F:\python\StockAnalyzer\test\20180831 082450.png'
img2_path = r'F:\python\StockAnalyzer\test\20180903 065859.png'

img1 = cv.imread(img1_path)
img2 = cv.imread(img2_path, 0)

'''
四个参数：原图像，分类阈值，设置值，方法
cv.THRESH_BINARY：二值阈值话，高于阈值设为设置值，低于阈值设置为0
cv.THRESH_BINARY_INV：二值阈值化，取反
cv.THRESH_TRUNC：截断阈值
cv.THRESH_TOZERO_INV：超过阈值设置为0
cv.THRESH_TOZERO_INV：低于阈值被设置为0

'''
img2 = cv.medianBlur(img2, 5)
ret, th1 = cv.threshold(img2, 127, 255, cv.THRESH_BINARY)
ret, th2 = cv.adaptiveThreshold(img2, 120, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
ret, th3 = cv.adaptiveThreshold(img2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)


titles = ['original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOXERO_INV']
images = [img2, th1, th2, th3]


for i in range(4):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()



















