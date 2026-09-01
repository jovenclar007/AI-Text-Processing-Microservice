# Architecture

## Simple Architecture Diagram

```text
                    Client
              Postman / Frontend
                       |
                       | HTTP + JSON
                       v
              +------------------+
              |    Flask API     |
              |     app.py       |
              +--------+---------+
                       |
          +------------+-------------+
          |            |             |
          v            v             v
     /translate   /analyze-text  /batch-analyze
          |            |             |
          v            v             v
     Gemini Service  Text Analysis  ThreadPoolExecutor
          |            |             |
          v            v             v
    Google Gemini   Local Python   Concurrent analysis
         API          calculation
```

## How to Explain It

1. The client sends an HTTP request.
2. Flask receives the request through a route.
3. The route validates the input.
4. The route calls a service when business logic is needed.
5. `/translate` calls Gemini.
6. `/analyze-text` calculates the results locally.
7. `/batch-analyze` processes independent texts concurrently.
8. Flask returns a JSON response.

## Why This Design Is Simple

- `routes/` contains API endpoints.
- `services/` contains the main processing logic.
- `tests/` contains automated tests.
- `performance/` contains the benchmark.
- `docs/` contains project documentation.
