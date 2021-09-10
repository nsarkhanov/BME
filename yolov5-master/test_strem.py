import cv2

cap=cv2.VideoCapture("https://192.168.178.133:8080")

while True:
     succ, img=cap.read()
     resized=cv2.resize(img,(600,400))
     cv2.imshow('img',resized)

     key=cv2.waitKey(1)
     if key==ord('q'):
         break
cap.release()
cap.destroyAllWindows()
