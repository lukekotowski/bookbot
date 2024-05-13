def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = get_character_count(text)
    generate_report(book_path, num_words, num_characters)

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    character_dict = {}
    for c in text:
        lc = c.lower()
        if lc in character_dict:
            character_dict[lc] += 1
        else:
            character_dict[lc] = 1
    return character_dict

def generate_report(book_path, num_words, num_characters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    dict_list = convert_to_list(num_characters)
    for dict in dict_list:
        if dict["character"].isalpha():
            print(f"The '{dict["character"]}' character was found {dict["number"]} times")

    print("--- End report ---")

def convert_to_list(dict):
    list = []
    for char, num in dict.items():
        new_dict = {"character": char, "number": num}
        list.append(new_dict)
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dict):
    return dict["number"]

main()
