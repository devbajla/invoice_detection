import cv2

img = cv2.imread('assets/invoice_1.jpg', 0)
img = cv2.resize(img, (600,600))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows