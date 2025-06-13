# main.py
def get_book_text(path):
    """Read the entire file and return it as one string."""
    with open(path, encoding="utf-8") as f:
        return f.read()


def strip_gutenberg_header_footer(text: str) -> str:
    """
    Keep content between the official START/END markers *inclusive of the line
    right after START* (that’s how Boot.dev’s reference count is computed).
    """
    start_token = "*** START OF THE PROJECT GUTENBERG"
    end_token   = "*** END OF THE PROJECT GUTENBERG"

    start_idx = text.find(start_token)
    if start_idx != -1:
        # jump to the newline *after* the START marker
        start_idx = text.find("\n", start_idx) + 1
        text = text[start_idx:]

    end_idx = text.find(end_token)
    if end_idx != -1:
        text = text[:end_idx]

    return text


def count_words(text):
    """Return the number of whitespace-separated words in *text*."""
    return len(text.split())


def main():
    book_path = "books/frankenstein.txt"
    full_text = get_book_text(book_path)
    core_text = strip_gutenberg_header_footer(full_text)
    num_words = count_words(core_text)
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()
