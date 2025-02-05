import easyocr
from config import LANGUAGES, USE_GPU
from utils.preprocess_image import preprocess_image

class OCRService:
    def __init__(self):
        # self.reader = easyocr.Reader(LANGUAGES, gpu=USE_GPU)
        self.reader = easyocr.Reader(LANGUAGES, gpu=USE_GPU, detector=True, recognizer=True)

    def extract_text(self, image_path):
        processed_path = preprocess_image(image_path)  # Apply preprocessing
        result = self.reader.readtext(processed_path)
        return [detection[1] for detection in result]
