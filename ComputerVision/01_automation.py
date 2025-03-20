# RemoveBg (API ou Local) : pip install removebg
from removebg import RemoveBg

key="R6tik6yhKjdR1ZtZrkqieMxz"
removebg = RemoveBg(key, 'error.log')
#path image input
input_image = 'data/img1.jpg'

#path image output
#output_image = 'image_out.jpg'

removebg.remove_background_from_img_file(input_image, size = 'regular')
