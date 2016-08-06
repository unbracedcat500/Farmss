import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
import matplotlib.pyplot as plt
load = cv2.imread('/home/pi/codes/opencv_mod.jpg',0)
roi=load[160:240,290:380]
total = np.sum(roi)
avg = total/7200
GV = int(avg)
print GV
