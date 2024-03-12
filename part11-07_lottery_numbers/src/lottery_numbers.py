# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week_number: int, numbers: list):
        self.week_number = week_number
        self.numbers = numbers

    def number_of_hits(self, my_numbers: list):
        return sum([1 for number in my_numbers if number in self.numbers])

    def hits_in_place(self, my_numbers: list):
        return [number if number in self.numbers else -1 for number in my_numbers]
