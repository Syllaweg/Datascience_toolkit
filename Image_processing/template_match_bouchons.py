"""Watch and add
https://www.pyimagesearch.com/2014/12/22/visual-logging-new-favorite-tool-debugging-opencv-python-apps/
https://www.pyimagesearch.com/2015/01/26/multi-scale-template-matching-using-python-opencv/
 """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

img_rgb = cv2.imread('data/pmz1.jpg')

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('data/panneau_droit.png',0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where(res >= threshold)


for p in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, p, (p[0] + w, p[1] + h), (0,255,255), 2)
    
cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
