import cv2
import numpy as np
import os
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
# Playing video from file:
cap = cv2.cv2.VideoCapture("b1_export_gray.avi")
                    

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    a=[]
    a.append(name)
    
    # To stop duplicate images
    currentFrame += 1
    if currentFrame==873:
        break


   
        

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
