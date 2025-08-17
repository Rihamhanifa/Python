
#How to convert image to pdf in Python

# Python3 program to convert image to pfd
# using img2pdf library
# importing necessary libraries

import img2pdf
from PIL import Image
import os

print (img2pdf.__version__)
# storing image path
img_path = "riham.jpg"
 
# storing pdf path
pdf_path = "file_pdf.pdf"

# opening image
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)
 
# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")

#pip3 install pillow && pip3 install img2pdf
