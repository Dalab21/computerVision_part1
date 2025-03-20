from PIL import Image

input_path='../data/img3.jpg'
output_path='img_rsz_output.jpg'

#dimensions
new_width= int(input("Enter new width: "))
new_height= int(input("Enter new height: "))
print(f"New Dims Img : ", "(", {new_width}, {new_height}, ")")

with Image.open(input_path) as img:
    img_resized=img.resize((new_width,new_height))
    img_resized.save(output_path)
    print("Image resized")

