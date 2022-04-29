#how to capture webcam inside python

#step 1 -import libararies
import cv2 as cv
import numpy as np

#step 2 -read the frames from camera
cap = cv.VideoCapture(0) #webcam no.1

# if (cap.isOpened()==False):
#     print("there is an error")

# read untill end
#step 3 -display frame by frame
while(cap.isOpened()):
    #cap frame by frame
    ret, frame = cap.read()
    if ret== True:
        #to display frame
        cv.imshow("frame",frame)
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break  
    else:
        break

#release or close windows easily
cap.release()
cv.destroyAllWindows()