def line (a, b):
    if b == "":
        print("*" * a)
    else:
        print(b[0] * a)
def shape(size, name, size_2, name_2):
    original_size = size # Сохраняем исходный размер
    while original_size > 0:
        line(size - original_size + 1, name)  # Используем исходный размер для вызова функции line
        original_size -= 1
    original_size = size_2
    while original_size > 0:
        # You should call function line here with proper parameters
        line(size, name_2)
        original_size -= 1

# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")