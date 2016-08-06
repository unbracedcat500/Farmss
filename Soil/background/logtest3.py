import RPi.GPIO as GPIO
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.IN,pull_up_down = GPIO.PUD_UP)
def photo(self):
    cam= cv2.VideoCapture(0)
    ret,image=cam.read()
    time.sleep(2)
    cv2.imwrite("/home/pi/background/opencv15.jpg",image)
    cam.release()
def three():
    photo()
GPIO.add_event_detect(13,GPIO.FALLING,callback=photo,bouncetime=5000)
while 1:
    time.sleep(1)
