# Write your solution here
def no_vowels(s):
    vowels = "aeiou"
    result = ''.join(char for char in s if char not in vowels)
    return result