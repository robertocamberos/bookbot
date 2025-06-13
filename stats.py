# stats.py
from collections import Counter
from typing import Dict


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in *text*."""
    return len(text.split())


def count_characters(text: str) -> Dict[str, int]:
    """
    Return a dict mapping each character (lower-cased) to its frequency
    in *text*.  Spaces, punctuation, and newlines are all included.
    """
    return Counter(text.lower())
