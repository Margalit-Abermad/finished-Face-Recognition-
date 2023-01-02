import cv2
import face_recognition


cap = cv2.VideoCapture(0)

img=cv2.imread("images/Mark Tzukerberg.jpg")
rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_encoding=face_recognition.face_encodings(rgb_img)[0]


img2=cv2.imread("images/Elon Musk.jpg")
rgb_img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img_encoding2=face_recognition.face_encodings(rgb_img2)[0]

result=face_recognition.compare_faces([img_encoding],img_encoding2)
print("Result: ", result)

cv2.imshow("Img", img)
cv2.imshow("Img 2", img2)
cv2.waitKey(0)

