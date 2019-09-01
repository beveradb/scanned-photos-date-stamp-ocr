from PIL import Image
import os
import pytesseract

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

for filename in os.listdir("example-images"):
    filepath = "example-images/" + filename
    print("Processing file: " + filepath)
    print(ocr_core(filepath))
