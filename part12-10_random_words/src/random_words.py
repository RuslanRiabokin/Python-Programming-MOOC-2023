# Write your solution here:
import random

def word_generator(characters: str, length: int, amount: int):
    return (''.join(random.choices(characters, k=length)) for _ in range(amount))