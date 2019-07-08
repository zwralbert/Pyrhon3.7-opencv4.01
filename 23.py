import cv2 as cv
import numpy as np
import pytesseract as tess
from PIL import Image


def recongnition_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_OTSU|cv.THRESH_BINARY)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    mroph=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel=kernel)
    cv.imshow("mroph",mroph)
    textImage=Image.fromarray(mroph)
    text=tess.image_to_string(textImage)
    print("result",text)


src=cv.imread("D:/Users/zwr/PycharmProjects/python-opencv/picture and video/m13.jpg")
cv.namedWindow("result",cv.WINDOW_AUTOSIZE)
cv.imshow("first",src)
res=cv.resize(src,(500,500))
recongnition_demo(res)
cv.waitKey(0)
cv.destroyAllWindows()


