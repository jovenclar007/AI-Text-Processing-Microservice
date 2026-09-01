# AI Text Processing Microservice

A simple MSIT 132 capstone microservice built with **Python Flask** and **Google Gemini**.

The project demonstrates:

1. REST API development
2. External API integration (Gemini)
3. Local text computation
4. Concurrency with `ThreadPoolExecutor`
5. Simple optimization with caching
6. Unit testing
7. Usability testing
8. Docker containerization

## 1. Project Structure

```text
AI-Text-Processing-Microservice/
│
├── routes/
│   ├── health.py
│   ├── translate.py
│   ├── analyze.py
│   └── batch.py
│
├── services/
│   ├── gemini_service.py
│   └── text_analysis_service.py
│
├── tests/
│   ├── test_health.py
│   ├── test_analyze.py
│   ├── test_translate.py
│   └── test_batch.py
│
├── performance/
│   └── benchmark.py
│
├── usability/
│   ├── usability_test_form.csv
│   └── analyze_results.py
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── ENDPOINTS.md
│   ├── TESTING.md
│   ├── OPTIMIZATION.md
│   ├── REFLECTION.md
│   └── DEFENSE_GUIDE.md
│
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── .env.example
```

## 2. Requirements

- Python 3.12+
- A Gemini API key for `/translate`
- Docker Desktop (optional, for container testing)

## 3. Local Setup — Windows

Create a virtual environment:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\Activate.ps1
```

Install packages:

```powershell
pip install -r requirements.txt
```

Create `.env` from `.env.example` and add your own API key:

```text
GEMINI_API_KEY=your_real_key_here
GEMINI_MODEL=gemini-3.5-flash
```

**Never upload the real `.env` file or API key to GitHub.**

## 4. Run the API

```powershell
python app.py
```

The service runs at:

```text
http://127.0.0.1:5000
```

## 5. Quick API Tests

### Health

```http
GET /health
```

### Local text analysis

```http
POST /analyze-text
Content-Type: application/json
```

```json
{
  "text": "Hello world. This is my microservice."
}
```

### Gemini translation

```http
POST /translate
Content-Type: application/json
```

```json
{
  "text": "Magandang umaga",
  "target_language": "English"
}
```

### Concurrent batch analysis

```http
POST /batch-analyze
Content-Type: application/json
```

```json
{
  "texts": [
    "Hello world.",
    "Docker is useful.",
    "Microservices are modular."
  ]
}
```

## 6. Run Tests

From the project root:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

The translation test uses a mock, so the test suite does **not** require a live Gemini request.

## 7. Run the Usability Test

After testing with 3–5 participants, enter their Pass/Fail results and ratings in `usability\usability_test_form.csv`. Then run:

```powershell
python usability\analyze_results.py
```

Use the output in the usability section of your report or defense. Do not invent results.

## 8. Run the Optimization Benchmark

```powershell
python performance\benchmark.py
```

The benchmark compares repeated text analysis before and after the cache optimization. The exact timing depends on the computer used.

## 9. Docker

Build:

```powershell
docker build -t ai-text-processing-microservice .
```

Run:

```powershell
docker run --env-file .env -p 5000:5000 ai-text-processing-microservice
```

Then test:

```text
http://localhost:5000/health
```

## 10. MSIT 132 Requirement Mapping

| Requirement | Project Feature |
|---|---|
| At least two endpoints | `/health`, `/translate`, `/analyze-text`, `/batch-analyze` |
| External API | `/translate` → Gemini |
| Local computation | `/analyze-text` |
| Containerization | Dockerfile |
| Documentation | `docs/` + README |
| Concurrency | `ThreadPoolExecutor` in `/batch-analyze` |
| Optimization | `lru_cache` in text analysis |
| Testing | `tests/` |
| AI integration | Gemini translation |

## 11. Important Defense Explanation

Keep the explanation simple:

> "My microservice accepts text through REST API endpoints. The translation endpoint sends text to Google Gemini, which is the external API. The analysis endpoint performs calculations locally using Python. For multiple texts, the batch endpoint uses ThreadPoolExecutor to demonstrate concurrency. I also used a small cache so repeated analysis of the same text does not need to repeat the calculation. Finally, I containerized the service using Docker."

## Author

Joven Clar Granada  
MSIT 132 Final Project
