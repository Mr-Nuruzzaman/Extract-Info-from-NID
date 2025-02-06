from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from services.ocr_service import OCRService
from utils.format_nid_back_text import format_nid_back_text
from utils.format_nid_front_text import format_nid_front_text

app = Flask(__name__)

# Set up a directory for image uploads
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ocr_service = OCRService()

@app.route('/extract-text', methods=['POST'])
def extract_text():
    try:
        # Check if both images are present in the request
        if 'nid-front' not in request.files or 'nid-back' not in request.files:
            return jsonify({"error": "Both nid-front and nid-back images are required"}), 400
        
        front_file = request.files['nid-front']
        back_file = request.files['nid-back']

        extracted_texts = {}

        # Process NID Front Image
        front_filename = secure_filename(front_file.filename)
        front_path = os.path.join(app.config['UPLOAD_FOLDER'], front_filename)
        front_file.save(front_path)
        front_text = ocr_service.extract_text(front_path)
        formatted_front_text = format_nid_front_text(front_text)
        os.remove(front_path)  # Delete after processing

        # Process NID Back Image
        back_filename = secure_filename(back_file.filename)
        back_path = os.path.join(app.config['UPLOAD_FOLDER'], back_filename)
        back_file.save(back_path)
        back_text = ocr_service.extract_text(back_path)
        formatted_back_text = format_nid_back_text(back_text)
        os.remove(back_path)  # Delete after processing

        # Merge the dictionaries
        combined_text = {**formatted_front_text, **formatted_back_text}

        # Update extracted_texts
        extracted_texts.update(combined_text)

        return jsonify(extracted_texts), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8081)
