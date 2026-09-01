import timeit
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


from services.text_analysis_service import analyze_text


TEXT = (
    "Artificial intelligence is transforming education. "
    "Microservices help developers build modular applications. "
    "Docker makes application deployment easier."
)


def uncached_analysis(text):
    """Run the same local calculation without using the cache."""
    return analyze_text.__wrapped__(text)


def cached_analysis(text):
    """Run the optimized cached function twice; the second call is a cache hit."""
    analyze_text(text)
    return analyze_text(text)


if __name__ == "__main__":
    analyze_text.cache_clear()
    before = timeit.timeit(lambda: uncached_analysis(TEXT), number=1000)

    analyze_text.cache_clear()
    after = timeit.timeit(lambda: cached_analysis(TEXT), number=1000)

    improvement = ((before - after) / before) * 100

    print("================================")
    print("TEXT ANALYSIS OPTIMIZATION")
    print("================================")
    print("Runs: 1000")
    print(f"Before caching : {before:.6f} seconds")
    print(f"After caching  : {after:.6f} seconds")
    print(f"Improvement     : {improvement:.2f}%")
    print("Results depend on the computer used.")
