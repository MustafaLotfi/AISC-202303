import mediapipe as mp
import numpy as np
import cv2


cap = cv2.VideoCapture(0)

model = mp.solutions.hands.Hands(static_image_mode=False, min_detection_confidence=0.5,
	min_tracking_confidence=0.5)

frame_size = 640, 480

prev_lm = None
while True:
	ret, frame = cap.read()

	if ret:
		frame = cv2.flip(frame, 1)
		frame = cv2.resize(frame, frame_size)

		rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		lms = model.process(rgb).multi_hand_landmarks
		landmarks = []
		if lms:
			for lm in lms:
				for point in lm.landmark:
					landmarks.append([point.x, point.y])

			landmarks = np.array(landmarks)

			lm_vel = None
			if prev_lm is not None:
				lm_vel = landmarks[12, 0] - prev_lm

			prev_lm = landmarks[12, 0]

			if lm_vel is not None and lm_vel > 0.4:
				print("High speed")

			for lm0 in landmarks:
				if (lm0 >= 0).all() and (lm0 <= 1).all():
					cv2.circle(frame, (lm0 * frame_size).astype(np.uint32), 2, (0, 0, 255), cv2.FILLED)



		cv2.imshow("Webcam", frame)

		q = cv2.waitKey(1)
		if (q == ord('q')) or (q == ord('Q')):
			break

cap.release()
cv2.destroyWindow("Webcam")