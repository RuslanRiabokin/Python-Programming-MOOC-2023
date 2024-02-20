# Write your solution here
correct_pin = "4321"
attempts = 0

while True:
    user_input = input("PIN: ")
    attempts += 1

    if user_input == correct_pin:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")
