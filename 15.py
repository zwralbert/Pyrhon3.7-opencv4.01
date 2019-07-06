import cv2 as cv
import numpy as np


# 圖像處理梯度处理三种算子直接调用不同的API调用
# Sobel算子是一阶导数的边缘检测算子，在算法实现过程中，
# 通过3×3模板作为核与图像中的每个像素点做卷积和运算，然后选取合适的阈值以提取边缘。
def sobel_image(image):
    grad_x = cv.Sobel( image, cv.CV_32F, 1, 0 )
    grad_y = cv.Sobel( image, cv.CV_32F, 0, 1 )
    gradx = cv.convertScaleAbs( grad_x )
    grady = cv.convertScaleAbs( grad_y )
    cv.imshow( "x direction", gradx )
    cv.imshow( "y direction", grady )
    gradxy = cv.addWeighted( gradx, 0.5, grady, 0.5, 0 )
    cv.imshow( "合成", gradxy )


def scharr_image(image):
    grad_x = cv.Scharr( image, cv.CV_32F, 1, 0 )
    grad_y = cv.Scharr( image, cv.CV_32F, 0, 1 )
    gradx = cv.convertScaleAbs( grad_x )
    grady = cv.convertScaleAbs( grad_y )
    cv.imshow( "x direction", gradx )
    cv.imshow( "y direction", grady )
    gradxy = cv.addWeighted( gradx, 0.5, grady, 0.5, 0 )
    cv.imshow( "合成", gradxy )


def laplian_image(image):
    dst = cv.Laplacian( image, cv.CV_32F )
    lpls = cv.convertScaleAbs( dst )
    cv.imshow( "lpls", lpls )


# 改变图片大小和计算输出时间
src = cv.imread( "D:/Users/zwr/PycharmProjects/python-opencv/picture and video/m1.jpg" )
res = cv.resize( src, (340, 440), cv.INTER_CUBIC )
cv.imshow( "original", res )
# sobel_image(res)
# laplian_image(res)
scharr_image( res )
cv.waitKey( 0 )
cv.destroyAllWindows()
