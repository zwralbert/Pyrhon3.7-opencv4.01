#直方图

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#画出图像的直方图
def hist_demo(image):
    color=("blue","green","red")
    for i,color in enumerate(color):
        hist=cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color=color)
    plt.show()
#灰度图
def equalHist_image(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("equalHist",gray)
    dst=cv.equalizeHist(gray)
    cv.imshow("默认处理",dst)
#自定义灰度对比度
def clahe_image(image):
    gray=cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    clahe=cv.createCLAHE(100,(1,1))#第一个参数对比度的大小，第二个是处理图像的大小
    dst=clahe.apply(gray)
    cv.imshow("clahe",dst)
#直方图的比较
def creat_demo(image):
    h,w,c=image.shape
    rgbhist=np.zeros([16*16*16,1],np.float32)
    bsize=256/16
    for row in range(h):
        for col in range(w):
            b=image[row,col,0]
            g = image[row, col, 1]
            r= image[row, col, 2]
        index=np.int(b/bsize)+np.int(g/bsize)+np.int(r/bsize)
        rgbhist[np.int(index),0]=rgbhist[np.int(index),0]+1
    return rgbhist
#直方图比较
def hist_compare(image1,image2):
    hist1=creat_demo(image1)
    hist2=creat_demo(image2)
    match1=cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA)#巴氏距离
    match2= cv.compareHist( hist1, hist2, cv.HISTCMP_CORREL )#相识度
    match3 = cv.compareHist( hist1, hist2, cv.HISTCMP_CHISQR )#卡方
    print("%s %s %s"%(match1,match2,match3))
src1=cv.imread("D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m1.jpg")
src2=cv.imread("D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m3.jpg")
# cv.imshow("first",src1)
res1=cv.resize(src1,(600,600),cv.INTER_CUBIC)
res2=cv.resize(src2,(600,600),cv.INTER_CUBIC)
hist_compare(res1,res2)
cv.imshow("2",res1)
cv.imshow("1",res2)
# hist_demo(res)
# equalHist_image(res)
# clahe_image(res)
# creat_demo(res1)
t1=cv.getTickCount()
t2=cv.getTickCount()
time=(t2-t1)/cv.getTickFrequency()
print("time:%s" %time)

cv.waitKey(0)
cv.destroyAllWindows()