from PIL import Image
from pylab import *

input_path = '../data/'
output_path = './data/'

im = array(Image.open(input_path + 'empire.jpg'))
imshow(im)
print 'Please click 3 points'
x = ginput(3)
print 'you clicked:',x
show()







