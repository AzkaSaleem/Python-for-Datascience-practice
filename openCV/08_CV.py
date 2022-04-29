## video reading, converting into gray/binary, diplaying and saving

# import libararies
import cv2 as cv
from matplotlib.colors import is_color_like

#reading/loading
cap= cv.VideoCapture("resourses/video.mp4")

#writting format,codec, video writer object and file output
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
out= cv.VideoWriter("resourses/out_video.avi",cv.VideoWriter_fourcc('M','J','P','G'),10,(frame_width, frame_height),isColor=False)

#reading and playing
while(True):
    (ret,frame) = cap.read()
    gray= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #for black n white
    #(thresh, binary)= cv.threshold(gray,127,255,cv.THRESH_BINARY)
    if ret == True:
        out.write(gray)
        cv.imshow("video",gray) #replace gray to binary
        # cv.waitKey(1)
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break       
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()