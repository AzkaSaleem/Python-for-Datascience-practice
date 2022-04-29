## Reading an image, Resizing, converting into gray and binaray
## image saving with writting

# import libararies
import cv2 as cv
from cv2 import imwrite
from cv2 import imshow

#reading resizing
img= cv.imread("resourses/image.jpg")
img= cv.resize(img,(600,400))


#conversion to gray
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#conversion to black-white
(thresh, binary)= cv.threshold(gray,127,255,cv.THRESH_BINARY)

#show
cv.imwrite('resourses/pehli pic.png',img)
cv.imwrite('resourses/gray pic.png',gray)
cv.imwrite('resourses/bw pic.png',binary)
