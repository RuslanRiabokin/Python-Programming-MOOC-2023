class SimpleDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, other):
        return (self.day, self.month, self.year) == (other.day, other.month, other.year)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                return self.day < other.day
        return False

    def __gt__(self, other):
        return not (self.__lt__(other) or self.__eq__(other))

    def __add__(self, days):
        new_day = self.day + days
        new_month = self.month
        new_year = self.year

        while new_day > 30:
            new_day -= 30
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1

        return SimpleDate(new_day, new_month, new_year)

    def __sub__(self, other):
        days_in_self = self.year * 360 + self.month * 30 + self.day
        days_in_other = other.year * 360 + other.month * 30 + other.day
        return abs(days_in_self - days_in_other)
