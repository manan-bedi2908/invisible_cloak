import cv2
import numpy as np

cap = cv2.VideoCapture(0)
url = "https://192.168.0.101:8080/video"
cap.open(url)

while cap.isOpened():
    ret, back = cap.read()       # Reading from the Webcam

    if ret:
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):
            # save the image
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()