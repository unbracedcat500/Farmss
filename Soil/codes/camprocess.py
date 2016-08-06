import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO

def picture ():
    ramp_frames = 30 
    camera = cv2.VideoCapture(0)
    def get_image():
        retval, im = camera.read()
        return im 
    for i in xrange(ramp_frames):
        temp = camera.read()

    camera_capture = get_image()
    filename = "/home/pi/codes/opencv_mod.jpg"
    cv2.imwrite(filename,camera_capture)
    camera.release()



def process():
    load = cv2.imread('/home/pi/codes/opencv_mod.jpg',0)
    roi=load[160:240,290:380]
    total = np.sum(roi)
    avg = total/7200
    GV = int(avg)
    return GV

def phosphor():
    GV = process()
    print GV
    if GV > 120 and GV < 122:
        print "Nitrate Concentration is Zero"

    elif GV == 101:
        print "Nitrate Concentration is Ten"

    elif GV > 104 and GV < 106:
        print "Nitrate Concentration is Twenty Five"

    elif GV == 100:
        print "Nitrate Concentration is Fifty"

    elif GV > 80 and GV < 82:
        print "Nitrate Concentration is Hundred"

    elif GV > 58 and GV < 60:
        print "Nitrate Concentration is Two Hundred Fifty"

    elif GV > 46 and GV < 52:
        print "Nitrate Concentration is Five Hundred"
    else:
        print "nil"

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down = GPIO.PUD_UP)
def function(channel):
    picture()
    phosphor()
GPIO.add_event_detect(18,GPIO.FALLING,callback = function, bouncetime = 5000)
while 1:
    time.sleep(1)
