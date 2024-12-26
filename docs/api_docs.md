
---

### **2. `api_docs.md`**

Details the API endpoints for the backend server used by the extension.

```markdown
# API Documentation - SafeGuardAI

This document describes the available API endpoints provided by the SafeGuardAI backend.

---

## Base URL
- `http://127.0.0.1:5000`

---

## Endpoints

### 1. **`POST /scan/file`**

**Description**: Analyze uploaded file for malware or threats.

- **Request**:
   ```json
   {
     "file_name": "example.exe",
     "file_hash": "a1b2c3d4..."
   }
