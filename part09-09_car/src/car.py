# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__petrol_tank = 0
        self.__odometer_reading = 0

    def fill_up(self):
        self.__petrol_tank = 60

    def drive(self, km):
        petrol_needed = km
        if petrol_needed > self.__petrol_tank:
            petrol_needed = self.__petrol_tank
        self.__odometer_reading += petrol_needed
        self.__petrol_tank -= petrol_needed

    def __str__(self):
        return f"Car: odometer reading {self.__odometer_reading} km, petrol remaining {self.__petrol_tank} litres"

