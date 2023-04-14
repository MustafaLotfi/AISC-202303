import cv2
import numpy as np


kernel_sharp = np.array([[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]])

ball_ys = []
in_out = []

for i in range(1, 6):
	img = cv2.imread(f"media/volleyball/{i}.png")

	img = cv2.resize(img, (975, 485))

	img_show = img.copy()

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	sharp = cv2.filter2D(gray, -1, kernel_sharp)

	circles = cv2.HoughCircles(sharp, cv2.HOUGH_GRADIENT, 1.5, 100, maxRadius=150)

	if circles is not None:
		circles = circles[0].astype(np.uint32)

		for circle in circles:
			ball_ys.append(circle[1])

			if (circle[0] + circle[2]) < 460:
				in_out.append("out")
			else:
				in_out.append("in")
				
			cv2.circle(img_show, (circle[0], circle[1]), circle[2], (0, 0, 255), 2)

	cv2.imshow("Frames", img_show)

	cv2.waitKey(0)

print(ball_ys)
print(in_out)

y_max_ind = np.argmax(ball_ys)
print(in_out[y_max_ind])

cv2.destroyAllWindows()