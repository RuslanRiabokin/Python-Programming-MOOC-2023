year = int(input("Year:"))
n_year = year
while True:
    n_year += 1
    if (n_year % 4 == 0 and n_year % 100 != 0) or n_year % 400 == 0:
        break;

print(f"The next leap year after {year} is {n_year}")
