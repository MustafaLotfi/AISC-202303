import cv2
import numpy as np
from ultralytics import YOLO


# Download the model from this github repo: https://github.com/ultralytics/ultralytics
# In the models sections. click on the YOLOv8x link.


lx1 = 220.
ly1 = 170.
lx2 = 400.
ly2 = 330.

m = (ly2-ly1)/(lx2-lx1)

b = -m * lx1 + ly1

model = YOLO("models/yolov8x")

for i in range(1, 7):
	img = cv2.imread(f"media/football/{i}.jpg")

	results = model.predict(source=img)

	for result in results:
		for (obj_xyxy, obj_cls) in zip(result.boxes.xyxy, result.boxes.cls):
			obj_cls = int(obj_cls)

			if obj_cls == 32:
				x1 = obj_xyxy[0].item()
				y1 = obj_xyxy[1].item()
				x2 = obj_xyxy[2].item()
				y2 = obj_xyxy[3].item()

				ball_x = (x2+x1)/2
				ball_y = (y2+y1)/2

				ball_r = ((x2-x1)/2+(y2-y1)/2)/2

				yhat = ball_x * m + b

				if yhat > ball_y:
					goal = False
				else:
					distance = abs(m*ball_x-ball_y+b)/(m**2+1)**0.5
					print(distance, ball_r)
					if distance > ball_r:
						goal = True
						break

				cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
		if goal:
			break

	cv2.imshow("Frames", img)

	cv2.waitKey(0)

	if goal:
		break

if goal:
	print("GOAAALL!")
cv2.destroyAllWindows()