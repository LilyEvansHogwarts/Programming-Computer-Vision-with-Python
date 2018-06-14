from PIL import Image
from pylab import *

input_path = '../data/'
output_path = './data/'

im = array(Image.open(input_path + 'empire.jpg').convert('L'))
figure()
gray()
contour(im, origin='image')
axis('equal')
axis('off')
show()

figure()
hist(im.flatten(),128)
show()




