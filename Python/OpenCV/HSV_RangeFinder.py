import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def nada():
    pass

cv2.namedWindow("result")

# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv2.createTrackbar('HMin', 'result', 0, 179, nada)
cv2.createTrackbar('SMin', 'result', 0, 255, nada)
cv2.createTrackbar('VMin', 'result', 0, 255, nada)
cv2.createTrackbar('HMax', 'result', 0, 179, nada)
cv2.createTrackbar('SMax', 'result', 0, 255, nada)
cv2.createTrackbar('VMax', 'result', 0, 255, nada)

# Set default value for Max HSV trackbars
cv2.setTrackbarPos('HMax', 'result', 179)
cv2.setTrackbarPos('SMax', 'result', 255)
cv2.setTrackbarPos('VMax', 'result', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0



while True:
    # Get current positions of all trackbars
    hMin = cv2.getTrackbarPos('HMin', 'result')
    sMin = cv2.getTrackbarPos('SMin', 'result')
    vMin = cv2.getTrackbarPos('VMin', 'result')
    hMax = cv2.getTrackbarPos('HMax', 'result')
    sMax = cv2.getTrackbarPos('SMax', 'result')
    vMax = cv2.getTrackbarPos('VMax', 'result')


    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    _, frame = cap.read()
  
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    
    # cv2.imshow('src', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
