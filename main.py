# The with block will automatically close the file when the block is exited, cleaning up resources.

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

main()
