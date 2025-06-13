# main.py
from stats import count_words          # ← required import line

def get_book_text(path: str) -> str:
    """Read the entire file and return it as one big string."""
    with open(path, encoding="utf-8") as f:
        return f.read()


def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()
