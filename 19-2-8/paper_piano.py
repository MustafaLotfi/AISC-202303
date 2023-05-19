import mediapipe as mp
import numpy as np
import cv2
from vlc import MediaPlayer


cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)


model0 = mp.solutions.hands.Hands(static_image_mode=False, min_detection_confidence=0.5,
	min_tracking_confidence=0.5)
model1 = mp.solutions.hands.Hands(static_image_mode=False, min_detection_confidence=0.5,
	min_tracking_confidence=0.5)

musics = [MediaPlayer('files/0.mp3'), MediaPlayer('files/1.mp3'), MediaPlayer('files/2.mp3')]
frame_size = 640, 480
i = 0
while True:
	ret0, frame0 = cap0.read()
	ret1, frame1 = cap1.read()


	if ret0 and ret1:
		frame0 = cv2.flip(frame0, 1)

		frame0 = cv2.resize(frame0, frame_size)
		frame1 = cv2.resize(frame1, frame_size)

		rgb0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2RGB)
		rgb1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)

		lms0 = model0.process(rgb0).multi_hand_landmarks
		landmarks0 = []
		touched = False
		if lms0:
			for lm in lms0:
				for point in lm.landmark:
					landmarks0.append([point.x, point.y])

			landmarks0 = np.array(landmarks0)

			if landmarks0[12, 1] > 0.6:
				touched = True

			for lm0 in landmarks0:
				if (lm0 >= 0).all() and (lm0 <= 1).all():
					cv2.circle(frame0, (lm0 * frame_size).astype(np.uint32), 2, (0, 0, 255), cv2.FILLED)

		lms1 = model1.process(rgb1).multi_hand_landmarks
		landmarks1 = []
		keys = [False] * 3
		if lms1:
			for lm in lms1:
				for point in lm.landmark:
					landmarks1.append([point.x, point.y])

			landmarks1 = np.array(landmarks1)

			if landmarks1[12, 0] < 0.33:
				keys[0] = True
			elif landmarks1[12, 0] < 0.66:
				keys[1] = True
			else:
				keys[2] = True

			for lm0 in landmarks1:
				if (lm0 >= 0).all() and (lm0 <= 1).all():
					cv2.circle(frame1, (lm0 * frame_size).astype(np.uint32), 2, (0, 0, 255), cv2.FILLED)


		if touched:
			if keys[0]:
				musics[0].play()
				musics[1].stop()
				musics[2].stop()

			elif keys[1]:
				musics[0].stop()
				musics[1].play()
				musics[2].stop()
			else:
				musics[0].stop()
				musics[1].stop()
				musics[2].play()
				
		frame = np.concatenate([frame0, frame1], axis=1)
		cv2.imshow("Webcam", frame)

		q = cv2.waitKey(1)
		if (q == ord('q')) or (q == ord('Q')):
			break

		i += 1

cap0.release()
cap1.release()
cv2.destroyWindow("Webcam")