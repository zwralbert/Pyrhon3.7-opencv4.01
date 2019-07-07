import cv2 as cv
import numpy as np
#腐蝕和膨脹操作 灰度和二值化之后
def erode_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel=cv.getStructuringElement(cv.MORPH_ERODE,(5,5))
    dst=cv.erode(binary,kernel)
    cv.imshow("erode",dst)

def dilate_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst=cv.dilate(binary,kernel)
    cv.imshow("erode",dst)
"""
开运算:先进性腐蚀再进行膨胀就叫做开运算,它被用来去除噪声。
闭运算:先膨胀再腐蚀。它经常被用来填充前景物体中的小洞，或者前景物体上的小黑点。
这里我们用到的函数是 cv2.morphologyEx()。
开闭操作作用：
1. 去除小的干扰块-开操作
2. 填充闭合区间-闭操作
3. 水平或垂直线提取,调整kernel的row，col值差异。
比如：采用开操作，kernel为(1, 15),提取垂直线，kernel为(15, 1),提取水平线，
"""
#开闭操作
def open_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    dst=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel=kernel)
    cv.imshow("open_demo",dst)


def close_demo(image):
    gray = cv.cvtColor( image, cv.COLOR_RGB2GRAY )
    ret, binary = cv.threshold( gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU )
    cv.imshow( "binary", binary )
    kernel = cv.getStructuringElement( cv.MORPH_RECT, (5, 5) )
    dst = cv.morphologyEx( binary, cv.MORPH_CLOSE, kernel=kernel )
    cv.imshow( "close_demo", dst )


# 改变图片大小和计算输出时间
src = cv.imread( "D:/Users/zwr/PycharmProjects/python-opencv/picture and video/m8.jpg" )

res = cv.resize( src, (340, 400), cv.INTER_CUBIC )
# erode_demo(res)
# # dilate_demo(res)
open_demo(res)
# close_demo(res)
cv.waitKey( 0 )
cv.destroyAllWindows()
