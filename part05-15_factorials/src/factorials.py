# Write your solution here
def factorials(n: int):
    result = {}
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        result[i] = factorial
    return result