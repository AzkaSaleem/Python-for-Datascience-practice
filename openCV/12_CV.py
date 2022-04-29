## saving videos from cam in gray

# import libararies
import cv2 as cv
import numpy as np

#reading/loading
cap= cv.VideoCapture(0)

#writting format,codec, video writer object and file output
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
out= cv.VideoWriter("resourses/gray_video.avi",cv.VideoWriter_fourcc('M','J','P','G'),50,(frame_width, frame_height),isColor=False)

#reading and playing
while(True):
    (ret,frame) = cap.read()
    gray= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if ret == True:
        out.write(gray)
        cv.imshow("video",gray)
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break       
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()