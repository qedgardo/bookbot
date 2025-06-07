from stats import get_book_words, get_book_characters, get_dict_report
import sys
# The with block will automatically close the file when the block is exited, cleaning up resources.
def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    # print(book_text)
    num_words = get_book_words(book_text)
    characters = get_book_characters(book_text)
    # print(characters)
    report = get_dict_report(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in report:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")
main()
