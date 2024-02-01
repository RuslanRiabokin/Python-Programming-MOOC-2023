# Write your solution here
def row_correct(sudoku, row_no):
    count = [0] * 10

    for value in sudoku[row_no]:
        if value != 0:
            count[value] += 1
            if count[value] > 1:
                return False

    return True

def column_correct(sudoku, column_no):
    count = [0] * 10

    for row in sudoku:
        value = row[column_no]
        if value != 0:
            count[value] += 1
            if count[value] > 1:
                return False

    return True

def block_correct(sudoku, row_no, column_no):
    count = [0] * 10

    for i in range(3):
        for j in range(3):
            value = sudoku[row_no + i][column_no + j]
            if value != 0:
                count[value] += 1
                if count[value] > 1:
                    return False

    return True

def sudoku_grid_correct(sudoku):
    for i in range(9):
        if not row_correct(sudoku, i) or not column_correct(sudoku, i):
            return False


    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_correct(sudoku, i, j):
                return False

    return True