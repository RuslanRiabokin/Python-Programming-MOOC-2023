# Write your solution here
def count_matching_elements(my_matrix, element):
    count = 0
    for row in my_matrix:
        for value in row:
            if value == element:
                count += 1
    
    return count

