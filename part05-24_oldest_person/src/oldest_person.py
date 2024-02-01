# Write your solution here
def oldest_person(people: list):
    oldest = min(people, key=lambda person: person[1])
    return oldest[0]

