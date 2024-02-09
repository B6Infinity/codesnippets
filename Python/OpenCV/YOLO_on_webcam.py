print("Importing YOLO from ultralytics...")
from ultralytics import YOLO

import cv2

model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training) 
cap = cv2.VideoCapture(0)

print("Predicting...")

while True:
    _, frame = cap.read()
    
    results = model(frame)[0]
    frame = results.plot()
    cv2.imshow('w', frame)

    for box in results.boxes:

        # Extracting the values from the box
        detected_class = results.names[int(box.cls)]
        box.conf[0].numpy()
        x1, y1, x2, y2 = [int(x) for x in box.data.numpy()[0][:4]]
        
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        cv2.putText(frame, detected_class, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    
    cv2.imshow('cus', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
