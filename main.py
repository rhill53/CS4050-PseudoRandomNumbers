import img_noise as imn

max = input("Enter maximum random value: ")

noise = imn.img_noise('image.jpg')

rand = int(float(max) % noise)

print(rand)
