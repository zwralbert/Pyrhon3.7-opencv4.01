import cv2 as cv
import numpy as np
#图像截取和图像合成
def jie_image(src1):
    src2 = src1[20:230, 40:400]
    cv.imshow( "截取", src2 )
    src1[60:270, 20:380] = src2
    cv.imshow( "合成", src1 )
    
src = cv.imread( "D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m1.jpg" )
cv.namedWindow( "1", cv.WINDOW_NORMAL )
cv.imshow( "1", src )
jie_image( src )
cv.waitKey( 0 )
cv.destroyAllWindows()
