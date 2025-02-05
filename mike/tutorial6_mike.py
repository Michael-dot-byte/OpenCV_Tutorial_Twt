import numpy as np
import cv2

img = cv2.imread('../assets/chessboard.png')
img = cv2.resize(img, (0,0),fx= 0.75, fy=0.75)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#return N (100) best corners in image
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()       #flattens an array: [[[x,y]]] --> [x,y]
    cv2.circle(img, (x,y), 5,(255,0,0),-1)  #draw edges on the image as circle

#draw a line between the corners
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])  # [0] needed because corner is [[x,y]]
        corner2 = tuple(corners[j][0])
        # 3 random values
        # map maps a function to values; here: each return value from random shall be converted into python int
        # map used in combination with lambda: value: return value
        color = tuple(map(lambda x: int(x), np.random.randint(0,255, size=3)))
        cv2.line(img, corner1, corner2, (),1)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()