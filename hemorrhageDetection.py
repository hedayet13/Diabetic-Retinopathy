import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_extraction.image import extract_patches_2d
from skimage.util import view_as_windows


img=cv.imread('retina5.jpg')

finalImage = cv.resize(img,(640,440))
green_channel = finalImage[:,:,1]
median1 = cv.medianBlur(green_channel,5)
median2 = cv.medianBlur(green_channel,15)
shadedCorrectedImage= cv.subtract(median2,median1)
# topHat= cv.morphologyEx(shadedCorrectedImage,cv.MORPH_TOPHAT,kernel=np.ones((10,10),np.uint8))

topHat= cv.morphologyEx(shadedCorrectedImage,cv.MORPH_TOPHAT,kernel=np.ones((2,2),np.uint8))
substract2=cv.subtract(shadedCorrectedImage,topHat)
sub1=shadedCorrectedImage-topHat
sub = topHat-shadedCorrectedImage
adaptiveThreshold= cv.adaptiveThreshold(sub1, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

# adaptiveThreshold= cv.adaptiveThreshold(adaptiveThreshold, 240, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 3, 2)
print(topHat.shape)
cv.imshow('final image',finalImage)
# cv.imshow('greenchannel',green_channel)
cv.imshow('median1',median1)
cv.imshow('median2',median2)
cv.imshow('Shaded corrected Image',shadedCorrectedImage)
# cv.imshow('substracted ',substract2)
cv.imshow('adaptive',adaptiveThreshold)
# cv.imshow('Top Hat',topHat)
# cv.imshow('sub',sub)
# cv.imshow('opening',opening)
cv.waitKey(0)

