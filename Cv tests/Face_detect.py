import numpy as np
import cv2
import math
#face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface_improved.xml')
face_cascade = cv2.CascadeClassifier('C:/Users/hariharan.mohanarang/Desktop/Cv tests/Cascades/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)

def diag( w,h):
    return int(math.sqrt(w**2 + h**2))


while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    face_track = []
    face_diag = []
    face_list = []
    # print(type(faces))
    for (x,y,w,h) in faces:
        face_list = faces.tolist()
        print("face_list", face_list)
        # print(type(faces))
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # print("idex : ",faces.

        diagonal_length = math.sqrt(w**2 + h**2)
        # print(diagonal_length)
        if diagonal_length > 280:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        #print(face_area)
        if len(faces) >= 1:
            index = 0
            for i in faces:
                x,y,w,h = i

                temp_list = list()
                temp_list.append(index)
                temp_list.append(diag(w, h))
                face_track.append(temp_list)
                index += 1
                print(f"{face_track} is the length")
            print(face_track)

            for elem in face_track:
                face_diag.append(elem[1])
            k = max(face_diag)
            faceIndex =face_diag.index(k)
            x1,y1,w1,h1 = face_list[faceIndex]

            crop = img[y1-60: y1 + h1+40,x1-60: w1 +x1+40]
            cv2.imwrite('face.jpg', crop)

            face_track.clear()

            #main_face = face_diag.index(max(face_diag))
            #print(main_face)

            



        
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
