import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import time
cam= cv2.VideoCapture(0)
time.sleep(2)
ret,image=cam.read()

cv2.imwrite("/home/pi/background/opencv16.jpg",image)
cam.release()
