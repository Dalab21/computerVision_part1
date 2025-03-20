# Cropping image with python using Pillow
#def crop_box, img_input path, ...
from PIL import Image

input = '../data/img4.jpg'
output = 'img_cropped_out4.jpg'

cb = (150, 150, 450, 450)

def crop_image(input_image, output_image, crop_box): 
    #open img
    img = Image.open(input_image)

    #crop img with crop_box(left, upper, right, lower)
    img_cropped = img.crop(crop_box)

    #convert to RGB
    if img.mode == 'RGBA':
        img_cropped = img.convert('RGB')

    #save img
    img_cropped.save(output_image, quality=95) #ajuste la qualité de l'image si necessaire


crop_image(input, output, cb)