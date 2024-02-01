# Write your solution here
def column_correct(sudoku, column_no):
    count = [0] * 10 
    for row in sudoku:
        value = row[column_no]
        if value != 0:  
            count[value] += 1
            if count[value] > 1:
                return False

    return True