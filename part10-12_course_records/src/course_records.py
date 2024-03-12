class StudyTracker:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name in self.__courses:
            if grade > self.__courses[name]['grade']:
                self.__courses[name]['grade'] = grade
        else:
            self.__courses[name] = {'grade': grade, 'credits': credits}

    def get_course_data(self, name: str):
        if name in self.__courses:
            course_info = self.__courses[name]
            return f"{name} ({course_info['credits']} cr) grade {course_info['grade']}"
        else:
            return "no entry for this course"

    def get_statistics(self):
        total_courses = len(self.__courses)
        total_credits = sum(course['credits'] for course in self.__courses.values())
        mean_grade = sum(course['grade'] for course in self.__courses.values()) / total_courses if total_courses > 0 else 0
        grade_distribution = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
        for course in self.__courses.values():
            grade_distribution[course['grade']] += 1

        statistics = f"{total_courses} completed courses, a total of {total_credits} credits\n"
        statistics += f"mean {mean_grade:.1f}\n"
        statistics += "grade distribution\n"
        for grade, count in grade_distribution.items():
            statistics += f"{grade}: {count * 'x'}\n"
        return statistics

class StudyTrackerApplication:
    def __init__(self):
        self.__tracker = StudyTracker()

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__tracker.add_course(name, grade, credits)

    def get_course_data(self):
        name = input("course: ")
        course_info = self.__tracker.get_course_data(name)
        print(course_info)

    def get_statistics(self):
        statistics = self.__tracker.get_statistics()
        print(statistics)

    def execute(self):
        while True:
            print("")
            print("1 add course")
            print("2 get course data")
            print("3 statistics")
            print("0 exit")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.get_statistics()

# when testing, no code should be outside application except the following:
application = StudyTrackerApplication()
application.execute()
