# 10–15 Minute Oral Defense Guide

## 1. Introduction — 1 minute

Say:

> "My project is an AI Text Processing Microservice built using Python Flask. It provides text translation using Google Gemini, local text analysis, and concurrent batch analysis. It is also containerized with Docker."

## 2. Architecture — 2 minutes

Show `ARCHITECTURE.md`.

Explain:

- Flask receives requests.
- Routes handle HTTP requests and validation.
- Services contain processing logic.
- Gemini is the external API.
- Text analysis is local.
- ThreadPoolExecutor demonstrates concurrency.

## 3. Live API Demo — 4 minutes

Recommended order:

### A. Health

```text
GET /health
```

Explain that it confirms the service is running.

### B. Local computation

```text
POST /analyze-text
```

Use:

```json
{
  "text": "Hello world. This is my MSIT 132 project."
}
```

Explain that the calculation is done locally by Python.

### C. AI integration

```text
POST /translate
```

Use:

```json
{
  "text": "Magandang umaga",
  "target_language": "English"
}
```

Explain that Flask sends the request to Gemini and returns the AI result.

### D. Concurrency

```text
POST /batch-analyze
```

Send several texts and explain that `ThreadPoolExecutor` processes independent tasks concurrently.

## 4. Docker — 2 minutes

Show:

```powershell
docker build -t ai-text-processing-microservice .
```

Then:

```powershell
docker run --env-file .env -p 5000:5000 ai-text-processing-microservice
```

Open `/health` and show that the API still works from the container.

## 5. Optimization and Testing — 2 minutes

Run:

```powershell
python performance\benchmark.py
```

Then:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

Explain the cache optimization and the automated tests.

## 6. Closing — 1 minute

Say:

> "This project demonstrates the main MSIT 132 competencies in one simple service: REST APIs, external API integration, local computation, concurrency, optimization, testing, AI integration, and Docker containerization."

## Likely Questions

### Why did you use Flask?

> "Flask is lightweight and easy to understand for a small REST microservice."

### Why is Gemini an external API?

> "The Gemini model runs outside my application. My service sends an API request and receives the generated translation."

### Which endpoint performs local computation?

> "`/analyze-text`. It calculates the text statistics using Python without calling an external service."

### Where is concurrency implemented?

> "In `/batch-analyze`, using Python's ThreadPoolExecutor."

### Where is optimization implemented?

> "In `text_analysis_service.py`, using `lru_cache` to reuse results for repeated text."

### Why mock Gemini in tests?

> "To avoid depending on network access, API quota, or a real API key during automated testing."

### Why Docker?

> "Docker packages the application and its dependencies so it can run consistently in another environment."

### What would you improve next?

> "I would add authentication, rate limiting, logging, monitoring, persistent storage, and a frontend."
