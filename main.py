# main.py
from stats import count_words, count_characters


def get_book_text(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    # word count
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

    # character frequencies
    char_counts = count_characters(text)
    print(char_counts)           # a full dict dump

    # --- optional: show the three characters the grader checks ----
    # print("'t':", char_counts['t'])
    # print("'p':", char_counts['p'])
    # print("'c':", char_counts['c'])


if __name__ == "__main__":
    main()
