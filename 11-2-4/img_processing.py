import cv2
import numpy as np

# Loading image
img = cv2.imread("media/It's a Wonderful Life.jpg")


# Implementations
# print(img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = gray.shape

kernel_size = 3

# Moving Average
# kernel = np.ones((kernel_size, kernel_size))

# Sobel
kernel = np.array([[0, -1, 0],
	[-1, 5, 0],
	[0, -1, 0]])

# blur = np.zeros((h-kernel_size, w-kernel_size))

# for i in range(h-kernel_size):
# 	for j in range(w-kernel_size):
# 		img_little = gray[i:i+kernel_size, j:j+kernel_size]

# 		little_float = np.float32(img_little)

# 		blur[i, j] = (little_float * kernel).mean()


# blur = blur.astype(np.uint8)


blur = cv2.GaussianBlur(gray, (3, 3), 0)

sharp = cv2.filter2D(gray, -1, kernel)

edges = cv2.Canny(gray, 100, 200)


# Displaying image
cv2.imshow("Image", sharp)
# cv2.imshow("Gray", gray)

cv2.waitKey(0)

cv2.destroyAllWindows()