## Reading an image, Resizing, converting into gray and displaying it

# import libararies
import cv2 as cv
from cv2 import cvtColor

img= cv.imread("resourses/image.jpg")
img= cv.resize(img,(600,400))

#conversion to gray
gray_img= cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('pehli pic',img)
cv.imshow('gray pic',gray_img)

#displaycode
cv.waitKey(0)
cv2.destroyAllWindows()