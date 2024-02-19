import cv2
import torch
from time import time
import numpy as np


weights_path = r"C:\Users\Zuhal\Downloads\yolov5n_212ep_64batch_dtsv10.pt"
model = torch.hub.load('ultralytics/yolov5', 'custom', weights_path, 'yolov5n')

confidence_threshold = 0.5
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'X264') # XVID algoritmasını tanımlama
kayit = cv2.VideoWriter(r'C:\Users\Zuhal\Downloads\kayit1.mp4',fourcc,10.0,(640,480))
# fourcc ile saniyede 20 resim alarak 640x480 boyutlarında bir avi dosyası


while True:
    # Get frames
    ret, frame = cap.read()
    start_time = time()

    results = model(frame) # Nesne tespiti sonuçlarını alın

    kayit.write(frame)  # video yazmayı başlatma

    car_indices = (results.pred[0][:, 5] == 0) #0 "araba" sınıfının indeksi
    car_scores = results.pred[0][car_indices, 4]  # Sınıfın skorları
    car_boxes = results.pred[0][car_indices, :4]

    for bbox, score in zip(car_boxes, car_scores):
        if score > confidence_threshold:
            x1, y1, x2, y2 = bbox
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (200, 0, 50), 3)
            text = f"car: {score:.2f}"
            cv2.putText(frame, text, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_PLAIN, 3, (200, 0, 50), 2)

    end_time = time()
    fps = 1 / np.round(end_time - start_time, 2)

    cv2.putText(frame, f"FPS: {round(fps, 2)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27: #esc için ASCII
        break

cap.release()
cv2.destroyAllWindows()