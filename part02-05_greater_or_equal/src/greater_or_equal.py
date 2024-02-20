# Write your solution here
number = int(input("Please type in the first number: "))
number2 = int(input("Please type in another number:"))
if number > number2:
    print("The greater number was:", number)
elif number2 > number:
    print("The greater number was:", number2)
else:
    print("The numbers are equal!")