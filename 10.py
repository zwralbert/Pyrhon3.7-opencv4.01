import cv2 as cv
import numpy as np
#图像分通道分割和合并
 # src =cv.imread("D:/Users/zwr/PycharmProjects/scikit-learn/picture and vidio/m1.jpg")
# cv.namedWindow("原来",cv.WINDOW_NORMAL)
# cv.imshow("原来",src)
#
# b,g,r=cv.split(src)
# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow("red",r)
#
# src=cv.merge([b,g,r])
# cv.imshow("合并",src)
# src[:,:,2]=100
# cv.imshow("单通道",src)
##
#图像平均以及方差
def logic_demo(m1,m2):
    src1=cv.bitwise_not(m1)
    cv.imshow("非",src1)
    src2=cv.bitwise_or(m1,m2)
    cv.imshow("异或",src2)
def others(m1,m2):
    M1=cv.mean(m1)
    M2=cv.mean(m2)
    M1,St1=cv.meanStdDev(m1)
    M2,St2=cv.meanStdDev(m2)
    print(St1)
    print(St2)
    print(M1)
    print(M2)

#色彩空间转换RGB->HSV
# def nextrace_object_demo():
#     capture=cv.VideoCapture("D:/Users/zwr/PycharmProjects/scikit-learn/picture and vidio/123.mp4")
#     while True:
#         ret,frame=capture.read()
#         if ret==False:
#             break
#         hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
#         lower_hsv=np.array([0,0,122])
#         upper_hsv=np.array([180,255,0])
#         mask=cv.inRange(hsv,lower_hsv,upper_hsv)
#         cv.imshow("video",frame)
#         cv.imshow("mask",mask)
#         if cv.waitKey(50) &0xFF == ord("q"):
#           break



dst1=cv.imread("D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m1.jpg")
dst2=cv.imread("D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m2.jpg")
print(dst1.shape)
print(dst2.shape)
# nextrace_object_demo()
# others(dst1,dst2)
cv.namedWindow("1",cv.WINDOW_NORMAL)
cv.namedWindow("3",cv.WINDOW_NORMAL)
cv.imshow("1",dst1)
cv.imshow("3",dst2)
logic_demo(dst1,dst2)
cv.waitKey()
cv.destroyAllWindows()