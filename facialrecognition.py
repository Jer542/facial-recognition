import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
 
cap = cv2.VideoCapture(0)
last_face = None

while True:

    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        last_face = img[y:y+h, x:x+w]

    cv2.imshow('img', img)

    if last_face is not None:
        cv2.imshow('Last face', last_face)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()