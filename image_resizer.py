import cv2

img = cv2.imread("360_F_615496890_W34yB8VDE6n5pehb5QCt1ek5oEvRo9qA.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("title",img)

width = 500
height = 500

output = cv2.resize(img ,(width,height))
cv2.imwrite("img1.jpg",output)
cv2.waitKey(0)