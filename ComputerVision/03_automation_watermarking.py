# define function to add watermark to image with Pillow
from PIL import Image, ImageDraw, ImageFont
import os




def add_watermark(input_img, output_img, watermark_text):
    # open image
    img = Image.open(input_img)

    if img.mode != 'RGB':
        img = img.convert('RGB') # convert img to RGB mode if it's in Aplha channel (RGBA)

    # create drawing text
    draw = ImageDraw.Draw(img)

    # create watermark(text and font)
    font = ImageFont.truetype("arial.ttf", 36)

    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)

    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # calculate text position for centering in  image
    text_position = ((img.width - text_width) // 2, (img.height - text_height) // 2)

    # add watermark text to image
    draw.text(text_position, watermark_text, fill=(255, 255, 255), font=font)

    # save the watermark image as Jpeg format
    img.save(output_img, quality=95)



#call function
input_img = "../data/img3.jpg"
output_img = "ing_watermark_img.jpg"
watermark_text = "Welcome in Paradise"

add_watermark(input_img, output_img, watermark_text)
