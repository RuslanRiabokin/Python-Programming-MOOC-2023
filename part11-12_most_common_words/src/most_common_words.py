# WRITE YOUR SOLUTION HERE:

import string

def most_common_words(filename: str, lower_limit: int):
    # Read the file and tokenize into words
    with open(filename, 'r') as file:
        words = file.read().split()

    # Remove punctuation and keep words as they are
    words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]

    # Create a dictionary to store word counts
    word_counts = {}

    # Count occurrences of each word while maintaining case sensitivity and treating inflected forms as unique words
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    # Filter out words that don't meet the lower limit requirement
    common_words = {word: count for word, count in word_counts.items() if count >= lower_limit}

    # Sort the dictionary by values in descending order, then by keys in ascending order
    sorted_common_words = dict(sorted(common_words.items(), key=lambda item: (-item[1], item[0])))

    return sorted_common_words

