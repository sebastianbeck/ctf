#!/usr/bin/python
from PIL import Image

def rgb2hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)
def rgb2hexmod(b):
    return '{:02x}'.format(b)
img = Image.open('Flag5_1.png')  
pixels = img.convert('RGBA').load()
width, height = img.size
f = open("demofile01.txt", "a")
oldhexval='ffffff '
for x in range(width):
        r, g, b, a = pixels[x, 1]
        hexval= '%s' % (rgb2hexmod(b))
        if hexval!='ff' and hexval!=oldhexval:
            f.write(hexval)
            oldhexval = hexval
f.close


