# Write your solution here
def all_the_longest(lst):
    if not lst:
        return []  

    longest_length = len(lst[0])

    for item in lst[1:]:
        if len(item) > longest_length:
            longest_length = len(item)

    result = [item for item in lst if len(item) == longest_length]

    return result