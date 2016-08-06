import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down = GPIO.PUD_UP)

def function(channel):
    print ("hello")
GPIO.add_event_detect(18,GPIO.FALLING,callback = function, bouncetime = 2000)
GPIO.cleanup()
