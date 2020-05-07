import cv2
import sys

def yuzTanimlama(capture):
    faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    video_capture = capture

    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        #cv2.CASCADE_SCALE_IMAGE
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Tanımalanan yüzün etrafında yeşil bir kare oluşturuluyor
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Sonuç ekranda gösteriliyor.
    return frame
       
