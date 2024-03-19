class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here
def most_goals(players):
    return max(players, key=lambda player: player.goals).name

def most_points(players):
    max_player = max(players, key=lambda player: player.goals + player.passes)
    return max_player.name, max_player.number

def least_minutes(players):
    return min(players, key=lambda player: player.minutes)