#!/usr/bin/env python3

import cv2


def getDim (img):
    shape = img.shape
    dimensions = (heigh, width) = (shape[0], shape[1])
    return dimensions

def turnBlack (img):
    # in order to turn an image black we need to first greysale it
    # this is due to the fact that we need to apply a treshhold technic to the image
    # threshhold is a binary sequence operation on images
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, bw) = cv2.threshold(grayImage, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return bw

def resize(img, width, height):
    return cv2.resize (img, (width, height), interpolation= cv2.INTER_LINEAR)


    
IMGSOURCE = 'dog.png'
img = cv2.imread(IMGSOURCE)
resized = resize (img, 100, 100)


cv2.imshow('Original image',resized)
cv2.imshow('black and white', turnBlack(resized))

cv2.waitKey(0)
cv2.destroyAllWindows()
