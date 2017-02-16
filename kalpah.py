import cv2
import numpy as np

t= cv2.imread("/home/toshika/Pictures/kalpah.png")
tcr = t [47.5:158.5, 76.5:176.5]

gray = cv2.cvtColor(tcr, cv2.COLOR_BGR2GRAY);
smoothedInput = cv2.GaussianBlur(gray, (1,1), 0);
edges = cv2.Canny(smoothedInput, 15, 50);
e=cv2.bitwise_not(edges)

b,g,r = cv2.split(tcr)
resultb=cv2.bitwise_and(b,b,mask=e)
resultg=cv2.bitwise_and(g,g,mask=e)
resultr=cv2.bitwise_and(r,r,mask=e)
result = cv2.merge((resultb,resultg,resultr))

kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(8,8))
d1=cv2.dilate(resultb,kernel,iterations=1)
d2=cv2.dilate(resultg,kernel,iterations=1)
d3=cv2.dilate(resultr,kernel,iterations=1)
d=cv2.merge((d1,d2,d3))

# show the images
cv2.imshow("Original", t)
cv2.imshow("ans", d)
cv2.waitKey(0)


