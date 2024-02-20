from math import sqrt
# Write your solution here
while True:
    code = int(input("Please type in a number:"))
    if code == 0:
        break
    elif code < 0:
        print("Invalid number")
    else:
        print(sqrt(code))
print("Exiting...")