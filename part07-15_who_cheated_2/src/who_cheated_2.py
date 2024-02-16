import csv
from datetime import datetime, timedelta

def final_points(start_times_file, submissions_file):
    # Read start times
    start_times = {}
    with open(start_times_file, 'r') as start_file:
        start_reader = csv.reader(start_file, delimiter=';')
        for row in start_reader:
            name, start_time = row
            start_times[name] = datetime.strptime(start_time, "%H:%M")
    
    # Initialize dictionary to store final points
    final_points_dict = {}
    
    # Read submissions
    with open(submissions_file, 'r') as submissions:
        submissions_reader = csv.reader(submissions, delimiter=';')
        for row in submissions_reader:
            name, task, points, submission_time = row
            task = int(task)
            points = int(points)
            submission_time = datetime.strptime(submission_time, "%H:%M")
            
            # Check if submission is within 3 hours of start time
            if (submission_time - start_times.get(name, submission_time)) <= timedelta(hours=3):
                # Update final points if submission has higher points for the task
                if name not in final_points_dict:
                    final_points_dict[name] = {}
                if task not in final_points_dict[name] or points > final_points_dict[name][task]:
                    final_points_dict[name][task] = points
    
    # Calculate total points for each student
    for name, tasks in final_points_dict.items():
        final_points_dict[name] = sum(tasks.values())
    
    return final_points_dict
