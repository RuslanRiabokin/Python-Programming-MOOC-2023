def calculate_grade(total_points):
    if total_points <= 14:
        return 0
    elif 15 <= total_points <= 17:
        return 1
    elif 18 <= total_points <= 20:
        return 2
    elif 21 <= total_points <= 23:
        return 3
    elif 24 <= total_points <= 27:
        return 4
    else:
        return 5

if True: # поменять на False для проверки 
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points_data = input("Exam points:")
    course_info_file = input("Course information:")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points_data = "exam_points1.csv"
    course_info_file = "course1.txt"

names = {}
exercises = {}
exam_points = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        _id = parts[0]
        first_name = parts[1]
        last_name = parts[2].strip()
        names[_id] = (first_name, last_name)

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        _id = parts[0]
        e_values = [int(part) for part in parts[1:]]
        total_exercise_sum = sum(e_values)
        total_exercise_points = total_exercise_sum // 4
        exercises[_id] = total_exercise_sum

with open(exam_points_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        _id = parts[0]
        e_values = [int(part) for part in parts[1:]]
        total_exam_points = sum(e_values)
        if _id in exam_points:
            exam_points[_id] += total_exam_points
        else:
            exam_points[_id] = total_exam_points

# Moved this block up
course_info = {}
with open(course_info_file) as course_file:
    for line in course_file:
        key, value = line.strip().split(':')
        course_info[key.strip()] = value.strip()

course_name = course_info.get("name", "Course Name Not Found")
course_credits = course_info.get("study credits", "Credits Not Found")

# Вывод информации в файл results.txt
with open("results.txt", "w") as results_file:
    results_file.write(f"{course_name}, {course_credits} credits\n")
    results_file.write("=" * 38 + "\n")
    results_file.write(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade'}\n")

    for pic, (first_name, last_name) in names.items():
        if pic == "Introduction to Programming":
            continue
        if pic in exercises and pic in exam_points:
            total_points = (exercises[pic] // 4) + exam_points[pic]
            grade = calculate_grade(total_points)
            full_name = f"{first_name} {last_name}"
            results_file.write(f"{full_name:30}{exercises[pic]:<10}{exercises[pic] // 4:<10}{exam_points[pic]:<10}{total_points:<10}{grade}\n")

# Вывод информации в файл results.csv
with open("results.csv", "w") as csv_file:
    for pic, (first_name, last_name) in names.items():
        if pic == "Introduction to Programming":
            continue
        if pic in exercises and pic in exam_points:
            total_points = (exercises[pic] // 4) + exam_points[pic]
            grade = calculate_grade(total_points)
            csv_file.write(f"{pic};{first_name} {last_name};{grade}\n")

