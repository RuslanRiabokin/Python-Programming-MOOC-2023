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

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    grid_copy = [list(row) for row in sudoku]

    grid_copy[row_no][column_no] = number

    return grid_copy