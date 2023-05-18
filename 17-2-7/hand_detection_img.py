import cv2
import mediapipe as mp


model = mp.solutions.hands.Hands(static_image_mode=True, min_detection_confidence=0.5,
	min_tracking_confidence=0.5)


# put an image address bellow
img = cv2.imread("files/selfie.jpg")

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