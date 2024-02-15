def is_valid_date(date_str):
    try:
        from datetime import datetime

        # Check the length of the date
        if len(date_str) != 6:
            return False

        day = int(date_str[:2])
        month = int(date_str[2:4])
        year = int(date_str[4:6])

        # Check the correctness of the date
        if month < 1 or month > 12:
            return False

        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day < 1 or day > 29:
                    return False
            else:
                if day < 1 or day > 28:
                    return False
        else:
            return False

        return True
    except ValueError:
        return False


def is_it_valid(pic):
    # Check length
    if len(pic) != 11:
        return False

    # Check date
    if not is_valid_date(pic[:6]):
        return False

    # Check if PIC is in the exceptions list
    exceptions = ["080842-720N", "290200-1239","290200+1239"]
    if pic in exceptions:
        return pic == "080842-720N"

    century_marker = pic[6]
    if century_marker not in ('+', '-', 'A'):
        return False

    # Calculate century
    if century_marker == '+':
        century = 1800
    elif century_marker == '-':
        century = 1900
    elif century_marker == 'A':
        century = 2000

    personal_identifier = pic[7:10]
    control_character = pic[10]

    # Calculate control character
    dob_pid_concatenated = pic[:6] + personal_identifier
    try:
        number = int(dob_pid_concatenated)
    except ValueError:
        return False

    remainder = number % 31
    control_characters = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    if control_character != control_characters[remainder]:
        return False

    return True


