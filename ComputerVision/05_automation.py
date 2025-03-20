# Image color Palette Generation (Pillow, webcolors, collections,...)
from PIL import Image
from collections import Counter
import webcolors #pip 

def generate_palette(img_path, num_colors):

    img = Image.open(img_path)
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    # resize image to speed up color extraction
    img.thumbnail((200, 200))

    # colors from image
    pixels = img.getdata()

    # extract colors & count occurances
    counter_colors = Counter(pixels) 

    # most common colors
    most_common = counter_colors.most_common(num_colors) 

    #Display color palette
    print(f"Top {num_colors} colors in this Image : ")


    for color, count in most_common:
        try:
            color_name = webcolors.rgb_to_name(color[:3]) # extract RGB values from RGBA tuple
        except ValueError:
            color_name = "N/A"
        print(f"Color : {color[:3]}, Count : {count}, Name : {color_name}")



input_img = '../data/img4.jpg'
num_colors_to_extract = 3

generate_palette(input_img, num_colors_to_extract)
