import cv2
import numpy as np
from ultralytics import YOLO

# Download the model from this github repo: https://github.com/ultralytics/ultralytics
# In the models sections. click on the YOLOv8x link.

model = YOLO("models/yolov8x")

model.predict(source=img, show=True)

cv2.waitKey(0)