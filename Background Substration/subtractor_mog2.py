
import cv2
import numpy as np

#cap = cv2.VideoCapture("highway.mp4")
cap = cv2.VideoCapture(0)

subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=10, detectShadows=True)

while True:
    _, frame = cap.read()

    mask = subtractor.apply(frame)

    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

print("Project End")

