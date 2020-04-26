import random


def get_word():
    filename = "words.txt"

    with open(filename) as f:
        lines = f.readlines()

    rndm = random.randint(0, len(lines))

    return lines[rndm]
