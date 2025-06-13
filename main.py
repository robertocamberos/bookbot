def get_book_text(path):
  """Return the entire text of the file at *path* as one big string."""
  with open(path, encoding="utf-8") as f:
    return f.read()
  
def main():
  book_path = "books/frankenstein.txt" # relative to the project root 
  text = get_book_text(book_path)
  print(text) # prints the whole novel

if __name__ == "__main__":
  main()