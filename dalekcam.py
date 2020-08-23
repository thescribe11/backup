import os

import cv2

import numpy as np

import pyfakewebcam
from dalekcam_modules import *
# setup access to the *real* webcam
cap = cv2.VideoCapture('/dev/video0')

height, width = 480, 640

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


# setup the fake camera

fake = pyfakewebcam.FakeWebcam('/dev/video20', width, height)
# frames forever

print("\n[*ALERT*] V4l2 webcam is now ACTIVE.\n")


while True:

    frame = get_frame(cap, None)

    # fake webcam expects RGB

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    fake.schedule_frame(frame)
