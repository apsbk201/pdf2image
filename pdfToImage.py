#!/usr/bin/python3

from sys import argv
from pdf2image import convert_from_path

pdf = argv[1]
images = convert_from_path(pdf)

for i in range(len(images)):
    images[i].save(str(pdf)+ '_page_'+ str(i) +'.jpg', 'JPEG')


