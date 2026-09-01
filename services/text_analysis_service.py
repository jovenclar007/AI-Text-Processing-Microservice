import re
from functools import lru_cache


@lru_cache(maxsize=128)
def analyze_text(text):
    """Perform simple text analysis locally using Python."""
    words = text.split()
    word_count = len(words)
    character_count = len(text)
    sentence_count = len([s for s in re.split(r"[.!?]+", text) if s.strip()])
    longest_word = max(words, key=len) if words else ""

    # Average reading speed: 200 words per minute.
    reading_seconds = max(1, round(word_count / 200 * 60))

    return {
        "text": text,
        "word_count": word_count,
        "character_count": character_count,
        "sentence_count": sentence_count,
        "longest_word": longest_word,
        "estimated_reading_time": f"{reading_seconds} second(s)"
    }
