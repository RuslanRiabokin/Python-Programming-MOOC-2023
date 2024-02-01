def add_student(students, name):
    students[name] = []

def add_course(students, name, course):
    course_name, grade = course
    if name in students:
        existing_courses = students[name]
        if grade > 0:
            
            course_index = next((i for i, (c, _) in enumerate(existing_courses) if c == course_name), None)
            if course_index is not None:
                
                existing_courses[course_index] = (course_name, max(existing_courses[course_index][1], grade))
            else:
                students[name].append(course)
    else:
        print(f"{name}: no such person in the database")



def print_student(students, name):
    if name in students:
        print(f"{name}:")
        if students[name]:
            print(f" {len(students[name])} completed courses:")
            total_grade = 0
            for course, grade in students[name]:
                print(f"  {course} {grade}")
                total_grade += grade
            average_grade = total_grade / len(students[name])
            print(f" average grade {average_grade:.1f}")
        else:
            print(" no completed courses")  
    else:
        print(f"{name}: no such person in the database")

def summary(students):
    if not students:
        print("Database is empty.")
        return

    print(f"students {len(students)}")

    most_courses_student = max(students, key=lambda name: len(set(c[0] for c in students[name])))
    most_courses_count = len(set(c[0] for c in students[most_courses_student]))
    print(f"most courses completed {most_courses_count} {most_courses_student}")

    best_average_student = max(students, key=lambda name: sum(grade for _, grade in students[name]) / len(set(c[0] for c in students[name])) if students[name] else 0)
    best_average_grade = sum(grade for _, grade in students[best_average_student]) / len(set(c[0] for c in students[best_average_student])) if students[best_average_student] else 0
    print(f"best average grade {best_average_grade:.1f} {best_average_student}")