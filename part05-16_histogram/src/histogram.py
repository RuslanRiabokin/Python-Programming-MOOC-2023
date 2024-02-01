# Write your solution here
def histogram(a):
    a = a.lower()
    letter_counts = {}
    for char in a:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    sorted_letter_counts = dict(sorted(letter_counts.items(), key=lambda x: a.find(x[0])))
    for letter, count in sorted_letter_counts.items():
        print(f"{letter} {count * '*'}")


