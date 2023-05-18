import cv2
import mediapipe as mp


model = mp.solutions.pose.Pose(static_image_mode=False, min_detection_confidence=0.5,
	min_tracking_confidence=0.5)


# put a video or number 0 bellow (to use webcam)
cap = cv2.VideoCapture("files/Football.mp4")

while True:
	ret, frame = cap.read()

	if ret:
		width, height = frame.shape[1], frame.shape[0]
		frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		lm = model.process(frame_rgb).pose_landmarks
		if lm:
			for point in lm.landmark:
				lm0 = point.x, point.y
				cv2.circle(frame, (int(lm0[0]*width), int(lm0[1]*height)), 3, (255, 255, 255), cv2.FILLED)
			
		cv2.imshow("Video", frame)
		q = cv2.waitKey(1)

		if q == ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyWindow("Video")

quit()

width, height = img.shape[1], img.shape[0]

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

lms = model.process(img_rgb).multi_hand_landmarks

if lms:
	for lm in lms:
		for point in lm.landmark:
			lm0 = point.x, point.y
			cv2.circle(img, (int(lm0[0]*width), int(lm0[1]*height)), 5, (0, 0, 255), cv2.FILLED)
		# lm0 = lm.landmark[0].x, lm.landmark[0].y
		# print((lm0[0]*width, lm0[1]*height))
		# cv2.circle(img, (int(lm0[0]*width), int(lm0[1]*height)), 5, (0, 0, 255), cv2.FILLED)
cv2.imshow("Image", img)

cv2.waitKey(0)

cv2.destroyWindow("Image")