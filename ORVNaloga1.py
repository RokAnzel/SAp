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
    visina, sirina, _ = slika.shape
    stev_skat_sr = visina // visina_skatle
    stev_skat_vs = sirina // sirina_skatle
    list_frame = []
    for i in range(stev_skat_sr):
        list_frame2 = []
        for j in range(stev_skat_vs):
            list_frame3 = []
            x1, y1 = j * sirina_skatle, i * visina_skatle
            x2, y2 = x1 + sirina_skatle, y1 + visina_skatle
            roi = slika[y1:y2, x1:x2]
            list_frame3.append(roi)
            list_frame3.append(prestej_piksle_z_barvo_koze(roi,barva_koze))
            if list_frame3[1] == 1 and not dbarvo:
                cv.rectangle(slika, (x1, y1), (x2, y2), (0, 0, 255), 1)
            list_frame2.append(list_frame3)
        list_frame.append(list_frame2)
    return list_frame

def prestej_piksle_z_barvo_koze(slika, barva_koze) -> int:

    spodnja_meja, zgornja_meja = barva_koze

    mask = cv.inRange(slika, spodnja_meja, zgornja_meja)

    stevilo_ujetih_pikslov = np.count_nonzero(mask)

    skupno_stevilo_pikslov = slika.shape[0] * slika.shape[1]

    if (stevilo_ujetih_pikslov / skupno_stevilo_pikslov) >= 0.5:
        return 1
    else:
        return 0 
    

if __name__ == '__main__':
    kamera = cv.VideoCapture(0)
    cv.namedWindow("Video Stream")
    cv.setMouseCallback("Video Stream", get_pixel_color)
    barvo_koze=(np.array([0, 0, 0]), np.array([255, 255, 255]))
    prev_time = time.time()

    if not kamera.isOpened():
        print('Kamera ni bila odprta.')
    else:
        while True:
            ret, frame = kamera.read() 
            if not ret:
                break

            frame = cv.flip(frame, 1) 
            frame = zmanjsaj_sliko(frame, 300, 260)
            if dbarvo and mouse_click:
                barvo_koze = doloci_barvo_koze(frame,Tls,Brs)
            
            List_frame = obdelaj_sliko_s_skatlami(frame,40,5,barvo_koze)

            curr_time = time.time()
            fps = 1 / (curr_time - prev_time)
            prev_time = curr_time

            cv.putText(frame, f"FPS: {int(fps)}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            cv.imshow("Video Stream", frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        kamera.release()
        cv.destroyAllWindows()