from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from services.ocr_service import OCRService

app = Flask(__name__)

# Set up a directory for image uploads
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ocr_service = OCRService()

@app.route('/extract-text', methods=['POST'])
def extract_text():
    try:
        # Check if the 'images' field is present in the request
        if 'images' not in request.files:
            return jsonify({"error": "No images part in the request"}), 400
        
        files = request.files.getlist('images')
        # if len(files) != 2:
        #     return jsonify({"error": "Please upload exactly two images"}), 400

        extracted_texts = []
        
        for file in files:
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(image_path)

            # Extract text from the image
            extracted_text = ocr_service.extract_text(image_path)
            extracted_texts.append({
                'image': filename,
                'extracted_text': extracted_text
            })
            
            # Delete the image after processing
            os.remove(image_path)

        return jsonify({"status": "success", "data": extracted_texts}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8081)
