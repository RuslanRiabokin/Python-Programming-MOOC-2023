# Copy here code of line function from previous exercise

def line (a, b):
    if b == "":
        print("*" * a)
    else:
        print(b[0] * a)
def triangle(size):
    original_size = size # Сохраняем исходный размер
    while original_size > 0:
        line(size - original_size + 1, "#")  # Используем исходный размер для вызова функции line
        original_size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
