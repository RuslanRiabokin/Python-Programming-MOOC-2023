# write your solution here
def read_matrix(file_name="matrix.txt"):
    matrix = []
    with open(file_name) as file:
        for line in file:
            row = [int(num) for num in line.strip().split(",")]
            matrix.append(row)
    return matrix

def matrix_sum():
    matrix = read_matrix()
    total_sum = sum(sum(row) for row in matrix)
    return total_sum

def matrix_max():
    matrix = read_matrix()
    max_element = max(max(row) for row in matrix)
    return max_element

def row_sums():
    matrix = read_matrix()
    sums = [sum(row) for row in matrix]
    return sums
