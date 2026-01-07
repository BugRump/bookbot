import sys
from stats import sort_on, word_count, character_count, book_report

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_report(sys.argv[1])

main()