# Convert PNG to JPEG
from PIL import Image


def convert_png_to_jpg(img_input, img_output):
    try:
        with Image.open(img_input) as img:
            if img.mode != 'RGB':
                img.convert('RGB').save(img_output, "JPEG")
                print(f"convert is success. Imahe saved as {img_output}")
            
    except Exception as e:
        print(f"Error occured : {e}")



in_img="img.png"
out_img="img_in_jpg.jpeg"

convert_png_to_jpg(in_img, out_img)