import cv2
import numpy as np

image = cv2.imread('nature.jpg', 1)
matrix = np.ones((5, 5), np.float32) / 25
new_img = cv2.filter2D(image, -1, matrix)
cv2.imshow('image', image)
cv2.imshow('newimg', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
