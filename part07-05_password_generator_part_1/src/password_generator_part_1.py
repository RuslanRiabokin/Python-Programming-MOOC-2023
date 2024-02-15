# Write your solution here
from random import choice
from string import ascii_lowercase

def generate_password(length: int) -> str:
    # Создаем пароль, выбирая случайные символы из строчных букв от 'a' до 'z'
    password = ''.join(choice(ascii_lowercase) for _ in range(length))
    return password
