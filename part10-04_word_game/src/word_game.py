# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return 0  

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = 'aeiouAEIOU'
        player1_vowels = sum(1 for char in player1_word if char in vowels)
        player2_vowels = sum(1 for char in player2_word if char in vowels)

        if player1_vowels > player2_vowels:
            return 1
        elif player1_vowels < player2_vowels:
            return 2
        else:
            return 0  

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_choice: str, player2_choice: str):
        choices = ['rock', 'paper', 'scissors']

        if player1_choice not in choices and player2_choice not in choices:
            return 0  # Both inputs are invalid, tie
        
        if player1_choice not in choices:
            return 2  # Player 2 wins if player 1 input is invalid
        
        if player2_choice not in choices:
            return 1  # Player 1 wins if player 2 input is invalid

        if player1_choice == player2_choice:
            return 0  # Tie

        rules = {
            'rock': {'scissors': 1, 'paper': 2},
            'paper': {'rock': 1, 'scissors': 2},
            'scissors': {'paper': 1, 'rock': 2}
        }

        return rules[player1_choice].get(player2_choice, 0)
