import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

while True:
    _, face_detect = capture.read()
    gray_scale = cv2.cvtColor(face_detect, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_scale, 1.2, 8)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(face_detect,(x,y), (x+y,y+h), (250, 0, 0), 3)
    cv2.imshow('face_detector',face_detect)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

capture.release()
    