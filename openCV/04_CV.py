# import libararies
import cv2 as cv

img= cv.imread("resourses/image.jpg")
img= cv.resize(img,(600,400))


#conversion to gray
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary)= cv.threshold(gray,127,255,cv.THRESH_BINARY)

#show
cv.imshow('pehli pic',img)
cv.imshow('gray pic',gray)
cv.imshow('bw pic',binary)

#displaycode
cv.waitKey(0)
cv2.destroyAllWindows()