import urllib.request
import json
import ssl
import math

def retrieve_course(course_name: str):
    context = ssl._create_unverified_context()
    address = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    request = urllib.request.urlopen(address, context=context)
    data = json.load(request)

    weeks = len(data)
    students = max([week['students'] for week in data.values()])
    hours = sum([week['hour_total'] for week in data.values()])
    exercises = sum([week['exercise_total'] for week in data.values()])

    hours_average = math.floor(hours / students)
    exercises_average = math.floor(exercises / students)

    return {
        'weeks': weeks,
        'students': students,
        'hours': hours,
        'hours_average': hours_average,
        'exercises': exercises,
        'exercises_average': exercises_average
    }

