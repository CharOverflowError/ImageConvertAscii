from skimage import io, img_as_float
from skimage.color import rgb2gray
from skimage.transform import rescale
import numpy as np
import math
from matplotlib import pyplot as plt

characters = """ .:-=+*#%@"""


img = io.imread("image.png")
img = rgb2gray(img)
height, width = img.shape
img = rescale(img, (400 / width))
height, width = img.shape
print(img.shape)

character_width = 4
character_height = 10

# Pad image
padded_image = np.ones((height + int((height / character_height) % character_height), width + int((width / character_width) % character_width)))
padded_image[:height, :width] = img
padded_height, padded_width = padded_image.shape

# Reshape image
new_width = int(padded_width / character_width)
new_height = int(padded_height / character_height)
reshaped_image = np.ones((new_height, new_width))

for y in range(new_height):
    for x in range(new_width):
        # print(y, x)
        block = padded_image[(y*character_height):(y*character_height)+character_height, (x*character_width):(x*character_width)+character_width]
        print(characters[int(round(min(np.mean(block), 0.9), 1) * 10)], end='')
    print()
