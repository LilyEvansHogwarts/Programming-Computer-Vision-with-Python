from PIL import Image
import os
from pylab import *

input_path = '../data/'
output_path = './data/'
'''
# example 1.1
pil_im = Image.open(input_path+'empire.jpg')
pil_im.show()

# example 1.1.1
filelist = os.listdir(input_path)
for infile in filelist:
    outfile = os.path.splitext(infile)[0]+'.jpg'
    if infile != outfile:
        try:
            Image.open(input_path + infile).save(output_path + outfile)
        except IOError:
            print 'cannot convert',infile

# example 1.1.2
pil_im.thumbnail((128,128))
pil_im.show()

# example 1.1.3
box = (100,100,400,400)
region = pil_im.crop(box)
region.show()
region = region.transpose(Image.ROTATE_180)
region.show()
pil_im.paste(region,box)
pil_im.show()

print 'size:',pil_im.size
print 'mode:',pil_im.mode
print 'format',pil_im.format

# example 1.1.4
out1 = pil_im.resize((128,128))
out1.show()

out2 = pil_im.rotate(45)
out2.show()

pil_im.thumbnail((128,128))
pil_im.show()
'''

# example 1.2.1
im = array(Image.open(input_path+'empire.jpg'))
imshow(im)

x = [100,100,400,400]
y = [200,500,200,500]

plot(x,y,'r*')
plot(x[:2],y[:2])

title('Ploting: "empire.jpg"')
axis('off')
show()













