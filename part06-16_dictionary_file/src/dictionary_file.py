def read_dictionary_from_file():
    try:
        with open("dictionary.txt", "r") as file:
            lines = file.readlines()
        dictionary = {}
        for line in lines:
            finnish, english = line.strip().split(" - ")
            dictionary[finnish] = english
        return dictionary
    except FileNotFoundError:
        return {}

def write_dictionary_to_file(dictionary):
    with open("dictionary.txt", "w") as file:
        for finnish, english in dictionary.items():
            file.write(f"{finnish} - {english}\n")

def add_word(dictionary):
    finnish_word = input("The word in Finnish: ")
    english_word = input("The word in English: ")
    dictionary[finnish_word] = english_word
    write_dictionary_to_file(dictionary)
    print("Dictionary entry added")

def search_word(dictionary):
    search_term = input("Search term: ")
    found_entries = [f"{finnish} - {english}" for finnish, english in dictionary.items() if search_term.lower() in finnish.lower() or search_term.lower() in english.lower()]
    if found_entries:
        print("\n".join(found_entries))
    else:
        print("No matching entries found")




def main():
    dictionary = read_dictionary_from_file()

    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        function_choice = input("Function: ")

        if function_choice == "1":
            add_word(dictionary)
        elif function_choice == "2":
            search_word(dictionary)
        elif function_choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

main()
