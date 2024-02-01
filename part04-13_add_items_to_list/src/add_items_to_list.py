# Write your solution here
my_list = []
items = int(input("How many items: "))
counter = 1

while counter <= items:
    item = int(input(f"Item {counter}: "))
    my_list.append(item)
    counter += 1

print(my_list)
