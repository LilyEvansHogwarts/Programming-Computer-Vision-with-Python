from PIL import Image
from pylab import *
import os

def compute_average(imlist):
    averageim = array(Image.open(imlist[0]),'f')
    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print imname + '...skipped'
    averageim /= len(imlist)
    return array(averageim, 'uint8')

input_path = './data/'

filelist = [os.path.join(input_path,f) for f in os.listdir(input_path)]

avg = compute_average(filelist)
im = Image.fromarray(avg)
im.show()







