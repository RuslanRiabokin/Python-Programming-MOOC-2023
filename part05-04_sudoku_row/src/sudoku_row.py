def row_correct(sudoku, row_no):
    count = [0] * 10  

    for value in sudoku[row_no]:
        if value != 0:  
            count[value] += 1
            if count[value] > 1:
                return False

    return True