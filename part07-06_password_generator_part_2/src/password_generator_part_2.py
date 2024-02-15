from random import choice
from string import ascii_lowercase, digits, punctuation


def generate_strong_password(length: int, include_numbers: bool, include_special_chars: bool) -> str:
    
    char_set = ascii_lowercase
    
   
    if include_numbers:
        char_set += digits
    
    
    if include_special_chars:
        char_set += "!?=+-()#"
    
    
    password = choice(ascii_lowercase)

    
    length_adjusted = length - 1

    
    if include_numbers:
        password += choice(digits)
        length_adjusted -= 1

    
    if include_special_chars:
        password += choice("!?=+-()#")
        length_adjusted -= 1

    
    password += ''.join(choice(char_set) for _ in range(length_adjusted))

    return password

