from PIL import Image
import os

input_path = '../data/'
output_path = './data/'

filelist = [f for f in os.listdir(input_path)]


for infile in filelist:
    outfile = os.path.splitext(infile)[0] + '.jpg'
    if outfile != infile:
        try:
            Image.open(input_path + infile).save(output_path + outfile)
        except IOError:
            print "cannot convert",infile




