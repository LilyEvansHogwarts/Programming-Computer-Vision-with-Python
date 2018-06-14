from PIL import Image

input_path = '../data/'
output_path = './data/'

pil_im = Image.open(input_path + 'empire.jpg')
pil_im.show()

box = (100,100,400,400)
region = pil_im.crop(box)
region.show()

region = region.transpose(Image.ROTATE_180)
region.show()

pil_im.paste(region, box)
pil_im.show()



