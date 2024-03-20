# Write your solution here
def even_numbers(beginning: int, maximum: int):
    number = beginning
    if number % 2 == 0:

        while number <= maximum:
            yield number
            number += 2
    else:
        while number < maximum:
            yield number +1
            number += 2
