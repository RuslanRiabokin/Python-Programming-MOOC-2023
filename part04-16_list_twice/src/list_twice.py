# Write your solution here
my_list = []

while True:
    item = int(input("New item:"))
    my_list.append(item)
    if item == 0:
        print("Bye!")
        break
    print("The list now:", my_list)
    print("The list in order:",sorted(my_list))