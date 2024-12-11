import pyautogui
import cv2
import numpy as np
import time
from ultralytics import YOLO
import os
import ai

model = YOLO("runs/detect/train/weights/best.pt")

wait_time = 3
ws = 600
nums = {}
for filename in os.listdir("numbers"):
    path = os.path.join("numbers", filename)
    num = cv2.imread(path)
    num = cv2.resize(num, (ws // 4, ws // 4))
    num = cv2.cvtColor(num, cv2.COLOR_BGR2HSV)
    nums[int(filename.split(".")[0])] = num

ii = 0
s_time = time.time()
while True:
    image = pyautogui.screenshot()
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    h, w, c = image.shape
    image = cv2.resize(image, (w // 5, h // 5))

    boxes = model(image)[0].boxes
    t = None
    for conf, cls, xyxy in zip(boxes.conf, boxes.cls, boxes.xyxy):
        if conf < 0.8: continue
        if int(cls) != 0: continue
        x1, y1, x2, y2 = map(int, xyxy)
        if t is None or (t[2] - t[0]) * (t[3] - t[1]) < (x2 - x1) * (y2 - y1):
            t = [x1, y1, x2, y2]

    img = np.zeros((ws, ws, 3), np.int8)
    board = np.zeros((4, 4), np.int32)
    if t is not None:
        # cv2.rectangle(image, (t[0], t[1]), (t[2], t[3]), (0, 255, 0), 2)
        img = cv2.resize(image[t[1]:t[3], t[0]:t[2], :], (ws, ws))

        o = ws // 4
        for i in range(4):
            for j in range(4):
                g = img[o*i:o*i+o, o*j:o*j+o, :]
                g = cv2.cvtColor(g, cv2.COLOR_BGR2HSV)

                p, e = 0, o * o * 3 * 255
                for k, num in nums.items():
                    mse = np.sum((num - g) ** 2)
                    if mse < e:
                        p, e = k, mse

                board[i][j] = p
                # cv2.imshow("g_%d_%d" % (i, j), g)
                cv2.rectangle(
                    img,
                    (o*j, o*i), (o*j+o, o*i+o),
                    (200, 255, 200), 1
                )
                cv2.putText(
                    img, str(p),
                    (o * j + o // 2, o * i + o // 2),
                    cv2.FONT_HERSHEY_PLAIN,
                    2.5, (200, 255, 200), 20, cv2.LINE_AA
                )
                cv2.putText(
                    img, str(p),
                    (o*j+o//2, o*i+o//2),
                    cv2.FONT_HERSHEY_PLAIN,
                    2.5, (0, 0, 255), 4, cv2.LINE_AA
                )
        print(time.time() - s_time)
        if time.time() - s_time > wait_time:
            # cv2.imwrite("Game2028_dataset/data/img_%d.jpg" % ii, image)
            # ii += 1
            # pyautogui.click((t[0] + t[2]) // 2 * 5, (t[1] + t[3]) // 2 * 5)
            x, y = pyautogui.position()
            if t[2] > x // 5 > t[0] and t[3] > y // 5 > t[1]:
                # c = ["left", "down", "up", "right"]
                # pyautogui.keyDown(np.random.choice(c))
                res = ai.play(board)
                pyautogui.keyDown(res)
                s_time = time.time()
    # print(board)

    cv2.imshow("img", img)
    key_code = cv2.waitKey(1)
    if key_code in [27, ord('q')]:
        break
