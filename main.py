def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    num_characters = get_character_count(text)
    print(num_characters)

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

main()
