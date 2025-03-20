# Extract text from Image using Tesseract OCR
from PIL import Image
import pytesseract

# Path to extract executable (installation in pc)
pytesseract.pytesseract.tesseract_cmd= r'C:\\Program Files\Tesseract-OCR\\tesseract.exe'

def extract_tect_from_image(img_path):

    try:
        with Image.open(img_path) as img:
            text = pytesseract.image_to_string(img)
            return text
        
    except Exception as e:
        print(f"An error occured : {e}")
        return None
    


img_path_link = '../data/img8.jpg'  #path img

extract_text = extract_tect_from_image(img_path_link)
if extract_text:
    print(f"Extract Text : {extract_text}")
else:
    print("Text extraction failed .... ")