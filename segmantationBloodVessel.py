import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('retina2.jpg', 1)

scale_percent = 30
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

kernel = np.ones((2,2),np.uint8)
#resized
resized=cv.resize(img,dim)
#extracted green channel
green_channel = resized[:,:,1]

#equalizations
equ=cv.equalizeHist(green_channel)
#clahe
clahe=cv.createCLAHE(clipLimit=2,tileGridSize=(8,8))
cl1=clahe.apply(green_channel)
# lab=cv.cvtColor(green_channel,cv.COLOR_BGR2LAB)
# lab_planes = cv.split(lab)
# clahe=cv.createCLAHE(clipLimit=2.0,tileGridSize=(500,500))
# lab_planes[0]=clahe.apply(lab_planes[0])
# lab=cv.merge(lab_planes)
# bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)

# blur
blu=cv.blur(cl1,(7,7))
blu1=cv.medianBlur(green_channel,3)
#thresholding

th2=cv.adaptiveThreshold(blu1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

#subtraction
subtract=cv.subtract(blu,cl1)

th1=cv.adaptiveThreshold(subtract,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)

# gradient=cv.morphologyEx(subtract,cv.MORPH_GRADIENT,kernel)
# closing=cv.morphologyEx(subtract,cv.MORPH_CLOSE,kernel)
ret,gray=cv.threshold(subtract,12,255,cv.THRESH_BINARY)
#cannyedge
edges=cv.Canny(blu1,100,200)


#contours
_,threshold = cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
contours,hierarchy=cv.findContours(threshold,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

threshold_blob_size = 4

for i in range(1,len(contours)):
    index_level =int(hierarchy[0][i][1])
    if index_level <= i :
        cnt =contours[i]
        area = cv.contourArea(cnt)
        print(area)
        if area<= threshold_blob_size:
            cv.drawContours(threshold,[cnt],-1,0,-1,8)
print(len(contours))
openmorpho=cv.morphologyEx(threshold,cv.MORPH_OPEN,kernel=np.ones((9,9),np.uint8))
closingMorpho =cv.morphologyEx(threshold,cv.MORPH_CLOSE,kernel)


# cv.drawContours(resized,contours,-1,(0,0,255),1)
# cv.polylines(threshold,contours,1,(255,255,255))








#ALLshow
cv.imshow('resizedImage',resized)
# cv.imshow('green_channel',green_channel)
# cv.imshow('equalization',equ)
# cv.imshow('clahe',cl1)
# cv.imshow('Blur',blu)
# cv.imshow('mean Thresholding',th1)
# cv.imshow('gaussianThresholding',th2)
cv.imshow('subtracted',subtract)
# cv.imshow('morphological',opening)
# cv.imshow('gray',gray)
# cv.imwrite('binaryImage.png',gray)
# cv.imshow("edges",edges)
cv.imshow('threshold',threshold)
cv.imshow('final',closingMorpho)
plt.hist(img.ravel(),256,[0,256])
# plt.show()
cv.waitKey(0)