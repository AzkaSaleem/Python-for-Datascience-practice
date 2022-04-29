## Reading an image, Resizing and displaying it

# import libararies
import cv2 as cv

# reading
img= cv.imread("resourses/image.jpg")
#resizing
img= cv.resize(img,(800,600))

cv.imshow('pehli pic',img)

cv.waitKey(0)
cv2.destroyAllWindows()