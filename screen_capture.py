import pyautogui    # PyAutoGUI
import cv2          # opencv-python
import numpy as np  # numpy
import time
from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

i = 1
t1 = time.time()
while True:
    image = pyautogui.screenshot()
    image = np.array(image)
    h, w, c = image.shape
    h2 = 600
    w2 = int(h2 / h * w)
    image = cv2.resize(image, (w2, h2))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    res = model(image)[0].boxes
    for cls, xyxy in zip(res.cls, res.xyxy):
        x1, y1, x2, y2 = map(int, xyxy)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # if time.time() - t1 > 3.0:
    #     print("save a image. %d" % i)
    #     cv2.imwrite("data/img_%04d.jpg" % i, image)
    #     i = i + 1
    #     t1 = time.time()

    cv2.imshow("image", image)
    key_code = cv2.waitKey(1)
    if key_code in [27, ord('q')]:
        break
