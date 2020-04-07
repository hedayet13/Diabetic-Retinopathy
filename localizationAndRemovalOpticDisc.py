import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('retina1.png', 1)

scale_percent = 20
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv.resize(img,dim)

hsv_image= cv.cvtColor(resized, cv.COLOR_BGR2HSV)
h,s,v = cv.split(hsv_image)
clahe = cv.createCLAHE(clipLimit=5.0,tileGridSize=(4,4))
h= clahe.apply(h)
s=clahe.apply(s)
v=clahe.apply(v)
hsv_image=cv.merge([h,s,v])
hsv_image=cv.cvtColor(hsv_image,cv.COLOR_HSV2BGR)
# lab = cv.merge()
# bgr = cv.cvtColor(lab, cv.COLOR_HSV2BGR)

blur = cv.blur(hsv_image,(5,5))
gray=cv.cvtColor(blur,cv.COLOR_BGR2GRAY)
gblur=cv.GaussianBlur(gray,(5,5),1)

(minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(gblur)
image=cv.circle(resized, maxLoc, 25, (0,0 , 0), -1)


cv.imshow('new size',resized)
# cv.imshow('lab',hsv)
cv.imshow('image',image)
cv.imshow('hsv',hsv_image)
cv.imshow('blur',blur)
cv.imshow('gray',gray)
cv.imshow('gaussianblur',gblur)

cv.waitKey(0)