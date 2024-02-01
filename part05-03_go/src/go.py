# Write your solution here
def who_won(game_board):
    player1_count = 0
    player2_count = 0
    for row in game_board:
        for value in row:
            if value == 1:
                player1_count += 1
            elif value == 2:
                player2_count += 1
    if player1_count > player2_count:
        return 1
    elif player1_count < player2_count:
        return 2
    else:
        return 0

