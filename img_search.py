"""
requires installing image-search lib
$ pip install image-search
"""

import os


def get_img(query):
    img = os.system(f"image_search google {query} --limit 1")

    return img


image = get_img('cat')
print(image)