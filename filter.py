import cv2
import numpy as np

#Sharpen Filter
array = [
    [3.14,0,3.14],
    [1,0,1],
    [3.14,0,3.14]
]

image = cv2.imread('Image Source')
sharpen_kernel = np.array(array)
sharpen = cv2.filter2D(image, -1, sharpen_kernel)

cv2.imshow('Sharpen Filter Of Dark Image : ', sharpen)
cv2.waitKey()
