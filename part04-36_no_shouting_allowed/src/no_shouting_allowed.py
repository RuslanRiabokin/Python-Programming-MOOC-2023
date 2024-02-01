# Write your solution here
def no_shouting(lst):
    filtered_list = []
    for item in lst:
        if not isinstance(item, str) or not item.isupper():
            filtered_list.append(item)
    return filtered_list