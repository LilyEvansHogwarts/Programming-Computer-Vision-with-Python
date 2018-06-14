from PIL import Image

input_path = '../data/'
output_path = './data/'

pil_im = Image.open(input_path + 'empire.jpg')
pil_im.show()

pil_im.thumbnail((128,128))
pil_im.show()
