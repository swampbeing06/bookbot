def get_num_words(file_contents):
    words = file_contents.split()
    word_count = 0
    for i in words: 
        word_count += 1
    return word_count


def get_character_count(file_contents):
    characters = {}
    for i in file_contents:
        lowercase_letters = i.lower()
        if lowercase_letters in characters:
            characters[lowercase_letters] = characters[lowercase_letters] + 1
        else:
            characters[lowercase_letters] = 1
    return characters
            

def report(characters):
    character_list = []
    for char, count in characters.items():
        if char.isalpha():
            character_list.append({"char": char, "count": count})

    def sort_on(character_count):
        return character_count["count"]
    character_list.sort(key=sort_on, reverse=True)

    return character_list
