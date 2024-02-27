# Write your solution after the class Car
# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

def fastest_car(cars: list) -> str:
    fastest = max(cars, key=lambda x: x.top_speed)
    return fastest.make