class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = []
        self.__persons[name].append(number)

    def get_entry(self, name: str):
        return self.__persons.get(name)

    def search_by_number(self, number: str):
        for name, numbers in self.__persons.items():
            if number in numbers:
                return name
        return None

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search by name")
        print("3 search by number")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search_by_name(self):
        name = input("name: ")
        numbers = self.__phonebook.get_entry(name)
        if numbers is None:
            print("entry not found") 
            return 
        for number in numbers:
            print(number)

    def search_by_number(self):
        number = input("number: ")
        name = self.__phonebook.search_by_number(number)
        if name is None:
            print("unknown number")
        else:
            print(name)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search_by_name()
            elif command == "3":
                self.search_by_number()
            else:
                self.help()

# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
