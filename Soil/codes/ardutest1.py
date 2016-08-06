import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(1)
ser.write("hello")
#while True:
	#data = ser.readline()
	#if data:
	#	print data.rstrip('\n') #strip out the new lines for now
		# (better to do .read() in the long run for this reason
