import difflib

def load_wordlist(file_path):
    with open(file_path, 'r') as wordlist_file:
        wordlist = set(word.strip().lower() for word in wordlist_file)
    return wordlist

def get_suggestions(misspelled_word, wordlist):
    suggestions = difflib.get_close_matches(misspelled_word, wordlist)
    return suggestions

def spell_check(text, wordlist):
    words = text.split()
    corrected_text = []
    misspelled_words = []

    for word in words:
        lower_word = word.lower()

        if lower_word not in wordlist:
            misspelled_words.append(lower_word)
            corrected_text.append(f'*{word}*')
        else:
            corrected_text.append(word)

    print(' '.join(corrected_text))  # Print corrected text in one line

    print("\nsuggestions:")
    for misspelled_word in misspelled_words:
        suggestions = get_suggestions(misspelled_word, wordlist)
        print(f"{misspelled_word}: {', '.join(suggestions)}")


def main():
    wordlist_path = "wordlist.txt"
    wordlist = load_wordlist(wordlist_path)

    user_text = input("Write text: ")
    spell_check(user_text, wordlist)

main()