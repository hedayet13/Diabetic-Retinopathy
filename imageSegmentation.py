import cv2 as cv
im=cv.imread('retina5.jpg')
imgheight = im.shape[0]
imgwidth = im.shape[1]
M=imgheight//4
N=imgwidth//4

for y in range (0,imgheight,M):
    for x in range(0,imgwidth,N):
        tiles= im[y:y+M,x:x+N]
        print(tiles)
        cv.imshow('tiles',tiles)
        cv.waitKey(0)