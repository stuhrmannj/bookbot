import sys
from stats import *

#get the contents of the book from the filepath of the book
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    
    word_count = count_words(book)
    
    book_char_dict = char_count(book)
    sorted_char_count = sorted_list_char_dict(book_char_dict)

    #report output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for each_char in sorted_char_count:
        print(f"{each_char["char"]}: {each_char["count"]}")
    print("============= END ===============")

main()
