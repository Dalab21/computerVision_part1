# counting Number of pixel from image
from PIL import Image

image = "../data/img8.jpg"

with Image.open(image) as img:
    width, height = img.size

    total_pixels = width * height

    print(f"Image dimensiosn : {width} x {height}")
    print(f"Total number of pixels in Image : {total_pixels}")