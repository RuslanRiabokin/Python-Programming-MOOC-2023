# Write your solution here
contacts = {}

def add_contact(name, number):
    global contacts
    if name in contacts:
        contacts[name].append(number)
    else:
        contacts[name] = [number]
    print("ok!")

def search_contact(name):
    global contacts
    if name in contacts:
        for number in contacts[name]:
            print(number)
    else:
        print("no number")

while True:
    command = input("command (1 search, 2 add, 3 quit):")

    if command == '1':
        name_to_search = input("name:")
        search_contact(name_to_search)
    elif command == '2':
        name_to_add = input("name:")
        number_to_add = input("number:")
        add_contact(name_to_add, number_to_add)
    elif command == '3':
        print("quitting...")
        break
    else:
        print("Invalid command. Please enter 1, 2, or 3.")
