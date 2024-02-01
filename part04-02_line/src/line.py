# Write your solution here
# You can test your function by calling it within the following block
def line (a, b):
    if b == "":
        print("*" * a)
    else:
        print(b[0] * a)
if __name__ == "__main__":
    line(5, "x")