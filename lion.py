import cv2
import numpy as np

img =cv2.imread("lion.png" , 0)
result = np.zeros(img.shape,np.float32)

mask = np.array([[0 , -1, 0],
                [-1 , 4, -1],
                [0 , -1 , 0]])

row,col = img.shape

for i in range (1 , row -1):
    for j in range(1 , col -1):
        new_img = img[i-1:i+2,j-1:j+2]
        result[i,j]= np.sum(new_img*mask)


cv2.imwrite("lion1.jpg" , result)
cv2.waitKey()