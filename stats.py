def sort_on(items):
    return items["num"]

def word_count(path):
    with open(path) as f:
        book_text = f.read()
        split_text = book_text.split()
        return len(split_text)

def character_count(path):
    with open(path) as f:
        char_dict = {}
        book_text = f.read().lower()
        split_text = book_text.split()
    for word in split_text:
        for char in word:
            if char.isalpha():
                if char not in char_dict:
                    char_dict[char] = 1
                else:
                    char_dict[char] += 1
    return char_dict
    
def book_report(path):
    words = word_count(path)
    char_dict = character_count(path)
    x = []
    y = []
    for k, v in char_dict.items():
        temp_dict = {}
        temp_dict["char"] = k
        temp_dict["num"] = v
        x.append(temp_dict)
    
    x.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dict in x:
        print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")