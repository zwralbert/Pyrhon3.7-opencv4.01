import cv2 as cv
import numpy as np
#改变图片大小和计算输出时间
src=cv.imread("D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m1.jpg")
cv.namedWindow("first",cv.WINDOW_NORMAL)
cv.imshow("first",src)
res=cv.resize(src,(1340,1104),cv.INTER_CUBIC)
cv.imshow("change",res)
t1=cv.getTickCount()
t2=cv.getTickCount()
time=(t2-t1)/cv.getTickFrequency()
print("time:%s" %time)

cv.waitKey(0)
cv.destroyAllWindows()