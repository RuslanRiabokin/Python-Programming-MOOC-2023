class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"


def accepted(attempts: list):
    return list(filter(lambda accepted : accepted.grade >=1, attempts))

def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda accepteds: accepteds.grade == grade, attempts))

def passed_students(attempts: list, course: str):
    # Filter attempts for the given course
    filtered_attempts = filter(lambda attempt: attempt.course_name == course, attempts)
    # Filter the attempts where grade is higher than 0
    passed_attempts = filter(lambda attempt: attempt.grade > 0, filtered_attempts)
    # Map to get student names
    student_names = map(lambda attempt: attempt.student_name, passed_attempts)
    # Sort the student names alphabetically
    return sorted(student_names)