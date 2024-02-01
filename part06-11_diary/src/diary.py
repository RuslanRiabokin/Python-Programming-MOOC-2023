# Write your solution here
def add_entry(diary_file):
    entry = input("Diary entry: ")
    with open(diary_file, 'a') as file:
        file.write(entry + '\n')
    print("Diary saved")

def read_entries(diary_file):
    try:
        with open(diary_file, 'r') as file:
            entries = file.readlines()
            print("Entries:")
            for entry in entries:
                print(entry.strip())
    except FileNotFoundError:
        print("No entries found.")

def main():
    diary_file = "diary.txt"

    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        function = input("Function: ")

        if function == '1':
            add_entry(diary_file)
        elif function == '2':
            read_entries(diary_file)
        elif function == '0':
            print("Bye now!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 0.")


main()
