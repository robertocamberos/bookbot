# main.py
def get_book_text(path):
    """Read the entire file and return it as one string."""
    with open(path, encoding="utf-8") as f:
        return f.read()


def strip_gutenberg_header_footer(text):
    """
    Return only the actual book contents.
    Lines outside the *** START … and *** END … markers are removed
    so the word-count matches the exercise’s expected total.
    """
    start_tag = "*** START"
    end_tag = "*** END"

    start = text.find(start_tag)
    end = text.find(end_tag)

    if start != -1:
        # skip the marker line itself
        text = text[start:]
        first_newline = text.find("\n")
        if first_newline != -1:
            text = text[first_newline + 1 :]

    if end != -1:
        text = text[:end]

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
