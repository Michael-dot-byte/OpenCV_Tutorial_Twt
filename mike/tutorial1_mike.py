import cv2

#load image
img = cv2.imread('assets/logo.jpg', cv2.IMREAD_COLOR)   #loads images in bgr
cv2.imshow('logo', img)
cv2.waitKey(0)  #wait an infinite amout of time
cv2.destroyAllWindows()

#resize and rotate
#img = cv2.resize(img,(400,400))    # resize to pixel value
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)    # resize according to a factor
cv2.imshow('logo', img)
cv2.waitKey(0)  #wait an infinite amout of time
cv2.destroyAllWindows()

#rotate image
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

#save image
cv2.imwrite('assets/rotated_logo.jpg', img)

cv2.imshow('logo', img)
cv2.waitKey(0)  #wait an infinite amout of time
cv2.destroyAllWindows()
