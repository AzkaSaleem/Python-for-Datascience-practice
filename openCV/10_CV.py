#how to capture webcam inside python and converting into gray and binary 

#step 1 -import libararies

import cv2 as cv
import numpy as np

#step 2 -read the frames from camera
cap = cv.VideoCapture(0) #webcam no.1

while(True):
    (ret, frame) = cap.read()
    gray= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary)= cv.threshold(gray,127,255,cv.THRESH_BINARY)


    cv.imshow('originalcam', frame)
    cv.imshow('graycam', gray)
    cv.imshow('bwcam', binary)
    
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break  

#release or close windows easily
cap.release()
cv.destroyAllWindows()