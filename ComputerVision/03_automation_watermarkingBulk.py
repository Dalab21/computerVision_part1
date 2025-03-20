# Watermarking Bulk Images
from PIL import Image, ImageDraw, ImageFont
import os


def add_watermark(input_folder, output_folder, watermark_text):
    img =Image.open(input_folder)

    if img.mode != 'RGB':
        img = img.convert('RGB')

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 36)

    #BBox du text
    text_bbox = draw.textbbox((0,0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # position text centering
    text_position = ((img.width - text_width) //2, (img.height - text_height) //2)

    #Add watermark text to image
    draw.text(text_position, watermark_text, fill=(255, 255, 155, 100), font=font)

    #save
    img.save(output_folder, quality=95)



def batch_watermark(input_folder, output_folder, watermark_text):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # watermarking for each image
            add_watermark(input_path, output_path, watermark_text)

# 

input_imgs_folder = '../data'
output_watermarked_data = 'output'
watermark_text = 'In ALLAH We Trust !!!'

batch_watermark(input_imgs_folder, output_watermarked_data, watermark_text)

