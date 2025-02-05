# from config import IMAGE_PATH, OUTPUT_TEXT_FILE
# from services.ocr_service import OCRService
# from utils.file_handler import save_text_to_file

# def main():
#     ocr_service = OCRService()
#     extracted_text = ocr_service.extract_text(IMAGE_PATH)
    
#     if extracted_text:
#         print("\nExtracted Text:")
#         for line in extracted_text:
#             print(line)

#         save_text_to_file(extracted_text, OUTPUT_TEXT_FILE)
#         print(f"\nText saved to: {OUTPUT_TEXT_FILE}")

# if __name__ == "__main__":
#     main()
