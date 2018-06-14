from PIL import Image
from pylab import *

input_path = '../data/'
output_data = './data/'

im = array(Image.open(input_path + 'empire.jpg'))
imshow(im)

x = [100,100,400,400]
y = [200,500,200,500]

plot(x,y,'r*')
plot(x[:2],y[:2])

# plot(x,y,'go-')
# plot(x,y,'ks:')


axis('off')
title('Plotting: "empire.jpg"')
show()







