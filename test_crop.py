import cv2
import numpy as np
from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"img.jpg"
pytesseract.tesseract_cmd = path_to_tesseract

img = cv2.imread('Output.jpeg')
print(img.shape) # Print image shape
cv2.imshow("original", img)
 
# Cropping an image
cropped_image = img[0:35, 400:700]
text = pytesseract.image_to_string(cropped_image)
  
# Displaying the extracted text
print(text[:-1])
# Display cropped image
cv2.imshow("cropped", cropped_image)
 
# Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)
 
cv2.waitKey(0)
cv2.destroyAllWindows()