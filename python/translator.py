import sys

# Braille representations (dummy examples)
braille_dict = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    # Add all letters, digits, and symbols...
}

# Reverse dictionary for Braille to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

# Special symbols
braille_capital_sign = '.....O'
braille_number_sign = '..O...'
space_braille = '......'

def is_braille(input_string):
    """Check if input is Braille."""
    return all(c in ['O', '.'] for c in input_string)

def english_to_braille(text):
    """Convert English to Braille."""
    result = []
    for char in text:
        if char.isupper():
            result.append(braille_capital_sign)
            result.append(braille_dict[char.lower()])
        elif char.isdigit():
            result.append(braille_number_sign)
            result.append(braille_dict[char])
        elif char == ' ':
            result.append(space_braille)
        else:
            result.append(braille_dict[char])
    return ''.join(result)

def braille_to_english(braille_text):
    """Convert Braille to English."""
    result = []
    i = 0
    capital = False
    number_mode = False
    
    while i < len(braille_text):
        # Check for special signs
        if braille_text[i:i+6] == braille_capital_sign:
            capital = True
            i += 6
        elif braille_text[i:i+6] == braille_number_sign:
            number_mode = True
            i += 6
        elif braille_text[i:i+6] == space_braille:
            result.append(' ')
            i += 6
        else:
            # Regular Braille to character
            braille_char = braille_text[i:i+6]
            char = reverse_braille_dict[braille_char]
            if capital:
                char = char.upper()
                capital = False
            if number_mode and char.isalpha():
                # Convert from letter to number if needed
                number_mode = False
            result.append(char)
            i += 6
    
    return ''.join(result)

def main():
    input_string = sys.argv[1]
    
    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

if __name__ == '__main__':
    main()

