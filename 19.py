import cv2 as cv
import numpy as np


# 对象测量
def measure_object(image):
    gray = cv.cvtColor( image, cv.COLOR_BGR2GRAY )
    ret, binary = cv.threshold( gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU )
    print( "threshold value: %s" % ret )
    cv.imshow( "binary image", binary )
    dst=cv.cvtColor(binary,cv.COLOR_GRAY2BGR)
    contours, hierarchy = cv.findContours( binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE )
    for i, contour in enumerate( contours ):
        # cv.drawContours( image, contours, i, (0, 255, 255), 1 )  # 用黄色线条画出轮廓

        area = cv.contourArea( contour )  # 计算轮廓面积
        print( "contour area:", area )

        # 轮廓周长,第二参数可以用来指定对象的形状是闭合的（True),还是打开的（一条曲线）。
        perimeter = cv.arcLength( contour, True )

        print( "contour perimeter:", perimeter )

        x, y, w, h = cv.boundingRect( contour )  # 用矩阵框出轮廓
        cv.rectangle( image, (x, y), (x + w, y + h), (0, 0, 255), 2 )

        rate = min( w, h ) / max( w, h )  # 计算矩阵宽高比
        print( "rectangle rate", rate )

        mm = cv.moments( contour )  # 函数 cv2.moments() 会将计算得到的矩以一个字典的形式返回
        # 计算出对象的重心
        cx = mm['m10'] / mm['m00']
        cy = mm['m01'] / mm['m00']
        cv.circle( image, (np.int( cx ), np.int( cy )), 2, (0, 255, 255), -1 )  # 用实心圆画出重心
        # epsilon=cv.arcLength(contour,True)
        approx=cv.approxPolyDP(contour,4,True)
        print(approx.shape)
        if approx.shape[0]==4:
            cv.drawContours(dst,contours,i,(0,0,255),2)

    cv.imshow( "measure_object", dst )


# 改变图片大小和计算输出时间
src = cv.imread( "D:/Users/zwr/PycharmProjects/python-opencv/picture and video/m9.jpg" )
res = cv.resize( src, (340, 400), cv.INTER_CUBIC )
cv.imshow( "change", res )
measure_object( res )

cv.waitKey( 0 )
cv.destroyAllWindows()
