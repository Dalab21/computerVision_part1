#  Brightness
from PIL import Image, ImageEnhance

def ajust_brightness(input_img, output_img, factor):
    #open image
    img = Image.open(input_img)

    if img.mode == 'RGBA':
        img = img.convert('RGB')

    # Enhance brightness
    enhancer = ImageEnhance.Brightness(img)
    enhanced_img = enhancer.enhance(factor)

    enhanced_img.save(output_img, format='JPEG', quality=95)



# call funct
img_input = '../data/img2.jpg'
img_output = 'img_brightness01.jpeg'
factor_brightness = 1.8

ajust_brightness(img_input, img_output, factor_brightness)



