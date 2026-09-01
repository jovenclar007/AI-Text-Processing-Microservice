# Testing

The project uses Python's built-in `unittest` framework.

Run all automated tests:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

## Tests Included

| Test | Purpose |
|---|---|
| `test_health.py` | Checks `/health` and status value |
| `test_analyze.py` | Checks local calculations and invalid input |
| `test_translate.py` | Checks validation and a mocked successful translation |
| `test_batch.py` | Checks batch processing and invalid input |

## Why Translation Is Mocked

The translation test does not call Gemini. It uses a mock response so tests are:

- faster
- repeatable
- independent of API quota
- safe to run without an API key

## Usability Testing

Technical unit tests are supported by a separate usability test. See `docs/USABILITY_TESTING.md` and `usability/usability_test_form.csv`.

## Defense Statement

> "I created automated tests for the health check, local analysis, translation validation, mocked translation success, and batch analysis. I also performed a small usability test where users completed the main API tasks and rated ease of use."
