"""
Requires the install of opencv
$ pip install opencv-python
"""

import cv2
from skimage.restoration import estimate_sigma


def img_noise(src):
    img = cv2.imread(src)
    return estimate_sigma(img, multichannel=True, average_sigmas=True)
