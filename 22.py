import cv2 as cv
import numpy as np
#人脸检测 2个包
def face_detection_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    face_detector=cv.CascadeClassifier("C:/Users/zwr/Desktop/opencv_exercises-master/haarcascade_frontalface_alt_tree.xml")
    faces=face_detector.detectMultiScale(gray,1.02,5)
    for x,y,w,h in faces:
        cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow("result",image)

def video_capture_demo():
    capture=cv.VideoCapture(0)
    cv.namedWindow("result",cv.WINDOW_AUTOSIZE)
    while True:
        ret,frame=capture.read()
        frame=cv.flip(frame,2)
        face_detection_demo(frame)
        c=cv.waitKey(10)
        if c==27:
            break


# 改变图片大小和计算输出时间
src = cv.imread( "D:/Users/zwr/PycharmProjects/python-opencv/picture and video/m3.jpg" )
cv.namedWindow("result",cv.WINDOW_AUTOSIZE)
video_capture_demo()
# face_detection_demo(src)
cv.waitKey( 0 )
cv.destroyAllWindows()
