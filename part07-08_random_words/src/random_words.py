# Write your solution here
import random

def words(n: int, beginning: str) -> list:
    with open('words.txt', 'r') as file:
        words_list = [word.strip() for word in file.readlines() if word.strip().startswith(beginning)]
    
    if len(words_list) < n:
        raise ValueError(f"Not enough words starting with '{beginning}' in the file.")
    
    return random.sample(words_list, n)

