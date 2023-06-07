#!/usr/bin/python3

from PIL import Image
from sys import argv

image = argv[1]

image_1 = Image.open(image)
im_1 = image_1.convert('RGB')
im_1.save(str(image)+'.pdf')

