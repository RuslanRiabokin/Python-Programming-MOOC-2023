# Write your solution here
from string import ascii_letters, punctuation


def separate_characters(my_string: str):
    
    letters = ''
    punctuations = ''
    others = ''

    
    for char in my_string:
        if char in ascii_letters:
            letters += char
        elif char in punctuation:
            punctuations += char
        else:
            others += char

    return letters, punctuations, others