# Write your solution here
from fractions import Fraction


def fractionate(amount: int):
    # Создаем список для хранения дробей
    fractions_list = []

    # Создаем рациональное число 1
    one = Fraction(1)

    # Делим 1 на количество дробей и добавляем результат в список
    for _ in range(amount):
        fractions_list.append(one / amount)

    return fractions_list