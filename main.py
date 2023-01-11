import cv2
from simple_facerec import SimpleFacerec

# 2 problems to corect, 1.its take too mutch time to incoding all datdbase images, 2. doesent differentiate between identical twins!! :(
# Encode faces from a folder
sfr= SimpleFacerec()
sfr.load_encoding_images("images3/")

# load camera
cap= cv2.VideoCapture(0)


while True:
    ret, frame= cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        print(face_loc)
        top, right, bottom, left= face_loc[0],face_loc[1],face_loc[2],face_loc[3]

        # add text name above the rectangle
        cv2.putText(frame,name,(left,top -10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,200),2)

        # create the rectangle on the face
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,200),2) #(0,0,200)->color of rectangle, 2=pixels

    cv2.imshow("Frame",frame)

    key= cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()