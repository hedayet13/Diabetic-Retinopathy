import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_extraction.image import extract_patches_2d
from skimage.util import view_as_windows


img=cv.imread('retina.jpg', 1)

scale_percent = 30
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resize = cv.resize(img,dim)

A=np.arange(4*4).reshape(4,4)
window_shape=(50,50)
B=view_as_windows(A,window_shape)
print(B)
print(A)

print(B.shape)
# cv.imshow("gBLUR",gblur)
# cv.imshow("orginal",resize)
# cv.imshow("gray",gray)
cv.waitKey(0)

