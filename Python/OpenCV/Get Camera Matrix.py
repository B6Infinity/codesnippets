'''All distances are to be in meters'''

import os
import numpy as np
import cv2
import json
import sys

SAVE = False
if '-s' in sys.argv or '--save' in sys.argv :
    SAVE = True
    print("Images will be saved")
elif '-o' in sys.argv or '--old' in sys.argv:
    print("Old images will be used")
    SAVE = None
    

with open('PARAMS.json') as f:
    PARAMS = json.load(f)

chessboardSize = tuple(PARAMS["CHESSBOARD_SIZE"])
frameSize = tuple(PARAMS["FRAME_SIZE"])
size_of_chessboard_squares = PARAMS["SIZE_OF_CHESSBOARD_SQUARES"]

print(chessboardSize, frameSize, size_of_chessboard_squares)
print(f"Chessboard edge length:  {chessboardSize[0] * size_of_chessboard_squares} x {chessboardSize[1] * size_of_chessboard_squares} meters")

print("Press 's' (with chessboard in frame) to save image coords")

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)


# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)

objp = objp * size_of_chessboard_squares

objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

cap = cv2.VideoCapture(0)
BACKEND_NAME = cap.getBackendName()
print(f"Using {BACKEND_NAME} backend")

IMAGE_COUNT = 0
if SAVE is None:
    IMAGE_COUNT = len([f for f in os.listdir('images') if f.endswith('.jpg')])
    print(f"Found {IMAGE_COUNT} images")

    for frame in os.listdir('images'):
        frame = cv2.imread(f'images/{frame}')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, chessboardSize, None)

        if ret == True:
            # Chessboard corners found
            corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)

            # Draw and display the corners
            cv2.drawChessboardCorners(frame, chessboardSize, corners2, ret)

            objpoints.append(objp)
            imgpoints.append(corners)
else:
    while True:
        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, chessboardSize, None)

        if ret == True:
            # Chessboard corners found
            corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)

            # Draw and display the corners
            cv2.drawChessboardCorners(frame, chessboardSize, corners2, ret)

            if cv2.waitKey(1) & 0xFF == ord('s'):
                IMAGE_COUNT += 1
                print(f"{IMAGE_COUNT} image coords saved")
                objpoints.append(objp)
                imgpoints.append(corners)
                cv2.imwrite(f'images/{IMAGE_COUNT}.jpg', frame)

        cv2.imshow('Cam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

if IMAGE_COUNT == 0:
    print("No images saved! Exiting...")
    exit()

print(f"Calibrating camera from {IMAGE_COUNT} images...")

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, frameSize, None, None)

if not ret:
    print("Failed to calibrate camera (idk why)! Exiting...")

# print("Camera matrix: \n", mtx)
# print("Distortion coefficients: ", dist)
# print("Translation vectors: ", tvecs)
# print("Rotation vectors: ", rvecs)

D = {
    'mtx': mtx.tolist(),
    'dist': dist.tolist(),
    'tvecs': [tvec.tolist() for tvec in tvecs],
    'rvecs': [rvec.tolist() for rvec in rvecs]
}

with open(f'{BACKEND_NAME}_calibration_data.json', 'w') as f:
    json.dump(D, f)

print(f"Calibration data saved to {BACKEND_NAME}_calibration_data.json")
