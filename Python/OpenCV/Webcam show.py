import cv2
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('w', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
