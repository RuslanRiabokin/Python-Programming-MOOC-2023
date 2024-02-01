# Write your solution here
def longest_series_of_neighbours(lst):
    current_series_length = 1  
    max_series_length = 1  

    for i in range(1, len(lst)):
        if abs(lst[i] - lst[i - 1]) == 1:
            current_series_length += 1
        else:
            current_series_length = 1
        max_series_length = max(max_series_length, current_series_length)
    return max_series_length