import cv2 as cv
import numpy as np
#读出图像大小和通道
def access_pixels(image):
    print(image.shape)
    height=image.shape[0]
    width=image.shape[1]
    channels=image.shape[2]
    print("width: %s,height: %s channels : %s"%(width,height,channels))
    for row in range (height):
        for col in range (width):
            for c in range(channels):
                pv=image[row,col,c]
                image[row,col,c]=255-pv
                cv.imshow("pixels_demo",image)

src=cv.imread("D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m1.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
# cv.imshow("input image",src)
access_pixels(src)
cv.waitKey(0)
cv.destroyAllWindows()

