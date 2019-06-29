#图像的加减乘除以及逻辑运算

import numpy as np
import cv2 as cv
import numpy as np

#图像数学运算和逻辑运算
def create_image():
    img= np.ones([200,200,1], np.uint8)
    img=img*127
    cv.imshow("img1",img)
    dst=cv.imread( "D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m1.jpg")
    dst=np.ones([200,200,3])
    cv.imshow("img",dst)
def inverse(image):
    dst1=cv.bitwise_not(image)
    cv.imshow("back",dst1)

def add_demo(m1,m2):
    dst=cv.add(m1,m2)
    cv.imshow("add_demo",dst)
def subtract_demo(m1,m2):
    dst=cv.subtract(m1,m2)
    cv.imshow("subtract_demo",dst)
def logic_demo(m1,m2):
    dst=cv.bitwise_and(m1,m2)
    cv.imshow("logic_demo",dst)
src1=cv.imread("D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m2.jpg")
src2=cv.imread("D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m1.jpg")
print(src1.shape)
print(src2.shape)
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src1)
cv.imshow("input image1",src2)

src3=cv.imread("D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m1.jpg")
cv.namedWindow("first",cv.WINDOW_NORMAL)
cv.imshow("first",src3)
t1=cv.getTickCount() ##计算取反时间
inverse(src3)
t2=cv.getTickCount()
time=(t2-t1)*1000/cv.getTickFrequency()
print("time:%s" %time)
create_image()

subtract_demo(src1,src2)
logic_demo(src1,src2)
cv.waitKey(0)
cv.destroyAllWindows()