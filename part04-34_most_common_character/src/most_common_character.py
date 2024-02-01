# Write your solution here
def most_common_character(s):
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    most_common_char = max(char_count, key=char_count.get)
    return most_common_char