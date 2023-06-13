import cv2
import numpy as np

img = cv2.imread('assets/invoice_1.jpg')
word = img[196:228,1663:1730]
word = cv2.resize(word,(0,0), fx= 4, fy = 4)
gray = cv2.cvtColor(word, cv2.COLOR_BGR2GRAY)


corners = cv2.goodFeaturesToTrack(gray,50, 0.01,10)
corners = np.int0(corners)

for corner in corners: 
    x,y = corner.ravel()
    cv2.circle(word,(x,y), 1, (0, 0, 255), -1)

cv2.imshow('word',word)
cv2.waitKey(0)
cv2.destroyAllWindows  