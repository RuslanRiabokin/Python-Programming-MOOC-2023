# Write your solution here
# You can test your function by calling it within the following block
def spruce(height):
    print("a spruce!")
    i = 1
    while i <= height:
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
        i += 1

    trunk_spaces = " " * (height - 1)
    print(trunk_spaces + "*")
if __name__ == "__main__":
    spruce(5)