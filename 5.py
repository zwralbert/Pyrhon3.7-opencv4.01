import cv2 as cv
import numpy as np

def contrast_brightness_image(src1,a,g):
    h,w,ch=src1.shape
    src2=np.zeros([h,w,ch],src1.dtype)
    dst=cv.addWeighted(src1,a,src2,1-a,g)
    cv.imshow("con-bri-demo",dst)

src=cv.imread("D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m1.jpg")
cv.namedWindow("1",cv.WINDOW_NORMAL)
cv.imshow("1",src)
contrast_brightness_image(src,1.2,20)
cv.waitKey(0)
cv.destroyAllWindows()
