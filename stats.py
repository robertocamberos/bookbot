"""
Statistics-helper functions for BookBot.
"""
from collections import Counter
from typing import Dict, List


# ---------- basic counts ----------
def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in *text*."""
    return len(text.split())


def count_characters(text: str) -> Dict[str, int]:
    """
    Return a mapping of every character (lower-cased) to its frequency
    in *text*.
    """
    return Counter(text.lower())


# ---------- helpers for reporting ----------
def get_sorted_char_list(char_dict: Dict[str, int]) -> List[Dict[str, int]]:
    """
    Convert *char_dict* into a list of
        {"char": <character>, "num": <count>}
    and return the list sorted from highest to lowest count.
    """
    char_list = [{"char": ch, "num": count} for ch, count in char_dict.items()]
    char_list.sort(key=lambda d: d["num"], reverse=True)
    return char_list
