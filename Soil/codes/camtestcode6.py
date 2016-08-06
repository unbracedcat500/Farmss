import picam
import time

ii = picam.takePhotoWithDetails(640,480, 85) 

filename = "/home/pi/picam/picam-%s.jpg" % time.strftime("%Y_%m_%d-%H:%M:%S")

ii.save(filename)
