import cv2 as cv
import numpy as np

#模板匹配，用很多种方法平方，平方归一化，匹配归一化
def template_image():
    tp1 = cv.imread( "D:/Users/zwr/PycharmProjects/python-opencv/picture and video/m4.jpg" )
    target = cv.imread( "D:/Users/zwr/PycharmProjects/python-opencv/picture and video/m3.jpg" )
    cv.imshow( "model", tp1 )

    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]#三种方法的API
    th, tw = tp1.shape[:2]
    for md in methods:
        print( md )
        result=cv.matchTemplate(target,tp1,md)
        min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
        if md==cv.TM_SQDIFF_NORMED:
            t1=min_loc
        else:
            t1=max_loc
        br=(t1[0]+tw,t1[1]+th)
        cv.rectangle(target,t1,br,(0,0,255),2)
        cv.imshow("pipei"+np.str(md),target)
        # cv.imshow( "pipei" + np.str( md ), result )


# 改变图片大小和计算输出时间
src = cv.imread( "D:/Users/zwr/PycharmProjects/python-opencv/picture and video/m1.jpg" )
res = cv.resize( src, (1340, 1104), cv.INTER_CUBIC )
template_image()
cv.waitKey( 0 )
cv.destroyAllWindows()
