Stage 0 Backend API - HNG12
This public API is developed for the Stage 0 Backend task of HNG12. It retrieves essential information, including the developer's registered email, the current datetime, and the GitHub URL for the project's codebase.

Features
Public API: Accessible via a single GET endpoint.
Dynamically Generated Data: Returns the current datetime in ISO 8601 format (UTC).
CORS Support: Handles Cross-Origin Resource Sharing (CORS).
JSON Response: All responses are in JSON format.
Technology Stack
Framework: FastAPI
Programming Language: Python
Deployment: Railway
Dependency Management: pip
Installation
Clone the repository: git clone https://github.com/KyakuwaPeninnah/hng-stage0

Install Dependencies: pip install -r requirements.txt

Run the app: uvicorn main:app --reload

Open in browser: http://127.0.0.1:8000

API Documentation
Endpoint
Base URL:
https://web-production-eafdf.up.railway.app/
GET /
GET /hire/python-developers

Response Format
HTTP 200 OK
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
Deployment
The API is deployed on https://hng-stage0-production-0990.up.railway.app/

Useful Links
[Hire Python Developers](https://hng.tech/hire/python-developers)
Hire C# Developers
Hire Golang Developers
Hire PHP Developers
Hire Java Developers
Hire Node.js Developers