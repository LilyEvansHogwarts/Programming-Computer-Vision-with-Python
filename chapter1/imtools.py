import os
from PIL import Image
from numpy import *
from pylab import *

def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im,sz):
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

def histeq(im,nbr_bins=256):
    imhist,bins,_ = hist(im.flatten(),nbr_bins,normed=True)
    show()
    cdf = imhist.cumsum()
    cdf = 255 * cdf/cdf[-1]
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf





