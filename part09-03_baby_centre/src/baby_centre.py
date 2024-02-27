class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
class BabyCentre:
    def __init__(self):
        self.number_of_weigh_ins = 0

    def weigh(self, person: Person):
        # increase the count of weigh-ins
        self.number_of_weigh_ins += 1
        # return the weight of the person passed as an argument
        return person.weight

    def feed(self, person: Person):
        # increase the weight of the person by one
        person.weight += 1

    def weigh_ins(self):
        # return the total number of weigh-ins performed
        return self.number_of_weigh_ins
if __name__ == "__main__":
    baby_centre = BabyCentre()