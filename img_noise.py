"""
Requires the install of opencv
$ pip install opencv-python
"""

import os
import cv2
from skimage.restoration import estimate_sigma


def img_noise(src):
    absolute_path = os.path.join(os.getcwd(), src)
    img = cv2.imread(absolute_path)
    if img is None:
        print("Unable to read src")
        return 0
    noise = estimate_sigma(img, multichannel=True, average_sigmas=True)
    return noise
