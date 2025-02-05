import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGE_PATH = os.path.join(BASE_DIR, "data", "nid_front.jpeg")
OUTPUT_TEXT_FILE = os.path.join(BASE_DIR, "output", "extracted_text.txt")

LANGUAGES = ['en', 'bn']
USE_GPU = True
