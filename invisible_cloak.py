import cv2
import numpy as np

cap = cv2.VideoCapture(0)
url = "https://192.168.0.101:8080/video"
cap.open(url)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame = cap.read()

    if ret:

        # Converting rgb to hsv

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # cv2.imshow("hsv", hsv)

        # Getting hsv value

        red = np.uint8([[[0,0,255]]])
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

        # get hsv value of red from BGR

        #Threshold the hsv value to get only red colors

        l_red = np.array([0, 100, 100])
        u_red = np.array([10, 255, 255])

        mask = cv2. inRange(hsv, l_red, u_red)

        # all things red
        part1 = cv2.bitwise_and(back, back, mask = mask)

        mask = cv2.bitwise_not(mask)

        # all things not red
        part2 = cv2.bitwise_and(frame, frame, mask = mask)

        cv2.imshow("cloak", part1 + part2)


        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()