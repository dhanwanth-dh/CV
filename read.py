import cv2 as cv

#Image
'''img=cv.imread("photos/me.jpg")
cv.imshow("Me",img)
cv.waitKey(0)'''

#Video
'''vid=cv.VideoCapture("videos/mevid.mp4")
trial=True
while trial:
    trial,img=vid.read()
    cv.imshow("Video", img)
    cv.waitKey(10)'''

#Webcam
vid=cv.VideoCapture(0)
trial=True
while trial:
    trial,img=vid.read()
    cv.imshow("Video", img)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break