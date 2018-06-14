from PIL import Image

input_path = '../data/'
output_path = './data/'

pil_im = Image.open(input_path + 'empire.jpg')
pil_im.show()

out1 = pil_im.resize((128,128))
out1.show()

out2 = pil_im.rotate(45)
out2.show()







