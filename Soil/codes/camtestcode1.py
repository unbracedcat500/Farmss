import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import SimpleCV
import time
from SimpleCV import Camera
cam = Camera()
time.sleep(2)
img=cam.getImage()
img.save("simplecv_picam.png")

