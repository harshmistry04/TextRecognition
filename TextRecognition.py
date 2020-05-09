import pytesseract as tess
from PIL import image
tess.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

img = Image.open("C:/Users/harsh/Desktop/Learnings/Text Recognition/testimage.jpg")
text = tess.image_to_string(img)
print(text)