# Write your solution here
def read_input(prompt, a, b):
    while True:
        try:
            number = int(input(prompt))
            if a <= number <= b:
                return number
            else:
                print(f"You must type in an integer between {a} and {b}")
        except ValueError:
            print(f"You must type in an integer between {a} and {b}")

