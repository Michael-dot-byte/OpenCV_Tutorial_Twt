import numpy as np
import cv2

#load a webcam image
cap = cv2.VideoCapture('../assets/Videos/dog.mp4')   #0: number of the webcam /or use video

while True:
    ret, frame = cap.read()
    #dimensions
    width = int(cap.get(3))
    height=int(cap.get(4))

    img = cv2.line(frame,(0,0),(width,height),(255,0,0),10)
    img = cv2.line(img, (width,0), (0, height), (0, 255, 0), 10)
    img = cv2.rectangle(img, (100,100), (200,200), (128,128,128),-1)    #-1 to fill the rectangle
    img = cv2.circle(img, (300,300), 50, (255,255,255), 5)      #5 and others (not -1) for thickness of line

    #write text
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'This is my text', (400, 500), font, 2, (0,0,0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)

    # wait 1ms; waitKey returns the key from keyboard that is pressed (as int val)
    #stop when hitting q
    if(cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()