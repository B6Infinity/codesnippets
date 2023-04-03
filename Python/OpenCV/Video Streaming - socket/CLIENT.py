import cv2
import socket
import struct
import pickle

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 7878))

data = b''
PAYLOAD_SIZE = struct.calcsize('Q')

while True:
    while len(data) < PAYLOAD_SIZE:
        packet = client_socket.recv(1024)
        if not packet: break
        data += packet
    packed_msg_size = data[:PAYLOAD_SIZE]
    data = data[PAYLOAD_SIZE:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(1024)

    frame_data = data[:msg_size]
    data = data[msg_size:]

        
    frame = pickle.loads(frame_data)
    


    cv2.imshow('0', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
client_socket.close()
cv2.destroyAllWindows()
