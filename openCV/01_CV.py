## Reading an image and displaying it

# import libararies
import cv2 as cv

#read imgage
img= cv.imread("resourses/image.jpg")

#show image
cv.imshow('pehli pic',img)

#display time
cv.waitKey(0)
