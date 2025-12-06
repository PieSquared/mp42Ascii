import os
import sys

if os.name == "nt":
    if not sys.stdout.isatty():
        os.system(f'start cmd /k python "{os.path.abspath(__file__)}"')
        sys.exit()

import cv2
import time

VIDEO_PATH = "input.mp4"
WIDTH = 120
THRESHOLD = 120
FRAME_DELAY = 1/60


COLOR_0 = "\033[97m"
COLOR_1 = "\033[90m"
RESET = "\033[0m"

clear = "cls" if os.name == "nt" else "clear"

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print("Failed to open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height = int(gray.shape[0] * (WIDTH / gray.shape[1]) * 0.55)
    gray = cv2.resize(gray, (WIDTH, height))
    binary_frame = (gray > THRESHOLD).astype(int)

    os.system(clear)

    for row in binary_frame:
        line = ""
        for pixel in row:
            if pixel == 1:
                line += COLOR_1 + "1" + RESET
            else:
                line += COLOR_0 + "0" + RESET
        print(line)

    time.sleep(FRAME_DELAY)

cap.release()
