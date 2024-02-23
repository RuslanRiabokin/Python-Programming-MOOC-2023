# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    def get_sum(self):
        return sum(self.numbers) if self.numbers else 0

    def average(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0

def main():
    all_stats = NumberStats()
    even_stats = NumberStats()
    odd_stats = NumberStats()
    
    print("Please type in integer numbers:")
    while True:
        num = int(input())
        if num == -1:
            break
        all_stats.add_number(num)
        if num % 2 == 0:
            even_stats.add_number(num)
        else:
            odd_stats.add_number(num)

    print("Sum of numbers:", all_stats.get_sum())
    print("Mean of numbers:", all_stats.average())
    print("Sum of even numbers:", even_stats.get_sum())
    print("Sum of odd numbers:", odd_stats.get_sum())
main()