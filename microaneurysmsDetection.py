import cv2 as cv
import numpy as np

import  os
import  sys
from matplotlib import pyplot as plt

img=cv.imread('retina5.jpg', 1)

scale_percent = 20
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv.resize(img,dim)

# cv.imshow('mainImage',resized)

hsv_image= cv.cvtColor(resized, cv.COLOR_BGR2HSV)
h,s,v = cv.split(hsv_image)
clahe = cv.createCLAHE(clipLimit=9.0,tileGridSize=(750,60))
h= clahe.apply(h)
hsv_image=cv.merge([h,s,v])
hsv_image=cv.cvtColor(hsv_image,cv.COLOR_HSV2BGR)
# lab = cv.merge()
# bgr = cv.cvtColor(lab, cv.COLOR_HSV2BGR)

blur = cv.blur(hsv_image,(5,5))
gray=cv.cvtColor(blur,cv.COLOR_BGR2GRAY)
gblur=cv.GaussianBlur(gray,(9,9),1)

(minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(gblur)
image=cv.circle(resized, maxLoc, 25, (0,0 , 0),-1)

# for patches
# print(resized)
# GRID_SIZE = 20
# height, width, channels = resized.shape
# for x in range(0, width -1  , GRID_SIZE):
#      cv.line(resized, (x, 0), (x, height), (255, 0, 0), 1, 1)
#      cv.line(resized, (0, x), (width, x),   (255,0,0))
# cv.imshow('Hehe', resized)
# gray_image = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
# sift = cv.SIFT()
# keypoints = sift.detect(gray_image, None)
# input_image = cv.drawKeypoints(resized, keypoints,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv.imshow('SIFT features', input_image)
#
lab1=cv.cvtColor(resized,cv.COLOR_BGR2LAB)

# red_channel=resized[:,:,0]
# red_img = np.zeros(resized.shape)
# red_img[:,:,0]=red_channel
# green_channel=resized[:,:,2]
# blue_channel=resized[:,:,1]
# cv.imshow("green",lab1)
# cv.imshow('green',red_img)
b,g,r =cv.split(resized)
lab_planes = cv.split(lab1)
clahe=cv.createCLAHE(clipLimit=9.0,tileGridSize=(1,1))

b= clahe.apply(b)
g= clahe.apply(g)
r= clahe.apply(r)

resized = cv.merge([b,g,r])
# green= clahe.apply(green_channel)
# red = clahe.apply(red_channel)
# blue= clahe.apply(blue_channel)
lab_planes[0]=clahe.apply(lab_planes[0])
# lab=cv.merge(lab_planes[0])

#different filtering
kernel= np.ones((5,5),np.float32)/25
convo= cv.filter2D(resized,-1,kernel)
gass =cv.GaussianBlur(convo,(1,1),0)
median =cv.medianBlur(gass,5)
blur=cv.blur(median,(1,1))


gray_image = cv.cvtColor(blur,cv.COLOR_BGR2GRAY)
ret,mask = cv.threshold(gray_image,100,255,cv.THRESH_BINARY)


cv.imshow("gray",gray_image)
cv.imshow('binary',mask)
cv.imshow('new size',resized)
# cv.imshow('clahe',lab_planes[0])
# cv.imshow('lab',green)
# cv.imshow('red',red)
# cv.imshow('blue',blue)
cv.imshow("convo",convo)
cv.imshow('blur',blur)
# cv.imshow('lab',hsv)
# cv.imshow('image',image)
# cv.imshow('hsv',hsv_image)
# cv.imshow('blur',blur)
# cv.imshow('gray',gray)
# cv.imshow('gaussianblur',gblur)
# cv.imshow('green channel',resized[:,:,0])
# cv.imshow('green channel',resized[:,:,1])
# cv.imshow('blue channel',resized[:,:,2])


print(resized.size)
print(resized.shape)
cv.waitKey(0)