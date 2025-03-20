# Flipping Image
from PIL import Image

img_path = '../data/img4.jpg'

img = Image.open(img_path)

flipped_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
flipped_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)
    

flipped_horizontal.save('flipped_horizontal_img.jpg')
flipped_vertical.save('flipped_vertical_img.jpg')
