# AI-Powered Website Link Analysis API

An AI-powered API that extracts website content and generates business, competitor, audience, and SEO insights using Google Gemini and FastAPI.

## Overview

This project analyzes a website URL, extracts relevant page content, and uses an AI model to generate structured insights.

It helps understand:
- Business overview
- Brand positioning
- Target audience
- Strengths and weaknesses
- Market gaps
- AI-inferred competitors
- Top 5 search query suggestions
- SEO recommendations
- Top 5 service suggestions

## Features

- Website content extraction using HTTPX and BeautifulSoup
- AI analysis using Google Gemini
- Structured JSON responses
- FastAPI REST API
- Interactive Swagger documentation
- URL validation
- Protection against localhost and private IP targets
- Redirect handling
- Response content size limit
- Automated tests with Pytest

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- HTTPX
- BeautifulSoup4
- Pydantic
- Google GenAI SDK
- Pytest

## Project Structure

```text
ai-link-analysis/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── website_extractor.py
│   │   ├── llm_service.py
│   │   └── analysis_service.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── validators.py
│
├── tests/
│   └── test_link_analysis.py
│
├── research/
│   └── llm_comparison.md
│
├── screenshots/
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-link-analysis
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the root directory.

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=your_supported_gemini_model
```

Never commit your actual API key.

### 6. Run the server

```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 4000 --reload
```

The API will run locally on port 4000.

## API Usage

### Endpoint

`POST /link-analysis`

### Request Body

```json
{
  "url": "https://example.com"
}
```

### Example cURL

```bash
curl -X POST "http://127.0.0.1:4000/link-analysis" \
-H "Content-Type: application/json" \
-d "{\"url\":\"https://example.com\"}"
```

### Successful Response

```json
{
  "success": true,
  "data": {
    "website": {
      "url": "https://example.com",
      "title": "Example Domain",
      "description": "",
      "headings": [],
      "content": "Extracted website text",
      "content_length": 171
    },
    "analysis": {
      "business_overview": "Business summary",
      "brand_positioning": "Brand positioning analysis",
      "target_audience": "Target audience description",
      "strengths": [],
      "weaknesses": [],
      "market_gaps": [],
      "competitors": [],
      "top_5_search_queries": [],
      "seo_recommendations": {
        "recommended_title": "SEO title suggestion",
        "meta_description": "Meta description suggestion",
        "keywords": [],
        "content_suggestions": []
      },
      "top_5_services": []
    }
  }
}
```

## API Documentation

Once the server is running