# Write your solution here
from datetime import datetime

day = int(input("Day:"))
month = int(input("Month:"))
year = int(input("Year:"))

date_time = datetime(1999, 12, 31)  # "Eve of the new millennium"

how_old = datetime(year, month, day)

if how_old <= date_time:  
    difference = date_time - how_old
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
