import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import pygame
import pygame.camera
import time
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
#time.sleep(2)
img=cam.get_image()
pygame.image.save(img,"pygame.jpg")
cam.stop()
    
