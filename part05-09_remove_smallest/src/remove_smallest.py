# Write your solution here
def remove_smallest(numbers: list):
    min_number = min(numbers)

    if min_number in numbers:
        numbers.remove(min_number)
        