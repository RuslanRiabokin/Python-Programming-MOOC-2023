import csv
from datetime import datetime, timedelta

def cheaters(start_times_file, submissions_file):
    cheaters_list = []
    
    # Dictionary to store start times of exams
    start_times = {}
    with open(start_times_file) as start_file:
        start_reader = csv.reader(start_file, delimiter=";")
        for row in start_reader:
            name, start_time_str = row
            start_time = datetime.strptime(start_time_str, "%H:%M")
            start_times[name] = start_time
    
    # Check submissions for cheaters
    with open(submissions_file) as submissions_file:
        submissions_reader = csv.reader(submissions_file, delimiter=";")
        for row in submissions_reader:
            name, task, points, submission_time_str = row
            submission_time = datetime.strptime(submission_time_str, "%H:%M")
            start_time = start_times.get(name)
            if start_time:
                # Calculate time difference
                time_difference = submission_time - start_time
                # Check if time difference is over 3 hours
                if time_difference > timedelta(hours=3):
                    cheaters_list.append(name)
    
    return cheaters_list

