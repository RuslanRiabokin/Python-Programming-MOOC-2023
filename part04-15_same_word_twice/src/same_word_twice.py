# Write your solution here
my_list = []

while True:
    word = input("Word:")
    if my_list.count(word) > 0:
        break
    my_list.append(word)

print(f"You typed in {len(my_list)} different words")

