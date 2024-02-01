# Copy here code of line function from previous exercise

def line(a, b):
    print(b * a)

def square(size, character):
    original_size = size  # Сохраняем исходный размер
    while original_size > 0:
        # You should call function line here with proper parameters
        line(size, character)
        original_size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")