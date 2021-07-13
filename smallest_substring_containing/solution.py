def smallestSubstringContaining(bigString, smallString):
    string_dict = {}
    needed_chars = {}
    characters_found = {}
    substring = ''

    for letter in smallString:
        if letter in needed_chars:
            needed_chars[letter] = needed_chars[letter] + 1
        else:
            needed_chars[letter] = 1

    for index, letter in enumerate(bigString):
        if letter not in needed_chars:
            continue

        if needed_chars[letter] > 1:
            if (
                letter in string_dict
                and len(string_dict[letter]) == needed_chars[letter]
            ):
                updated_dict = string_dict[letter]
                updated_dict.append(index)
                updated_dict = updated_dict[1:]
                string_dict[letter] = updated_dict
            elif (
                letter in string_dict
                and len(string_dict[letter]) < needed_chars[letter]
            ):
                updated_dict = string_dict[letter]
                updated_dict.append(index)
                string_dict[letter] = updated_dict
                characters_found[letter] = characters_found[letter] + 1
            else:
                string_dict[letter] = [index]
                characters_found[letter] = 1
        else:
            string_dict[letter] = index
            characters_found[letter] = 1

        if characters_found.keys() == needed_chars.keys() and sum(characters_found.values()) == sum(needed_chars.values()):
            new_substring = calculate_substring(string_dict, bigString)
            
            print(new_substring)
            if not substring or len(new_substring) < len(substring):
                substring = new_substring

    return substring


def calculate_substring(string_dict, big_string):
    smallest_index = float("inf")
    largest_index = 0

    for key, value in string_dict.items():
        if isinstance(value, int):
            smallest_index = min(value, smallest_index)
            largest_index = max(value, largest_index)
        else:
            smallest_index = min(value + [smallest_index])
            largest_index = max(value + [largest_index])
    
    return big_string[smallest_index:largest_index+1]
