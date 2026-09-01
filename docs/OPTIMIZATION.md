# Optimization

## Optimization Used

The local text analysis function uses Python's `lru_cache`:

```python
@lru_cache(maxsize=128)
def analyze_text(text):
    ...
```

If the exact same text is analyzed again, the previous result can be returned from memory instead of repeating the calculation.

## Benchmark

Run:

```powershell
python performance\benchmark.py
```

The benchmark performs 1,000 repeated calls and compares:

- **Before:** direct calculation every time
- **After:** cached repeated calculation

The program calculates the percentage improvement automatically.

Example output format:

```text
================================
TEXT ANALYSIS OPTIMIZATION
================================
Runs: 1000
Before caching : X.XXXXXX seconds
After caching  : X.XXXXXX seconds
Improvement     : XX.XX%
Results depend on the computer used.
```

Do not memorize a sample number. During the defense, show the actual number produced on your computer.

## Concurrency

`/batch-analyze` also uses `ThreadPoolExecutor` so independent texts can be processed by multiple worker threads.

This demonstrates the concurrency competency. It is separate from the cache optimization.

## Defense Statement

> "I used caching as a simple optimization. Repeated analysis of the same text can use the cached result instead of recalculating it. I measured the difference using Python timeit. I also used ThreadPoolExecutor for concurrent batch processing."
