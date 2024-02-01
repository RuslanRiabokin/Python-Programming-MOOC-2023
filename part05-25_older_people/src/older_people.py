# Write your solution here
def older_people(people: list, year: int):
    older_people_list = [person[0] for person in people if person[1] < year]
    return older_people_list
