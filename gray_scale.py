import cv2 as cv

#Grayscale Image
img=cv.imread("photos/me.jpg")
grayimg=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img = cv.resize(img, (800, 600))
grayimg = cv.resize(grayimg, (800, 600))
cv.imshow("Me",img)
cv.waitKey(0)
cv.imshow("Me",grayimg)
cv.waitKey(0)