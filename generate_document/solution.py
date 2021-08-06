# document: Will
# chars: Wil

def generate_document(available_characters, document):
    char_dict = {}

    for character in available_characters:
        if character in char_dict:
            char_dict[character] = char_dict[character] + 1
        else:
            char_dict[character] = 1

    
    for letter in document:
        if letter not in char_dict or char_dict[letter] == 0:
            return False

        char_dict[letter] = char_dict[letter] - 1

    return True