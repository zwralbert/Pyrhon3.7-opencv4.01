import cv2 as cv
import numpy as np


def edge_image(image):
    blur = cv.GaussianBlur( image, (3, 3), 0 )
    gray = cv.cvtColor( blur, cv.COLOR_RGB2GRAY )
    # ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    xgrad = cv.Sobel( gray, cv.CV_16SC1, 1, 0 )
    ygrad = cv.Sobel( gray, cv.CV_16SC1, 0, 1 )
    edge_output = cv.Canny( xgrad, ygrad, 50, 100 )
    cv.imshow( "canny", edge_output )
    # dst = cv.bitwise_and( image, image, mask=edge_output )
    # cv.imshow( "color", dst )

#轮廓检测
def contours_image(image):
    dst = cv.GaussianBlur( image, (5, 5), 0 )
    gray = cv.cvtColor( dst, cv.COLOR_RGB2GRAY )
    ret, binary = cv.threshold( gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU )
    cv.imshow( "binary", binary )
    # binary=edge_image(image)

    contours, heriachy = cv.findContours( binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE )  # 第二个参数修改
    for i, contour in enumerate( contours ):
        cv.drawContours( image, contours, i, (0, 0, 255), 1 )
    cv.imshow( "contours", image )


# 改变图片大小和计算输出时间
src = cv.imread( "D:/Users/zwr/PycharmProjects/python-opencv/picture and video/m5.jpg" )
res = cv.resize( src, (340, 400), cv.INTER_CUBIC )
contours_image( res )
edge_image( res )
cv.waitKey( 0 )
cv.destroyAllWindows()
