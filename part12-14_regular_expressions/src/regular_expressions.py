# Write your solution here
import re

def is_dotw(my_string: str) -> bool:
    pattern = r'\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b'
    return bool(re.search(pattern, my_string))

def all_vowels(my_string: str) -> bool:
    pattern = r'^[aeiouAEIOU]+$'
    return bool(re.match(pattern, my_string))

def time_of_day(my_string: str) -> bool:
    pattern = r'^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'
    return bool(re.match(pattern, my_string))
