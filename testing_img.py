from PIL import Image
from pytesseract import pytesseract
  
# Defining paths to tesseract.exe
# and the image we would be using



path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path1 = r"image.jpg"
image_path = r"Cropped-Image-Copy.jpg"
  
# Opening the image & storing it in an image object
img = Image.open(image_path)
img2 = Image.open(image_path1)
# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)
text2 = pytesseract.image_to_string(img2)
  
# Displaying the extracted text
print(text[:-1])
print(text2[:-1])