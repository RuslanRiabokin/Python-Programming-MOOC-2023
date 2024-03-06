class Money:
    def __init__(self, euros: int, cents: int):
        self.__total_cents = euros * 100 + cents

    def __str__(self):
        return f"{self.__total_cents // 100}.{self.__total_cents % 100:02d} eur"

    def __eq__(self, another):
        return self.__total_cents == another.__total_cents

    def __lt__(self, another):
        return self.__total_cents < another.__total_cents

    def __ne__(self, another):
        return not self.__eq__(another)

    def __gt__(self, another):
        return self.__total_cents > another.__total_cents

    def __add__(self, other):
        total_cents = self.__total_cents + other.__total_cents
        new_euros = total_cents // 100
        new_cents = total_cents % 100
        return Money(new_euros, new_cents)

    def __sub__(self, other):
        if self.__total_cents < other.__total_cents:
            raise ValueError("a negative result is not allowed")
        total_cents = self.__total_cents - other.__total_cents
        new_euros = total_cents // 100
        new_cents = total_cents % 100
        return Money(new_euros, new_cents)
