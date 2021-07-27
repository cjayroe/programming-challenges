# AAAAAAAAAAAAABBCCCCDD
# 9A4A2B4C2D

def run_length_encocding(decoded_string):
    previous_letter = ''
    letter_count = 0
    encoded_string = ''

    for letter in decoded_string:
        if previous_letter and previous_letter != letter or letter_count == 9:
            encoded_string += f'{letter_count}{previous_letter}'
            previous_letter = letter
            letter_count = 1
            continue

        if letter == previous_letter:
            letter_count += 1
            previous_letter = letter
            continue
        
        letter_count += 1
        previous_letter = letter
    
    if letter_count > 0:
        encoded_string += f'{letter_count}{previous_letter}'

    return encoded_string