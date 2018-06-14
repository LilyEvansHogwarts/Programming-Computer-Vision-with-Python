from PIL import Image

input_path = '../data/'
output_path = './data/'

pil_im = Image.open(input_path + 'empire.jpg')
pil_im.show()

pil_im = Image.open(input_path + 'empire.jpg').convert('L')
pil_im.show()





