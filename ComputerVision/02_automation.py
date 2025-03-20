#02: resizing image with python using Pillow  pip install Pillow
from PIL import Image
input_image = '../data/img3.jpg'
output_image = 'image_output.jpg'

desired_width=200
desired_height=200

#Open image
img = Image.open(input_image)

#Resize image
img_resized =img.resize((desired_width,desired_height))

#Save image
img_resized.save(output_image)