import cv2
import numpy as np



kernel = np.array([[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]])

for i in range(1, 6):
	img = cv2.imread(f"media/volleyball/{i}.png")

	img = cv2.resize(img, (975, 485))

	print(img.shape)

	img_show = img.copy()

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	sharp = cv2.filter2D(gray, -1, kernel)

	circles = cv2.HoughCircles(sharp, cv2.HOUGH_GRADIENT, 1.5, 100, maxRadius=150)

	circle_max_y = 0
	ball_out = False
	if circles is not None:
		circles = circles[0].astype(np.uint32)

		for circle in circles:
			if circle[1] > circle_max_y:
				circle_max_y = circle[1]
				if (circle[0] + circle[2]) < 460:
					print(circle[1], circle_max_y)
					ball_out = True
			cv2.circle(img_show, (circle[0], circle[1]), circle[2], (0, 0, 255), 2)

	print(ball_out)
	cv2.imshow("Frames", img_show)

	cv2.waitKey(0)

cv2.destroyAllWindows()