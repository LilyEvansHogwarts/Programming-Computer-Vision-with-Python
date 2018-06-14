from PIL import Image
from pylab import *

input_path = '../data/'
output_path = './data/'

im = array(Image.open(input_path + 'empire.jpg'))
print im.shape, im.dtype

im = array(Image.open(input_path + 'empire.jpg').convert('L'))
print im.shape, im.dtype

im = array(Image.open(input_path + 'empire.jpg').convert('L'),'f')
print im.shape, im.dtype




