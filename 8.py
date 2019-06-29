import cv2 as cv
import numpy as np

#图像模糊以及各种滤波
#def mo_demo(src1):

    # src2=cv.blur(src1,(10,10))#数值愈大愈模糊
    # cv.imshow("blur",src2)##卷积公式

    # src2=cv.medianBlur(src1,3)#椒盐噪声的化解
    # cv.imshow("medianBlur",src2)

    # src3=cv.GaussianBlur(src1,(7,7),2)
    # cv.imshow("GaussianBlur",src3)
    #
     # src2=cv.bilateralFilter(src1,10,10,2)#双边滤波器的美颜
     # cv.imshow("bilateralFilter",src2)
    #
    # src2=cv.pyrMeanShiftFiltering(src1,5,10)
    # cv.imshow("pyrMeanShiftFiltering",src2)

#自定义模糊
def zi_image(src1):
    kernel1 = np.ones( (5, 5), np.float ) /25  # 自定义矩阵，并防止数值溢出，修改模糊效果
    src2 = cv.filter2D( src1, -1, kernel1 )
    cv.imshow( "blur", src2 )
    kernel2 = np.array( [[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32 )
    src2 = cv.filter2D( src1, -1, kernel2 )#锐化效果
    cv.imshow( "filter", src2 )



src = cv.imread( "D:/Users/zwr/PycharmProjects/scikit-learn/picture and video/m3.jpg" )
src2=cv.resize(src,(400,300),cv.INTER_CUBIC)
cv.namedWindow( "1", cv.WINDOW_NORMAL )
cv.imshow( "1", src2 )
# mo_demo(src2)
zi_image(src2)
cv.waitKey( 0 )
cv.destroyAllWindows()
