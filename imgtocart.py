import cv2
import numpy as np
#read image
img=cv2.imread("download.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
gary = cv2.medianBlur(gray,5)
#to show edges
edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

color=cv2.bilateralFilter(img, 9, 250, 250)
#to show cartoon

cartoon=cv2.bitwise_and(color,color,mask=edges)
cv2.imshow("img",img)
cv2.imshow("edges",edges)
cv2.imshow("cartoon",cartoon)
cv2.waitKey(0)
cv2.destroyWindow()
