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

def get_square():
    global frame,Tls,Brs
    if Tls is not None and Brs is not None and dbarvo:
        cv.rectangle(frame, Tls, Brs, (0, 0, 255), 3)
    if not dbarvo:
        cv.rectangle(frame, (0,0),(0,0), (0, 0, 255), 3)


def zmanjsaj_sliko(slika, sirina, visina):
    return cv.resize(slika, (sirina, visina))

def doloci_barvo_koze(slika, levo_zgoraj, desno_spodaj) -> tuple:
    global dbarvo
    k = 1.5
    dbarvo = False
    x1, y1 = levo_zgoraj
    x2, y2 = desno_spodaj
    roi = slika[y1:y2, x1:x2]

    if roi.size == 0:
        return (0, 0, 0)
    
    mean_color = np.mean(roi,axis=(0,1))
    std_dev = np.std(roi,axis=(0,1))

    spodnja_meja = np.clip(mean_color - k * std_dev, 0, 255).astype(np.uint8)
    zgornja_meja = np.clip(mean_color + k * std_dev, 0, 255).astype(np.uint8)

    return spodnja_meja.reshape(1, 3), zgornja_meja.reshape(1, 3)

def obdelaj_sliko_s_skatlami(slika, sirina_skatle, visina_skatle,barva_koze) -> list:


def prestej_piksle_z_barvo_koze(slika, barva_koze) -> int:
