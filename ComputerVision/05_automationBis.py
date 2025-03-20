# Rotation with python script
from PIL import Image

img_path = '../data/img2.jpg'

img = Image.open(img_path)

rotated_img = img.rotate(90)
    
if rotated_img.mode == 'RGBA':
    rotated_img = rotated_img.convert('RGB')

rotated_img.save('rotated_img.jpg')

