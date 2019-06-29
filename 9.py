import cv2 as cv
import numpy as np
#图像粗略调节对比度和亮度
def contrast_brigthless_image(src1,a,g):
    h,w,ch=src1.shape
    src2=np.zeros([h,w,ch],src1.dtype)
    dst=cv.addWeighted(src1,a,src2,1-a,g)
    cv.imshow("con_bri_image",dst)
src=cv.imread("D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m1.jpg")
cv.namedWindow("first",cv.WINDOW_NORMAL)
cv.imshow("first",src)
contrast_brigthless_image(src,1,5)#后面两个参数分别是亮度和对比度，第二是原图的倍数，第三是原来加上这个数值
res=cv.resize(src,(1340,1104),cv.INTER_CUBIC)
cv.imshow("change",res)
t1=cv.getTickCount()
t2=cv.getTickCount()
time=(t2-t1)/cv.getTickFrequency()
print("time:%s" %time)

cv.waitKey(0)
cv.destroyAllWindows()