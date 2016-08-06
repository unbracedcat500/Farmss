import serial
import time
ser = serial.Serial('/dev/rfcomm0')
ser.write("hi wassup?")
