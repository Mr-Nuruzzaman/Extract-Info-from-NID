import easyocr
from config import LANGUAGES, USE_GPU

class OCRService:
    def __init__(self):
        self.reader = easyocr.Reader(LANGUAGES, gpu=USE_GPU)

    def extract_text(self, image_path):
        result = self.reader.readtext(image_path)
        return [detection[1] for detection in result]
