# GIF Image Creation using Pillow imageio -- pip install pillow imageio
import imageio
from PIL import Image
import numpy as np
import os
 
def create_gif_from_images(image_folder, output_gif, duration=0.5):
    # Get all image files in the folder
    images = []
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # Add other image formats if needed
            img_path = os.path.join(image_folder, filename)
            images.append(imageio.imread(img_path))
 
    # Save the images as a GIF
    imageio.mimsave(output_gif, images, duration=duration)
 
    print(f"GIF saved as {output_gif}")
 
# call of function
create_gif_from_images('img/', 'output.gif')