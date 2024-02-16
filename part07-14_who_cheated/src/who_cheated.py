import csv
from datetime import datetime, timedelta
def cheaters(start_times_file, submissions_file):
    cheaters_list = []

    # Read start times
    start_times = {}
    try:
        with open(start_times_file, 'r') as start_file:
            start_reader = csv.reader(start_file, delimiter=';')
            for row in start_reader:
                name, start_time = row
                start_times[name] = datetime.strptime(start_time, "%H:%M")
    except FileNotFoundError:
        print(f"Error: {start_times_file} not found.")
        return cheaters_list

    # Check submissions
    try:
        with open(submissions_file, 'r') as submissions:
            submissions_reader = csv.reader(submissions, delimiter=';')
            for row in submissions_reader:
                name, _, _, submission_time = row
                submission_time = datetime.strptime(submission_time, "%H:%M")

                # Check if submission time exceeds 3 hours from start time
                if (submission_time - start_times.get(name, submission_time)) > timedelta(hours=3):
                    if name not in cheaters_list:
                        cheaters_list.append(name)
                        print(f"{name} is a cheater!")
    except FileNotFoundError:
        print(f"Error: {submissions_file} not found.")
        return cheaters_list

    return cheaters_list


