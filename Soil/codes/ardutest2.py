import serial
ser = serial.Serial('/dev/rfcomm0')
ser.write('100')
