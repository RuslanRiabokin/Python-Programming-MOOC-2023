# Get three letters from the user
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

# Compare the letters to find the one in the middle
if (letter1 < letter2 < letter3) or (letter3 < letter2 < letter1):
    print(f"The letter in the middle is {letter2}")
elif (letter2 < letter1 < letter3) or (letter3 < letter1 < letter2):
    print(f"The letter in the middle is {letter1}")
else:
    print(f"The letter in the middle is {letter3}")
