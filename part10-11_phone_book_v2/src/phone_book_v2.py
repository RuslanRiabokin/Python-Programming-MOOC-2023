class Person:
    def __init__(self, name):
        self.__name = name
        self.__numbers = []
        self.__address = None
    
    def name(self):
        return self.__name
    
    def add_number(self, number):
        self.__numbers.append(number)
    
    def numbers(self):
        return self.__numbers
    
    def add_address(self, address):
        self.__address = address
    
    def address(self):
        return self.__address

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        return self.__persons.get(name)

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)
        if person is None:
            print("number unknown")
        else:
            numbers = person.numbers()
            if not numbers:
                print("number unknown")
            else:
                print(numbers)
            if person.address():
                print(person.address())
            else:
                print("address unknown")
        if person is None:
            print("address unknown")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
