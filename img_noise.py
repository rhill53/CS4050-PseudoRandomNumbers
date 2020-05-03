"""
Requires the install of opencv
$ pip install opencv-python
"""

import os
import cv2
import numpy
from skimage.restoration import estimate_sigma


def img_noise(src):
    absolute_path = os.path.join(os.getcwd(), src)
    img = cv2.imread(absolute_path)
    if img is None:
        print("Unable to read src")
        img_noise(src)
    noise = estimate_sigma(img, multichannel=True, average_sigmas=True)
    return noise


def img_average(src):
    absolute_path = os.path.join(os.getcwd(), src)
    img = cv2.imread(absolute_path)
    if img is None:
        print("Unable to read src")
        return 0
    avg_color_per_row = numpy.average(img, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    avg = (avg_color[0] + avg_color[1] + avg_color[2])/3
    return avg
