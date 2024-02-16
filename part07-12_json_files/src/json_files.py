# Write your solution here
import json

def print_persons(filename: str):
    with open(filename, 'r') as file:
        data = json.load(file)
        for person in data:
            name = person['name']
            age = person['age']
            hobbies = ', '.join(person['hobbies'])
            print(f"{name} {age} years ({hobbies})")
