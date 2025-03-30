import cv2 as cv
import numpy as np
import time
from collections import Counter

frame = None
Tls = None
Brs = None
drawing = False
mouse_click = False
dbarvo = True
List_frame = []

def get_pixel_color(event, x, y, flags, param):
    global frame,Tls,Brs,drawing,mouse_click
    if event == cv.EVENT_LBUTTONDOWN:
        if frame is not None:
            drawing = True
            Tls = (x,y)
    if event == cv.EVENT_MOUSEMOVE:
        if frame is not None and drawing:
            Brs = (x,y)
    if event == cv.EVENT_LBUTTONUP:
        if frame is not None:
            drawing = False
            mouse_click = True
            Brs = (x,y)
    if mouse_click:
        cv.setMouseCallback("Video Stream", lambda *args: None)