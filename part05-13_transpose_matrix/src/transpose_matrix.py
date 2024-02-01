# Write your solution here
def transpose(matrix: list):
    size = len(matrix)

    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]