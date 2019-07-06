import cv2 as cv
import numpy as np


# canny边缘检测 先高斯模糊，然后Sobel变幻，最后Canny边缘检测
def edge_image(image):
    blur = cv.GaussianBlur( image, (3, 3), 0 )
    gray = cv.cvtColor( blur, cv.COLOR_RGB2GRAY )
    xgrad = cv.Sobel( gray, cv.CV_16SC1, 1, 0 )
    ygrad = cv.Sobel( gray, cv.CV_16SC1, 0, 1 )
    edge_output = cv.Canny( xgrad, ygrad, 50, 100 )
    cv.imshow( "canny", edge_output )
    dst = cv.bitwise_and( image, image, mask=edge_output )
    cv.imshow( "color", dst )


# 改变图片大小和计算输出时间
src = cv.imread( "D:/Users/zwr/PycharmProjects/python-opencv/picture and video/m1.jpg" )
res = cv.resize( src, (340, 400), cv.INTER_CUBIC )
cv.imshow( "original", res )
edge_image( res )
cv.waitKey( 0 )
cv.destroyAllWindows()
