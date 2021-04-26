import numpy as np
import cv2

img = cv2.resize(cv2.imread('../assets/soccer_practice.jpg',0), (0,0), fx= 0.8, fy=0.8)
template = cv2.resize(cv2.imread('../assets/shoe.PNG',0), (0,0), fx=0.8, fy=0.8)
h,w =template.shape     #is only a grayscale, so no rgb values

#available methodes for template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

#not all methodes produce the correct results!
for method in methods:
    img2 = img.copy()   #use copy of base image otherwise all methods would be applied on the original
    #slide template around on the original to find position of template on image
    #result: (W-w+1, H-h+1)
    result = cv2.matchTemplate(img2, template, method)
    #result might look like this
    #[[0,0,0],
    # [0,1,0],
    # [0,0,0]]
    #--> template is right in the middle of the image
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc, max_loc)
    #draw a rectangel around to location where template was found
    if method is [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0]+w, location[1]+h)  #find the bottom corner of the image
    cv2.rectangle(img2, location, bottom_right, 255,5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# template image (e.g. ball) need to have about the same size as in the image where they are searched for