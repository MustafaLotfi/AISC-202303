import cv2
import mediapipe as mp


model = mp.solutions.hands.Hands(static_image_mode=False,
	min_detection_confidence=0.5,
	min_tracking_confidence=0.5)


cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	if ret:
		width, height = frame.shape[1], frame.shape[0]
		frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		lms = model.process(frame_rgb).multi_hand_landmarks
		if lms:
			for lm in lms:
				lm0 = lm.landmark[0].x, lm.landmark[0].y

				if lm0[0] < 0.33:
					print(1)
				elif 0.33 <= lm0[0] < 0.66:
					print(2)
				else:
					print(3)
				# for point in lm.landmark:
				# 	lm0 = point.x, point.y
				# 	cv2.circle(frame, (int(lm0[0]*width), int(lm0[1]*height)), 3, (0, 0, 255), cv2.FILLED)
			
		cv2.imshow("Video", frame)
		q = cv2.waitKey(1)

		if q == ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyWindow("Video")
