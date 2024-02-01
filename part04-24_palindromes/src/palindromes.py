# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]

while True:
    enter_text = input("Please type in a palindrome: ")

    if palindromes(enter_text):
        print(f"{enter_text} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

