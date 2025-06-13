# main.py
from stats import count_words, count_characters, get_sorted_char_list


def get_book_text(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def main() -> None:
    book_path = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)

    # word count section
    num_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # character count section
    char_counts = count_characters(text)
    sorted_chars = get_sorted_char_list(char_counts)

    print("--------- Character Count -------")
    for entry in sorted_chars:
        ch = entry["char"]
        if ch.isalpha():         # skip spaces, punctuation, etc.
            print(f"{ch}: {entry['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
