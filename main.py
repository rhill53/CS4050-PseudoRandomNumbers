import img_noise as imn
import rand_img as rand_img
import matplotlib.pyplot as plt
import random

py_rand_nums = []
rand_nums = []
i = 0
min = 0
max = 1000
while i < 1000:
    rand_img.get_rndm_image()

    noise = imn.img_noise('image.jpg')
    avg = imn.img_average('image.jpg')

    noise = int(noise * avg * max)

    rand = (noise % (max - min)) + min

    rand_nums.append(rand)

    i += 1

plt.hist(rand_nums, bins=1000)
plt.show()


i = 0
while i < 1000:
    x = random.randint(min, max)
    py_rand_nums.append(x)
    i += 1

plt.hist(py_rand_nums, bins=1000)
plt.show()
