import cv2

img=cv2.imread('1.jpeg');
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Amay',(10,500), font,2,(255,0,1),2,cv2.LINE_AA)

cv2.imshow('Image Text Water Marked',img);
