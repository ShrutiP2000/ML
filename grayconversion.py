import cv2

Img=cv2.imread('1.jpeg');
cv2.imshow('original image',Img);
gray=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY);
cv2.imshow('gray',gray);

cv2.waitKey(0)
cv2.destroyAllWindows()
