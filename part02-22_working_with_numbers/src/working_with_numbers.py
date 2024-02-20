sum_numbers = 0
attempts = 0
positive_numbers = 0
negative_numbers = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input("Number:"))

    if number == 0:
        print("... the program asks for numbers")
        break

    attempts += 1
    sum_numbers += number

    if number > 0:
        positive_numbers += 1
    elif number < 0:
        negative_numbers += 1

print("Numbers typed in", attempts)
print("The sum of the numbers is", sum_numbers)
print("The mean of the numbers is", sum_numbers / attempts)
print("Positive numbers", positive_numbers)
print("Negative numbers", negative_numbers)
