import os, glob, sys
import digital_display_ocr
from pytesseract import image_to_string
from PIL import Image

def ocr_core(filename):
    tessdata_dir = os.getcwd() + "/letsgodigital"

    text = image_to_string(
        Image.open(filename), 
        lang="letsgodigital", 
        config="--psm 11 \
            -c tessedit_char_whitelist=\".'0123456789\" \
            --tessdata-dir " + tessdata_dir
        )
    return text

def process_dir():
    for filepath in sorted(glob.glob(sys.argv[1] + '/*'), key=os.path.abspath):
        print("Performing OCR on file: " + filepath)
        print(ocr_core(filepath) + "\n")

process_dir()