# Write your solution here
names = input("Whom should I sign this to:")
open_txt = input("Where shall I save it:")
with open(f"{open_txt}", "w") as my_file:
    my_file.write(f"Hi {names}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

