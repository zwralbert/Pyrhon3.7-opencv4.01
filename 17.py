import cv2 as cv
import numpy as np


# 霍夫直线检测前提是灰度和canny邊緣检测
def line_image(image):
    gray = cv.cvtColor( image, cv.COLOR_BGR2GRAY )
    edges = cv.Canny( gray, 50, 150, apertureSize=3 )
    lines = cv.HoughLines( edges, 2, np.pi / 180, 200 )
    # lines=cv.HoughLinesP( edges, 1, np.pi / 180, minLineLength=100,maxLineGap=10)
    for line in lines:
        rho, theta = line[0]
        a = np.cos( theta )
        b = np.sin( theta )
        x0 = a * rho
        y0 = b * rho
        x1 = int( x0 + 1000 * (-b) )
        y1 = int( y0 + 1000 * (a) )
        x2 = int( x0 - 1000 * (-b) )
        y2 = int( y0 - 1000 * (a) )
        cv.line( image, (x1, y1), (x2, y2), (0, 0, 255), 2 )
    cv.imshow( "直线", image )

#霍夫圆检测
def circle_image(image):
    dst = cv.GaussianBlur(image,(5,5),50)
    cgray = cv.cvtColor( dst, cv.COLOR_RGB2GRAY )
    circles = cv.HoughCircles( cgray, cv.HOUGH_GRADIENT, 1, 20, param1=10, param2=70, minRadius=0, maxRadius=0 )
    #param1=定义的漂移物理空间半径大小；param2=定义的漂移色彩空间半径大小；
    circles = np.uint16( np.around( circles ) )
    for i in circles[0, :]:
        cv.circle( image, (i[0], i[1]), i[2], (0, 0, 255), 2 )
        cv.circle( image, (i[0], i[1]), 2, (255, 0, 0),2)
    cv.imshow( "circles", image )




src = cv.imread( "D:/Users/zwr/PycharmProjects/python-opencv/picture and video/m6.jpg" )
res = cv.resize( src, (340, 400), cv.INTER_CUBIC )
cv.imshow( "change", res )
# circle_image( src )
line_image( res )
cv.waitKey( 0 )
cv.destroyAllWindows()
