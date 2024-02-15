# Write your solution here
from random import choice

def roll(die: str) -> int:
    if die == "A":
        return choice([3, 3, 3, 3, 3, 6])
    elif die == "B":
        return choice([2, 2, 2, 5, 5, 5])
    elif die == "C":
        return choice([1, 4, 4, 4, 4, 4])
    else:
        raise ValueError("Invalid die type")

def play(die1: str, die2: str, times: int) -> tuple:
    wins1 = 0
    wins2 = 0
    draws = 0

    for _ in range(times):
        result1 = roll(die1)
        result2 = roll(die2)

        if result1 > result2:
            wins1 += 1
        elif result2 > result1:
            wins2 += 1
        else:
            draws += 1

    return wins1, wins2, draws


