# Write your solution here
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