import cv2 as cv

#Blur Image
img=cv.imread("photos/me.jpg")
img = cv.resize(img, (800, 600))
#[y1:y2,x1:x2]
cropimg=img[200:600,200:600]
cv.imshow("Me",cropimg)
cv.waitKey(0)