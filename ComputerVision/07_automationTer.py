# Bulk Convert PNG to JPEG
from PIL import Image
import os


def convert_png_to_jpg_bulk(input_path, output_path):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        #Loop through all files in the input directory
        for file_name in os.listdir(input_path):
            if file_name.endswith(".png"):
                with Image.open(os.path.join(input_path, file_name)) as img:
                    jpg_name = file_name.replace(".png", ".jpg")
                    img.convert("RGB").save(os.path.join(output_path,jpg_name))
            
                print(f"convert is successful : {file_name} -> {jpg_name}")

        print("Bulk conversion is completed")
    except Exception as e:
        print(f"An error occured : {e}")
            
    

in_path="07"
out_path="output_img/"

convert_png_to_jpg_bulk(in_path, out_path)