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