import cv2
import socket
import pickle
import struct
# import threading

HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_IP = '127.0.0.1'
PORT = 7878

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, PORT))
server_socket.listen(5)
print('Listening at:', HOST_IP, PORT)

# Look for at least one connection:
client_socket, addr = server_socket.accept()
print('Got connection from:', addr)

# Init Video Feed

cam = cv2.VideoCapture(0)
while True:
    
    _, frame = cam.read()


    # if client_socket:
    try:
        pd = pickle.dumps(frame)
        data_to_send = struct.pack("Q", len(pd))+pd
        client_socket.sendall(data_to_send)
        
    except:
        pass


    # CLOSE
    if cv2.waitKey(1) & 0xFF == ord('q'):
        client_socket.close()
        break
            
# cam.relase()
cv2.destroyAllWindows()

