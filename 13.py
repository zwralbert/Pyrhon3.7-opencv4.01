import cv2 as cv
import numpy as np


# 高斯金字塔
def pyramid_image(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range( level ):
        dst = cv.pyrDown( temp )
        pyramid_images.append( dst )
        cv.imshow( "gussi" + str( i ), dst )  # 三层重复
        temp = dst.copy()
    return pyramid_images


# 拉普拉斯金子塔图像大小必须是2N次方
def laplian_image(image):
    pyramid_images = pyramid_image( image )
    level = len( pyramid_images )
    for i in range( level - 1, -1, -1 ):
        if (i - 1) < 0:
            expand = cv.pyrUp( pyramid_images[i], dstsize=image.shape[:2] )
            lpls = cv.subtract( image, expand )
            cv.imshow( "lpls" + str(i), lpls )
        else:
            expand = cv.pyrUp( pyramid_images[i], dstsize=pyramid_images[i - 1].shape[:2] )
            lpls = cv.subtract( pyramid_images[i - 1], expand )
            cv.imshow( "lpls" + str(i), lpls )





# 改变图片大小和计算输出时间
src = cv.imread( "D:/Users/zwr/PycharmProjects/python-opencv/picture and video/m1.jpg" )
res = cv.resize( src, (1048, 1048), cv.INTER_CUBIC )
cv.imshow( "change", res )
laplian_image( res )
cv.waitKey( 0 )
cv.destroyAllWindows()
