import cv2 as cv
import numpy as np
#分水岭算法  灰度->二值化->距离变换->寻找种子->生成Maker->分水岭变换_>输出
def watershed_demo(image):
    blurred=cv.pyrMeanShiftFiltering(image,10,100)
    gray=cv.cvtColor(blurred,cv.COLOR_RGB2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary",binary)

    #形态学去噪
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    sure=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel,iterations=2)
    sure1=cv.dilate(sure,kernel,iterations=3)
    cv.imshow("surel",sure1)

    #distance transform
    distance=cv.distanceTransform(sure1,cv.DIST_L2,3)
    ret,sure_fg=cv.threshold(distance,0.7*distance.max(),255,0)

    #find seed
    sure_fg=np.uint8(sure_fg)
    unknown=cv.subtract(sure1,sure_fg)
    ret1,makers=cv.connectedComponents(sure_fg)



    #watershed
    makers=makers+1
    makers[unknown==255]=0
    makers3=cv.watershed(image,makers)
    image[makers3==-1]=[0,0,255]
    cv.imshow("result",image)

# 改变图片大小和计算输出时间
src = cv.imread( "D:/Users/zwr/PycharmProjects/python-opencv/picture and video/m11.jpg" )

res = cv.resize( src, (340, 400), cv.INTER_CUBIC )
cv.imshow( "change", res )
watershed_demo(res)

cv.waitKey( 0 )
cv.destroyAllWindows()
