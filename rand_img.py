"""
Utilizes free random image generator at picsum.photos
"""

import requests
import shutil


def get_rndm_image():
    image_url = 'https://picsum.photos/200'
    resp = requests.get(image_url, stream=True)
    local_file = open('image.jpg', 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    del resp
