import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/home/aleix/Escritorio/dona_treballadora_101.jpg',0)


orb=cv2.ORB_create()
# Initiate STAR detector

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,None, flags=0)
plt.imshow(img2),plt.show()

