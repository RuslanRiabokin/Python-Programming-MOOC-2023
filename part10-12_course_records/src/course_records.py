class StudyTracker:
    def __init__(self):
        self.__courses = {}

    def add_course(self, course: str, grade: int, credits: int):
        if course not in self.__courses:
            self.__courses[course] = {'grade': grade, 'credits': credits}
        else:
            # Update grade only if the new grade is higher
            if grade > self.__courses[course]['grade']:
                self.__courses[course]['grade'] = grade

    def get_course_data(self, course: str):
        if course in self.__courses:
            return f"{course} ({self.__courses[course]['credits']} cr) grade {self.__courses[course]['grade']}"
        else:
            return "no entry for this course"

    def get_statistics(self):
        total_courses = len(self.__courses)
        total_credits = sum(course['credits'] for course in self.__courses.values())
        mean_grade = sum(course['grade'] for course in self.__courses.values()) / total_courses if total_courses > 0 else 0

        grade_distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for course in self.__courses.values():
            grade_distribution[course['grade']] += 1

        statistics = f"{total_courses} completed courses, a total of {total_credits} credits\nmean {mean_grade:.1f}\ngrade distribution"
        for grade, count in grade_distribution.items():
            if count > 0:
                statistics += f"\n{grade}: {'x' * count}" if grade != 3 else f"\n{grade}:"
        return statistics

class StudyTrackerApplication:
    def __init__(self):
        self.__study_tracker = StudyTracker()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__study_tracker.add_course(course, grade, credits)

    def get_course_data(self):
        course = input("course: ")
        data = self.__study_tracker.get_course_data(course)
        print(data)

    def get_statistics(self):
        statistics = self.__study_tracker.get_statistics()
        print(statistics)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.get_statistics()
            else:
                self.help()

# when testing, no code should be outside application except the following:
application = StudyTrackerApplication()
application.execute()
