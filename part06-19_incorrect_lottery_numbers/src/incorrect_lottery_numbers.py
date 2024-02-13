import csv

def is_valid_line(line):
    try:
        week, numbers = line.strip().split(";")
        week_number = int(week.split()[-1])
        numbers_list = list(map(int, numbers.split(",")))
        if week_number < 1 or week_number > 52:
            return False
        if len(numbers_list) != 7:
            return False
        if any(num < 1 or num > 39 for num in numbers_list):
            return False
        if len(numbers_list) != len(set(numbers_list)):
            return False
        return True
    except:
        return False

def filter_incorrect():
    with open("lottery_numbers.csv", "r") as infile:
        with open("correct_numbers.csv", "w", newline='') as outfile:
            for line in infile:
                if is_valid_line(line):
                    outfile.write(line)


