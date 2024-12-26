# # app.py - Backend for File and URL Analysis
# from flask import Flask, request, jsonify
# import hashlib
# import os
# from utils.file_hashing import hash_file
# from utils.url_checker import check_url
# from ai_models.malware_detection import scan_file_with_ai
# from ai_models.phishing_detector import scan_url_with_ai

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Welcome to SafeGuardAI Backend!"

# # Analyze File Endpoint
# @app.route('/analyze', methods=['POST'])
# def analyze():
#     data = request.json
#     if not data:
#         return jsonify({"error": "No data provided"}), 400

#     if data.get("type") == "file":
#         file_name = data.get("name", "unknown")
#         file_hash = data.get("hash", "")
#         if not file_hash:
#             return jsonify({"error": "No file hash provided"}), 400

#         # Run AI-based file scan
#         ai_result = scan_file_with_ai(file_hash)
#         return jsonify({"isSafe": ai_result, "message": f"File '{file_name}' analyzed."})

#     elif data.get("type") == "url":
#         url = data.get("url", "")
#         if not url:
#             return jsonify({"error": "No URL provided"}), 400

#         # Run AI-based phishing scan
#         ai_result = scan_url_with_ai(url)
#         return jsonify({"isSafe": ai_result, "message": f"URL '{url}' analyzed."})

#     return jsonify({"error": "Invalid request type"}), 400
 
# if __name__ == '__main__':
#     app.run(debug=True)

# app.py - Backend for File and URL Analysis
import logging, 
from flask import Flask, request  #- getting flask , request , 
import hashlib
import os
from utils.file_hashing import hash_file #not in use at the moment
from utils.url_checker import check_url
from ai_models.malware_detection import scan_file_with_ai #-malware detecting
from ai_models.phishing_detector import scan_url_with_ai #- phishing detecting 

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to SafeGuardAI Backend!"

# Analyze File and URL Endpoint
@app.route('/analyze', methods=['POST'])
import logging

# Configure logging
logging.basicConfig(filename="scan_logs.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    if not data:
        logging.warning("No data provided in the request.")
        return jsonify({"error": "No data provided"}), 400

    if data.get("type") == "file":
        file_name = data.get("name", "unknown")
        file_hash = data.get("hash", "")
        if not file_hash:
            logging.warning("No file hash provided.")
            return jsonify({"error": "No file hash provided"}), 400

        ai_result = scan_file_with_ai(file_hash)
        logging.info(f"File '{file_name}' analyzed. Safe: {ai_result}")
        return jsonify({"isSafe": ai_result, "message": f"File '{file_name}' analyzed."})

    elif data.get("type") == "url":
        url = data.get("url", "")
        if not url:
            logging.warning("No URL provided.")
            return jsonify({"error": "No URL provided"}), 400

        ai_result = scan_url_with_ai(url)
        logging.info(f"URL '{url}' analyzed. Safe: {ai_result}")
        return jsonify({"isSafe": ai_result, "message": f"URL '{url}' analyzed."})

    logging.warning("Invalid request type.")
    return jsonify({"error": "Invalid request type"}), 400

# def analyze():
#     data = request.json
#     if not data:
#         return jsonify({"error": "No data provided"}), 400

#     if data.get("type") == "file":
#         file_name = data.get("name", "unknown")
#         file_hash = data.get("hash", "")
#         if not file_hash:
#             return jsonify({"error": "No file hash provided"}), 400

#         # Run AI-based file scan
#         ai_result = scan_file_with_ai(file_hash)
#         return jsonify({"isSafe": ai_result, "message": f"File '{file_name}' analyzed."})

#     elif data.get("type") == "url":
#         url = data.get("url", "")
#         if not url:
#             return jsonify({"error": "No URL provided"}), 400

#         # Run AI-based phishing scan
#         ai_result = scan_url_with_ai(url)
#         return jsonify({"isSafe": ai_result, "message": f"URL '{url}' analyzed."})

#     return jsonify({"error": "Invalid request type"}), 400

# if __name__ == '__main__':
#     app.run(debug=True)
