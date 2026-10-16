# Service Health REST API

Designed and implemented a REST API for monitoring internal services.

## Endpoints (4)
- `GET /health` - Returns status of all services (Public)
- `GET /health/<service_name>` - Returns specific service status (Auth required)
- `POST /check` - Validates and checks a service (Auth + JSON validation)

## Features
- Input validation & error handling (400, 404, 401)
- Bearer token authentication
- HTTP status codes best practices
- Tested with Postman, Deployed on Linux

## Tech Stack
Python, Flask, HTTP, REST API, Git, Linux

## How to Run
```bash
pip install -r requirements.txt
python app.py
# Server runs on http://localhost:5000
