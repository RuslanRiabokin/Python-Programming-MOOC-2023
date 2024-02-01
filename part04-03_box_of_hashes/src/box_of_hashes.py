# Copy here code of line function from previous exercise

def line (a, b):
    if b == "":
        print("*" * a)
    else:
        print(b[0] * a)
def box_of_hashes(times):
    while times > 0:
        # You should call function line here with proper parameters
        line(10, "#")
        times -=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
