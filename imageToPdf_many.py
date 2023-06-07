#!/usr/bin/python3

from sys import argv
from PIL import Image

many = argv[1]
many = int(many)
im = []
try:
    for i in range(many):
        #a = i -1
        #im[i] = argv[i+2]
        if i == 0:
            #im_1 = argv[i+2]
            im_1 = argv[i+2]
            img_1= Image.open(im_1)
            image_1 = img_1.convert('RGB')
            #print(im_1)
    
        else:
            ii = argv[i+2]
            ii = Image.open(ii)
            iig = ii.convert('RGB')
            im.insert(i,iig)
            #print(im[i-1])
    image_1.save('imageToPdf_many.pdf', save_all=True,append_images=im)
    print("Done")

except:
    print("Like This (./imageToPdf_many.py 3 img1 img2 im3)")
