# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date

def list_years(dates: list):
    years_ = [d.year for d in dates] 
    return sorted(years_)
