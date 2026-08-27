import cv2 as cv

#Blur Image
img=cv.imread("photos/me.jpg")
img = cv.resize(img, (800, 600))
blurimg=cv.GaussianBlur(img,(15,15),10)
# cv.imshow("Me",img)
# cv.waitKey(0)
cv.imshow("Me",blurimg)
cv.waitKey(0)