from operator import attrgetter
class Room:
    def __init__(self):
        self.persons = []

    def add(self, person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        if self.is_empty():
            return None
        else:
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {sum(person.height for person in self.persons)} cm")
            for person in self.persons:
                print(person)

    def shortest(self):
        if self.is_empty():
            return None
        else:
            shortest_person = min(self.persons, key=attrgetter('height'))
            return shortest_person

    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person:
            self.persons.remove(shortest_person)
            return shortest_person
        else:
            return None


class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"

