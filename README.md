# short-me
A minimal URL shortener API

---
## Features
- `POST /shorten` – accepts a long URL and returns a short one.  
If the URL has already been shortened, returns the existing short codeIf the URL has already been shortened, returns the existing short code
- `GET /{code}` – redirects to the original long URL
- Basic persistence using SQLite
- Error handling
---
## Tech Stack
- Python
- FastAPI
- SQLite
- SQLAlchemy
---
## Requirements
Install dependencies:
```bash 
   pip install -r requirements.txt
```
---
## How to run
Start the server with:
```bash 
   uvicorn app.main:app --reload
```
   The API will be available at:

http://localhost:8000

---
## Example usage
Shorten a URL:
```bash 
   curl -X POST http://localhost:8000/shorten -H "Content-Type: application/json" -d '{"url": "https://example.com"}'
```
Redirect to original URL:
```bash 
   curl -v http://localhost:8000/abc123
```
---
## Running tests

To run tests, install development dependencies:
```bash
   pip install -r requirements-dev.txt
```

Then run:
```bash
   pytest
```
---
## License
[MIT](./LICENSE)