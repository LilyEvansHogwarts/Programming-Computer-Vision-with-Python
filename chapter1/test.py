from imtools import *
from PIL import Image

im = Image.open('../data/empire.jpg').convert('L')
im.show()
im = array(im)

im2, cdf = histeq(im)

im3 = Image.fromarray(im2)
im3.show()




