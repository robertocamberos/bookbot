#!/usr/bin/env python3
"""
BookBot — quick book-statistics CLI

Usage:
    python3 main.py <path_to_book>
"""
import sys
from stats import count_words, count_characters, get_sorted_char_list


def usage_and_exit() -> None:
    """Print usage help and exit with status-code 1."""
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path: str) -> str:
    """Return the entire file at *path* as one string."""
    with open(path, encoding="utf-8") as f:
        return f.read()


def main() -> None:
    # ------------- CLI argument handling -------------
    if len(sys.argv) != 2:
        usage_and_exit()

    book_path = sys.argv[1]

    # ----------------- analysis ----------------------
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_counts = count_characters(text)
    sorted_chars = get_sorted_char_list(char_counts)

    # ------------------ report -----------------------
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in sorted_chars:
        ch = entry["char"]
        if ch.isalpha():  # skip digits, punctuation, spaces, …
            print(f"{ch}: {entry['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
