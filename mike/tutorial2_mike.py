import random
import cv2

img = cv2.imread('assets/logo.jpg', -1)
print(img.shape)    #3 channels, bgr

#look at the 257. row and pixel 400 --> has bgr values: [41 98 243]
print(img[257][400])

'''
# manipulate the first 100 rows, all columns, and randomize the 3 pixel values
# (rows, colums, pixels) where pixels: b,g,r
for i in range(100):    #first 100 rows
    for j in range(img.shape[1]):   #all the colums
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('modifiedImage', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#copy one part of the image and copy it somewhere else
#take the pixels from row 500 bis 700 und davon die colums 600:900
tag = img[500:700, 600:900]  #part of the picture

#paste this on another location in the image; needs same dimeension/ size
img[100:300, 650:950] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()