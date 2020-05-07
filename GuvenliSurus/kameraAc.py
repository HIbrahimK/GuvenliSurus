#Bu dosya sadece bilgi amaçlıdır kullanımamaktadır

import cv2
import sys


def kamera():
        

    video_capture = cv2.VideoCapture(0)

    while True:
        # kare kare webcam den gelen görüntü yakalanıyor
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Sonuç ekranda gösteriliyor.
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # herşey tamamsa ekran yakalaması serbest bırakılıyor.
    video_capture.release()
    cv2.destroyAllWindows()



