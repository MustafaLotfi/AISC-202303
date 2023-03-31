import cv2
import numpy as np


detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	if ret:
		frame = cv2.flip(frame, 1)

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		results = detector.detectMultiScale(gray)

		for (x, y, w, h) in results:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
			
		cv2.imshow("Webcam", frame)

		q = cv2.waitKey(1)
		if q == ord('q'):
			break
	else:
		break


cap.release()
cv2.destroyAllWindows()