# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    if 0 <= x < 3 and 0 <= y < 3 and game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    else:
        return False