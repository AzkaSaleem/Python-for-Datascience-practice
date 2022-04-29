## video reading, converting into gray/binary and diplaying

# import libararies
import cv2 as cv

cap= cv.VideoCapture("resourses/video.mp4")



#reading and playing
while(True):
    (ret,frame) = cap.read()
    gray= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #for black n white
    #(thresh, binary)= cv.threshold(gray,127,255,cv.THRESH_BINARY)
    if ret == True:
        cv.imshow("video",gray) #replace gray to binary
        # cv.waitKey(1)
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break       
    else:
        break

cap.release()
cv.destroyAllWindows()
     