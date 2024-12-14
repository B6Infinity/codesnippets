import serial
from time import sleep
import cv2
import numpy as np

# Configuration
SERIAL_PORT = '/dev/ttyUSB0'  # Change to your serial port (e.g., 'COM3' on Windows)
BAUD_RATE = 115200            # Must match the ESP32 Serial.begin() rate
OUTPUT_FILE = 'captured_image.jpg'  # File to save the image data

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
sleep(2)


def read_frame():
    ser.write('CAP'.encode())


    print("Sent CAP command.")
    print("Waiting for image size...")
    

    size = b""
    while True:
        line = ser.read()
        print(f"Line ({line.isdigit()}):", line)
        size += line
        if line == b'\n': break
    
    size = size.decode().strip()
    image_size = int(size)

    print(f"Image size: {image_size} bytes")
    
    
    print("Recieving image data...")
    image_data = bytearray()
    while len(image_data) < image_size:
        if ser.in_waiting > 0:
            chunk = ser.read(ser.in_waiting)
            image_data.extend(chunk)

    # print("Image data revcieved!")
    # print(image_data)

    return image_data

    # with open(OUTPUT_FILE, 'wb') as f:
        # f.write(image_data)
    # print(f"Image saved to {OUTPUT_FILE}")



ser.close()
