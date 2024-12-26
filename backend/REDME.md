# SafeGuardAI Backend

## Description
This is the backend server for SafeGuardAI Chrome extension. It handles file hash analysis, URL safety checks, and integrates AI models for malware and phishing detection.

## Setup

### Prerequisites
- Python 3.8+
- Virtual Environment

### Install Dependencies
```bash
pip install -r requirements.txt
//--------------
Run Server
Start the Flask backend:

bash
Copy code
python app.py
The server will run on http://localhost:5000/.

API Endpoints
Analyze File
POST /analyze

Request:
json
Copy code
{
    "type": "file",
    "hash": "file_hash",
    "name": "file_name"
}
Response:
json
Copy code
{"isSafe": true, "message": "File analyzed."}
Analyze URL
POST /analyze

Request:
json
Copy code
{
    "type": "url",
    "url": "http://example.com"
}
Response:
json
Copy code
{"isSafe": false, "message": "URL analyzed."}
Notes
Replace SAFE_BROWSING_API key with a valid Google Safe Browsing API key.
Pre-trained AI models must be placed in the ai_models directory.
yaml
Copy code

---

This backend handles all file hash and URL analysis, integrates AI models, and provides a clean API for the frontend to interact with.

Let me know if you need any refinements! 🚀
