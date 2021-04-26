import numpy as np
import cv2

cap = cv2.VideoCapture('../assets/Videos/dog.mp4')  #use video rather than camera access
#classifiers are already trained and can be used
#all sorts of classifiers available, e.g.: faces, eyes, nose,...
#here: specific classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #finds all the faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        #draw a rectangle around the images
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        # within the faces find the eyes --> region of interest
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #in all the faces find alle the eyes
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3,5)
        #draw reactangle around eyes
        for (ex, ey, ew, eh) in eyes:
            #be aware: frame and roi_color are of different size
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 5)

    cv2.imshow('frame', frame)
    # if cv2.waitKey() == ord('q'):    #exit when q is hit
    #     break

cap.release()
cv2.destroyAllWindows()