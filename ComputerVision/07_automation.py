# Converting image into PDF 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def image_to_pdf(img_path, output_pdf):
    # create de canvas (PDF Document)
    c = canvas.Canvas(output_pdf, pagesize=letter)
    c.drawImage(img_path, 100, 100) #possible to adjust position 
    c.save()



img_in = "../data/img8.jpg"
output_img = "output_img8.pdf"
image_to_pdf(img_in, output_img)