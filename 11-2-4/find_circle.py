import cv2
import numpy as np

# Loading image
img = cv2.imread("media/circle.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (3, 3), 0)

edges = cv2.Canny(blur, 100, 200)

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.5, 100)

if circles is not None:
	circles = circles[0].astype(np.uint32)

	for circle in circles:
		cv2.circle(img, (circle[0], circle[1]), circle[2], (0, 0, 255), 2)

# Displaying image

resize = cv2.resize(img, None, fx=0.5, fy=0.5)

cv2.imshow("Image", resize)
# cv2.imshow("Gray", gray)

cv2.waitKey(0)

cv2.destroyAllWindows()