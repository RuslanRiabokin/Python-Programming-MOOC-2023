words = ""

while True:
    word = input("Please type in a word:")

    if word == "end":
        break

    word_list = words.split()
    
    if word_list and word_list[-1] == word:
        break

    words += word + " "

print(words)
