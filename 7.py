import cv2 as cv
import numpy as np
#图像填充以及ROI
def fill_image(image):
    copyimage=image.copy()
    h,w=image.shape[:2]
    mask=np.zeros([h+2,w+2],np.uint8)#函数要求给出范围+2
    cv.floodFill(copyimage,mask,(0,80),(0,100,255),(100,100,50),(50,50,50),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("tianchong",copyimage)

src=cv.imread("D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m1.jpg")
cv.namedWindow("yuantu",cv.WINDOW_NORMAL)
cv.imshow("yuantu",src)
copyimage1=src.copy()
cv.imshow("copyimage1",copyimage1)
fill_image(src)
cv.waitKey(0)
cv.destroyAllWindows()