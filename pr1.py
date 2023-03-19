import cv2
import numpy as np
import time


t0 = time.time()

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

while True:
	ret, frame = cap.read()

	if ret:
		t1 = time.time() - t0

		frame = cv2.flip(frame, 1)

		t1_str = str(round(t1, 2))

		cv2.putText(frame, t1_str, (100, 100), cv2.FONT_HERSHEY_SIMPLEX,
			1, (0, 0, 255), 1)

		# frame = 255 - frame
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		cv2.imshow("Webcamasdfasdf", frame)

		q = cv2.waitKey(1)

		if q == ord('q'):
			break

cv2.destroyAllWindows()
cap.release()