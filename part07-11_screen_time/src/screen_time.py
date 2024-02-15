from datetime import datetime, timedelta

def write_screen_time_data(filename, start_date, days, screen_time_data):
    with open(filename, 'w') as file:
        # Write time period
        end_date = start_date + timedelta(days=days - 1)
        file.write(f"Time period: {start_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n")

        # Calculate total and average minutes
        total_minutes = sum(sum(day) for day in screen_time_data)
        average_minutes = total_minutes / days

        # Write total and average minutes
        file.write(f"Total minutes: {total_minutes}\n")
        file.write(f"Average minutes: {average_minutes}\n")

        # Write screen time for each day
        for i in range(days):
            date = start_date + timedelta(days=i)
            screen_time = '/'.join(str(minutes) for minutes in screen_time_data[i])
            file.write(f"{date.strftime('%d.%m.%Y')}: {screen_time}\n")

def get_user_input():
    filename = input("Enter filename: ")
    start_date_str = input("Enter starting date (in format DD.MM.YYYY): ")
    days = int(input("Enter how many days: "))
    start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
    screen_time_data = []
    for i in range(days):
        screen_time = input(f"Screen time {start_date.strftime('%d.%m.%Y')}: ").split()
        screen_time = [int(time) for time in screen_time]
        screen_time_data.append(screen_time)
        start_date += timedelta(days=1)
    return filename, start_date_str, days, screen_time_data

# Get user input
filename, start_date_str, days, screen_time_data = get_user_input()

# Write data to file
write_screen_time_data(filename, datetime.strptime(start_date_str, "%d.%m.%Y"), days, screen_time_data)
