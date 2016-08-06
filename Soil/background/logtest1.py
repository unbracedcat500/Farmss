import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN,pull_up_down = GPIO.PUD_UP)
#orig=sys.stdout

#f = open('output.txt', 'w')
def loggy():
    f=file('output.txt','a')
    sys.stdout=f
    print("hell")
    f.close()
def one(channel):
    loggy()
GPIO.add_event_detect(26,GPIO.FALLING,callback = one, bouncetime = 1000)
#sys.stdout=orig

while 1:
    time.sleep(1)
#GPIO.cleanup()
