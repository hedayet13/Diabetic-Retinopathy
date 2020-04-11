import cv2 as cv
import numpy as np

Image = cv.imread('retina5.jpg',1)

imgheight =Image.shape[0]
imgwidth = Image.shape[1]
m=imgheight//4
n=imgwidth//4

for x in range(0,imgheight,m):
    for y in range(0,imgwidth,n):
        tiles = Image[x:x+m,y:y+n]



        print(tiles)
        cv.imshow('tiles',tiles)

        cv.waitKey(0)