## video reading and diplaying

# import libararies
import cv2 as cv

#reading video frames
cap= cv.VideoCapture("resourses/video.mp4")

#indicator
if (cap.isOpened()==False):
    print("error in reading video")

#reading and playing
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        cv.imshow("video",frame)
        # cv.waitKey(1)
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break       
    else:
        break

cap.release()
cv.destroyAllWindows()