# Write your solution here
age = int(input("What is your age?"))
if not 5 > age <= 100:
    print(f"Ok, you're {age} years old")
elif age >= 0 and age < 5:
    print("I suspect you can't write quite yet...")
elif age < 0:
    print("That must be a mistake")