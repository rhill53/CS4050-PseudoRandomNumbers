import random_word as rw
import random_img as ri
import img_noise as imn

key = rw.get_word()

temp = ri.download_images(key)

noise = imn.img_noise(temp)

print(noise)
