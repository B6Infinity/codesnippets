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
