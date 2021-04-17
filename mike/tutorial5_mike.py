import numpy as np
import cv2

#load a webcam image
cap = cv2.VideoCapture('../assets/Videos/dog.mp4')   #0: number of the webcam /or use video

while True:
    ret, frame = cap.read()
    #dimensions
    width = int(cap.get(3))
    height=int(cap.get(4))

    #convert colors bgr in hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #define colors that shall be extracted
    lower_blue = np.array([110,50,50])  #colors are hsv format (done with hsv color picker)
    upper_blue = np.array([130, 255,255])

    #only takes the pixels that are within this given range
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    #only use the pixels in the original img if the color is defined in mask, otherwise turn the pixel black
    #bitwise_and: 1 and 1 = 1; 0 and 1 = 0; 0 and 0 = 0
    result = cv2.bitwise_and(frame,frame, mask=mask)    #takes two images and uses the common pixels

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    # wait 1ms; waitKey returns the key from keyboard that is pressed (as int val)
    #stop when hitting q
    if(cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()