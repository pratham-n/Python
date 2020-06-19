import cv2

img= cv2.imread("test_image.jpg",1)
cv2.imshow("test_image",img)
cv2.waitkey(2000)
cv2.destroyAllWindows()
