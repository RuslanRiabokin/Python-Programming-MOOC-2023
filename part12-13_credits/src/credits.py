from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(course_attempts):
    return reduce(lambda total_credits, course_attempt: total_credits + course_attempt.credits, course_attempts, 0)

def sum_of_passed_credits(course_attempts):
    # Filter course attempts with grade 1 or above
    passed_attempts = filter(lambda attempt: attempt.grade >= 1, course_attempts)
    # Sum up the credits of passed attempts
    return reduce(lambda total_credits, course_attempt: total_credits + course_attempt.credits, passed_attempts, 0)

def average(course_attempts):
    # Filter course attempts with grade 1 or above and store them in a list
    passed_attempts = list(filter(lambda attempt: attempt.grade >= 1, course_attempts))
    # Count the number of passed attempts
    num_passed_attempts = len(passed_attempts)
    
    # If there are no passed attempts, return 0
    if num_passed_attempts == 0:
        return 0
    
    # Calculate the sum of grades for passed attempts
    sum_of_grades = reduce(lambda total, attempt: total + attempt.grade, passed_attempts, 0)
    
    # Calculate the average grade
    average_grade = sum_of_grades / num_passed_attempts
    
    return average_grade
