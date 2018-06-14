from PIL import Image
from numpy import *
from pylab import *

input_path = '../data/'
output_path = './data/'

im = array(Image.open(input_path + 'empire.jpg').convert('L'))
imshow(im)
gray()
show()
print int(im.min()),int(im.max())

im2 = 255-im
imshow(im2)
gray()
show()
print int(im2.min()),int(im2.max())

im3 = (100.0/255)*im + 100
imshow(im3)
gray()
show()
print int(im3.min()),int(im3.max())

im4 = 255.0 * (im/255.0)**2
imshow(im4)
gray()
show()
print int(im4.min()),int(im4.max())

pil_im = Image.fromarray(im)
pil_im.show()


