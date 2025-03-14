import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]

from stats import get_num_words
from stats import get_character_count
from stats import report

def main():

    with open(file_path) as f:
        file_contents = f.read()

    word_count = get_num_words(file_contents)
    characters = get_character_count(file_contents)
    character_list = report(characters)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print(f"--------- Character Count -------")
    for i in character_list:
        print(f"{i["char"]}: {i["count"]}")
    print(f"============= END ===============")


main()