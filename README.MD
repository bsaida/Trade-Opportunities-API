# Trade Opportunities API

## Features
- FastAPI backend
- Gemini AI integration
- Rate limiting
- JWT Authentication
- Session tracking
- Markdown report generation

## Setup

1. Clone repo
2. Install dependencies:
   pip install -r requirements.txt

3. Add Gemini API key:
   export GEMINI_API_KEY=your_key_here

4. Run server:
   uvicorn main:app --reload

## Usage

1. Get token:
   GET /token?username=test

2. Analyze sector:
   GET /analyze/pharmaceuticals
   Authorization: Bearer <token>