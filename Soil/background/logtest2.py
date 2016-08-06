import RPi.GPIO as GPIO
import sys
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_UP)
def prin():
    f=file('/home/pi/background/output1.txt','a')
    sys.stdout = f
    print('back in hell')
    f.close()
def two(channel):
    prin()
GPIO.add_event_detect(19,GPIO.FALLING,callback=two,bouncetime=1000)
while 1:
    time.sleep(1)
