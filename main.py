def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    word_count = get_wordcount(text)
    char_count = get_charcount(text)
    char_count_list = create_list_of_char_counts(char_count)
    print_report(book_path, word_count, char_count_list)

def print_report(book_path, word_count, char_count_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document.")
    print("\n")
    for d in char_count_list:
        print(f"The '{d["char"]}' character was found {d["count"]} times.")
    print("--- End report ---")
        
def sort_on(dict):
    return dict["count"]

def create_list_of_char_counts(char_count):
    char_count_list = []

    for k in char_count:
        single_char_dict = {}
        single_char_dict["char"] = k
        single_char_dict["count"] = char_count[k]
        char_count_list.append(single_char_dict)
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list

def get_charcount(text):
    char_count = {}

    for char in text:
        c = char.lower()
        if c.isalpha() == False:
            pass
        elif c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    return char_count

    
def get_wordcount(text):
    words = text.split()
    word_count = len(words)
    return word_count

def read_book(path):
    with open(path) as f:
        return f.read()

main()