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

# stats.py  (add below count_characters)

def get_sorted_char_list(char_dict: dict) -> list[dict]:
    """
    Convert *char_dict* into a list of {"char": <c>, "num": <count>} elements
    and return the list sorted from highest to lowest count.
    """
    char_list = [{"char": ch, "num": n} for ch, n in char_dict.items()]
    char_list.sort(reverse=True, key=lambda d: d["num"])
    return char_list
