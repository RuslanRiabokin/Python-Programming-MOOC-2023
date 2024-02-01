if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
names = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        _id = parts[0]
        first_name = parts[1]
        last_name = parts[2].strip()  
        names[_id] = (first_name, last_name)

salaries = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue

        _id = parts[0]
        e_values = [int(part) for part in parts[1:]]
        total_salary = sum(e_values)

        salaries[_id] = total_salary


for pic, (first_name, last_name) in names.items():
    if pic in salaries:
        salary = salaries[pic]
        print(f"{first_name} {last_name} {salary}")
    else:
        print(f"{first_name} {last_name} 0")
