import cv2 as cv
import numpy as np
import matplotlib
from PIL import Image
import glob


img = cv.imread("retina.jpg",1)

scale_percent = 30
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resize = cv.resize(img,dim)

imgHeight = resize.shape[0]
imgWidth  = resize.shape[1]
M= imgHeight//2
N= imgWidth//2
tiles= []
for y in range(0, imgHeight,M):
    for x in range(0,imgWidth,N):
        tiles=resize[y:y+M,x:x+N]
        print(tiles)
        cv.imshow('s',tiles)

cv.imshow("newSize",resize)
cv.waitKey(0)