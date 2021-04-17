import numpy as np
import cv2

#load a webcam image
cap = cv2.VideoCapture('../assets/Videos/dog.mp4')   #0: number of the webcam /or use video

while True:
    ret, frame = cap.read()
    #dimensions
    width = int(cap.get(3))
    height=int(cap.get(4))
    # wait 1ms; waitKey returns the key from keyboard that is pressed (as int val)
    #stop when hitting q
    if(cv2.waitKey(1) == ord('q')):
        break
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    blackFrame = np.zeros(frame.shape, dtype='uint8')
    #blackFrame = np.zeros((500,500,3), dtype='uint8')
    blackFrame[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    blackFrame[height // 2:height, :width // 2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    blackFrame[:height // 2, width // 2:width] = smaller_frame
    blackFrame[height // 2:height, width // 2:width] = smaller_frame

    cv2.imshow('blackFrame', blackFrame)

cap.release()
cv2.destroyAllWindows()