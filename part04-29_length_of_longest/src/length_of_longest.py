# Write your solution here
def length_of_longest(lst):
    best_length = 0 
    for item in lst:
        if len(item) > best_length:
            best_length = len(item)

    return best_length