import cv2
import numpy as np
import matplotlib.pyplot as plt


## Loading image
img = cv2.imread("media/It's a Wonderful Life.jpg")

print(f"Main image shape: {img.shape}")

h, w = img.shape[:2]

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# plt.imshow(img_rgb)
# plt.title("Image (RGB)")
# plt.show()


###### Implementations #######
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# plt.imshow(gray, cmap="gray")
# plt.title("Image (gray)")
# plt.show()


# Blur (Manual)
kernel_size = 10
kernel_blur = np.ones((kernel_size, kernel_size))

blur_mnl = np.zeros((h-kernel_size, w-kernel_size))

# for i in range(h-kernel_size):
# 	for j in range(w-kernel_size):
# 		img_little = np.float32(gray[i:i+kernel_size, j:j+kernel_size])

# 		blur_mnl[i, j] = (img_little * kernel_blur).mean()

# blur_mnl = blur_mnl.astype(np.uint8)
# print(f"Blurred image shape: {blur_mnl.shape}")

# plt.imshow(blur_mnl, cmap="gray")
# plt.title("Blurred Image (Manual)")
# plt.show()


# Blur
blur_gray = cv2.GaussianBlur(gray, (13, 13), 0)

# print(blur_gray.shape)
# plt.imshow(blur_gray, cmap="gray")
# plt.title("Blurred image (gray)")
# plt.show()

blur = cv2.GaussianBlur(img, (13, 13), 0)
blur_rgb = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)

# plt.imshow(blur_rgb)
# plt.title("Blurred image")
# plt.show()


## Sobel
kernel_sobel_x = np.array([[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]])
sobel_x = cv2.filter2D(gray, -1, kernel_sobel_x)

kernel_sobel_y = np.array([[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]])
sobel_y = cv2.filter2D(gray, -1, kernel_sobel_y)

sobel = np.sqrt(np.float32(sobel_x)**2 + np.float32(sobel_y)**2).astype(np.uint8)


# plt.imshow(sobel_x, cmap="gray")
# plt.title("Sobel x")
# plt.show()
# plt.imshow(sobel_y, cmap="gray")
# plt.title("Sobel y")
# plt.show()
# plt.imshow(sobel, cmap="gray")
# plt.title("Sobel")
# plt.show()


## Sharp
kernel_sharp = np.array([[0, -1, 0],
	[-1, 5, 0],
	[0, -1, 0]])

sharp = cv2.filter2D(img, -1, kernel_sharp)
sharp_rgb = cv2.cvtColor(sharp, cv2.COLOR_BGR2RGB)

# plt.imshow(sharp_rgb)
# plt.title("Shapr image (RGB)")
# plt.show()

## Canny
edges = cv2.Canny(gray, 200, 300)

print(edges.shape)
plt.imshow(edges, cmap="gray")
plt.title("Edges (canny)")
plt.show()