import cv2
import time
import os
from pynput.keyboard import Key, Controller


def selfDestruct():
    scriptPath = os.path.abspath(__file__)

    os.remove(scriptPath)


def smallWindows():
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press(Key.home)
    keyboard.release(Key.home)
    keyboard.release(Key.cmd)


def playVideo():
    smallWindows()
    cap = cv2.VideoCapture("video.mp4")
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("video", frame)
            cv2.waitKey(1)
        else:
            selfDestruct()


while True:
    when = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if when == "2024-02-12 23:06:07":
        playVideo()
