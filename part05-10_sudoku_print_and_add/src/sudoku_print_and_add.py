# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(9):
        for j in range(9):
            if j % 3 == 0 and j > 0:
                print("", end=" ")
            print("_" if sudoku[i][j] == 0 else str(sudoku[i][j]), end=" ")
        print()
        if (i + 1) % 3 == 0 and i < 8:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    if 1 <= number <= 9 and 0 <= row_no < 9 and 0 <= column_no < 9 and sudoku[row_no][column_no] == 0:
        sudoku[row_no][column_no] = number
    else:
        print(f"Invalid input: {number} at ({row_no}, {column_no}).")
