def calculate_exercise_points(exercise_count):
    return exercise_count // 10

def calculate_grade(exam_score, exercise_points):
    total_points = exam_score + exercise_points

    if exam_score < 10:
        return 0  

    if 0 <= total_points <= 14:
        return 0
    elif 15 <= total_points <= 17:
        return 1
    elif 18 <= total_points <= 20:
        return 2
    elif 21 <= total_points <= 23:
        return 3
    elif 24 <= total_points <= 27:
        return 4
    elif 28 <= total_points <= 30:
        return 5
    else:
        return None  

def main():
    total_exam_score = 0
    total_exercise_points = 0
    passed_students = 0
    grades_distribution = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}

    while True:
        user_input = input("Exam points and exercises completed:")

        if not user_input:
            print("Statistics:")
            total_students = passed_students + grades_distribution[0]
            average_score = (total_exam_score + total_exercise_points) / max(total_students, 1)
            pass_percentage = (passed_students / max(total_students, 1)) * 100

            print(f"Points average: {average_score:.1f}")
            print(f"Pass percentage: {pass_percentage:.1f}")

            print("Grade distribution:")
            for grade, count in grades_distribution.items():
                stars = '*' * count
                print(f"  {grade}: {stars}")

            break

        exam_score, exercise_count = map(int, user_input.split())
        exercise_points = calculate_exercise_points(exercise_count)
        grade = calculate_grade(exam_score, exercise_points)

        total_exam_score += exam_score
        total_exercise_points += exercise_points

        if grade > 0:
            passed_students += 1
        grades_distribution[grade] += 1


main()
