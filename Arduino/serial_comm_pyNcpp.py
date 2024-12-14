# Intialise with a 2 sec delay (for the mahcine to heat up)
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
sleep(2)


# In Python:
ser.write('CAP'.encode())


# In CPP
'''
if (rcvdTxt == "CAP")
    {...}     
'''


# Output     
# for i in range(10):
#     line = ser.read()
#     print(f"Line ({line.isdigit()}):", line)

'''

Line (True): b'6'
Line (True): b'8'
Line (True): b'7'
Line (True): b'0'
Line (False): b'\r'
Line (False): b'\n'
Line (False): b'\xff'

'''
