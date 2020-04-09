import cv2 as cv
import numpy as np

img= cv.imread('retina5.jpg')
scale_percent = 20
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
finalImage=cv.resize(img,dim)

def vesselSegmentation(Image):
    green_channel=Image[:,:,1]
    clahe=cv.createCLAHE(clipLimit=4,tileGridSize=(8,8))
    cl1=clahe.apply(green_channel)
    blu = cv.blur(cl1, (7, 7))
    blu1 = cv.medianBlur(green_channel, 3)
    subtract = cv.subtract(blu, cl1)
    th1 = cv.adaptiveThreshold(subtract, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    ret, gray = cv.threshold(subtract, 12, 255, cv.THRESH_BINARY)
    _, threshold = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    contours, hierarchy = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    threshold_blob_size = 50
    for i in range(1, len(contours)):
        index_level = int(hierarchy[0][i][1])
        if index_level <= i:
            cnt = contours[i]
            area = cv.contourArea(cnt)
            if area <= threshold_blob_size:
                cv.drawContours(threshold, [cnt], -1, 0, -1, 8)
    kernel = np.ones((2, 2), np.uint8)
    # openmorpho = cv.morphologyEx(threshold, cv.MORPH_OPEN, kernel=np.ones((9, 9), np.uint8))
    # closingMorpho = cv.morphologyEx(openmorpho, cv.MORPH_CLOSE, kernel)
    return threshold

def removalOpticDisc(Image):
    hsv_image = cv.cvtColor(Image, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv_image)
    clahe = cv.createCLAHE(clipLimit=9.0, tileGridSize=(750, 60))
    h = clahe.apply(h)
    s = clahe.apply(s)
    v = clahe.apply(v)
    hsv_image = cv.merge([h, s, v])
    hsv_image = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)
    blur = cv.blur(hsv_image, (5, 5))
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    gblur = cv.GaussianBlur(gray, (9, 9), 1)

    (minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(gblur)
    image = cv.circle(Image, maxLoc, 25, (0, 0, 0), -1)
    return image

def removalOfMacula(Image):
    lower_back = np.array([0, 0, 0], dtype=np.uint8)
    upper_back = np.array([15, 15, 15], dtype=np.uint8)
    mask = cv.inRange(Image, lower_back, upper_back)
    res = cv.bitwise_not(Image, Image, mask)
    lab = cv.cvtColor(res, cv.COLOR_BGR2LAB)
    lab_planes = cv.split(lab)
    clahe = cv.createCLAHE(clipLimit=20.0, tileGridSize=(5, 5))
    lab_planes[0] = clahe.apply(lab_planes[0])
    lab = cv.merge(lab_planes[0])
    blur = cv.blur(lab_planes[0], (9, 9))


# def microaneurysmDetection(Image):
#     hsv_image = cv.cvtColor(Image, cv.COLOR_BGR2HSV)
#     h, s, v = cv.split(hsv_image)
#     clahe = cv.createCLAHE(clipLimit=9.0, tileGridSize=(750, 60))
#     h = clahe.apply(h)
#     s = clahe.apply(s)
#     v = clahe.apply(v)
#     hsv_image = cv.merge([h, s, v])
#     hsv_image = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)
#     blur = cv.blur(hsv_image, (5, 5))
#     gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
#     gblur = cv.GaussianBlur(gray, (9, 9), 1)
#
#     (minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(gblur)
#     image = cv.circle(Image, maxLoc, 25, (0, 0, 0), -1)
#
#     lab1 = cv.cvtColor(Image, cv.COLOR_BGR2LAB)
#
#     b, g, r = cv.split(Image)
#     lab_planes = cv.split(lab1)
#     clahe = cv.createCLAHE(clipLimit=9.0, tileGridSize=(1, 1))
#
#     b = clahe.apply(b)
#     g = clahe.apply(g)
#     r = clahe.apply(r)
#
#     newSize = cv.merge([b, g, r])
#     # green= clahe.apply(green_channel)
#     # red = clahe.apply(red_channel)
#     # blue= clahe.apply(blue_channel)
#     lab_planes[0] = clahe.apply(lab_planes[0])
#     # lab=cv.merge(lab_planes[0])
#
#     # different filtering
#     kernel = np.ones((5, 5), np.float32) / 25
#     convo = cv.filter2D(newSize, -1, kernel)
#     gass = cv.GaussianBlur(convo, (1, 1), 0)
#     median = cv.medianBlur(gass, 5)
#     blur = cv.blur(median, (1, 1))
#     gray_image = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
#     ret, mask = cv.threshold(gray_image, 100, 255, cv.THRESH_BINARY)
#     return mask

vessel=vesselSegmentation(finalImage)
opticDisc= removalOpticDisc(finalImage)
# microaneurysm = microaneurysmDetection(finalImage)
cv.imshow('Vessel Segmentation',vessel)
cv.imshow('Removal Optic Disc',opticDisc)
# cv.imshow('Microaneurysm detection', microaneurysm)
cv.waitKey(0)