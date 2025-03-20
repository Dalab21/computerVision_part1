# Cropping image with python using Pillow
#def crop_box, img_input path, ...
from PIL import Image

def crop_image(input_image, output_image, crop_box): 
    #open img
    img = Image.open(input_image)

    img_cropped = img.crop(crop_box)

    
    if img.mode != 'RGB':
        img_cropped = img.convert('RGB')


    img_cropped.save(output_image, quality=95) 




img_in = '../data/img4.jpg'
img_out = 'img_cropped_out4.jpg'
cb = (150, 150, 450, 450)
crop_image(input, output, cb)