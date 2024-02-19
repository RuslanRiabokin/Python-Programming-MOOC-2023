# Write your solution here
import re

def change_case(orig_string: str) -> str:
    """
    Change the case of characters in the string.
    """
    return orig_string.swapcase()

def split_in_half(orig_string: str) -> tuple:
    """
    Split the string into two halves.
    """
    length = len(orig_string)
    half_length = length // 2
    return orig_string[:half_length], orig_string[half_length:]

def remove_special_characters(orig_string: str) -> str:
    """
    Remove special characters from the string.
    """
    return re.sub(r'[^A-Za-z0-9\s]', '', orig_string)

# Test the functions
if __name__ == "__main__":
    my_string = "Well hello there!"
    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)
    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)
