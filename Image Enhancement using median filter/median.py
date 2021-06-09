import cv2
Img=cv2.imread('2.jpg');
cv2.imwrite('334.jpg',Img);
cv2.imshow('334.jpg',Img);

Img=cv2.imread('2.jpg');
cv2.imshow('original image',Img);
gray=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY);
cv2.imshow('gray',gray);


img=cv2.imread('2.jpg');
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Family',(10,500), font,2,(255,0,1),2,cv2.LINE_AA)

cv2.imshow('Image Text Water Marked',img);
