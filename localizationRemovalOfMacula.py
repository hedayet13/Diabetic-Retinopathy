import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('retina5.jpg', 1)
print(img.shape)
scale_percent = 40
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv.resize(img,dim)
print(resized.shape)
hsv=cv.cvtColor(resized,cv.COLOR_BGR2HSV)

lower_back=np.array([0,0,0],dtype=np.uint8)
upper_back=np.array([15,15,15],dtype=np.uint8)

mask =cv.inRange(resized,lower_back,upper_back)
res =cv.bitwise_not(resized,resized,mask)

lab=cv.cvtColor(res,cv.COLOR_BGR2LAB)


lab_planes = cv.split(lab)
clahe=cv.createCLAHE(clipLimit=5.0,tileGridSize=(7,7))
lab_planes[0]=clahe.apply(lab_planes[0])
lab_planes[1]=clahe.apply(lab_planes[1])
lab_planes[2]=clahe.apply(lab_planes[2])
lab =cv.merge(lab_planes)
lab = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
blur =cv.blur(lab,(5,5))
blur= cv.bilateralFilter(blur,10,75,75)
gray = cv.cvtColor(blur,cv.COLOR_BGR2GRAY)
ret,thresh1 = cv.threshold(gray,40,255,cv.THRESH_BINARY)
# cv.imshow('mask',mask)
# cv.imshow('res',res)

cv.imshow('NewSize',resized)
cv.imshow('lab',lab_planes[0])
cv.imshow('blur',gray)
cv.imshow('l',thresh1)


# cv.imshow('testpng',tmp)
cv.waitKey(0)