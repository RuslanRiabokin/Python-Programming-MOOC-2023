def load_wordlist(file_path):
    with open(file_path, 'r') as wordlist_file:
        wordlist = set(word.strip().lower() for word in wordlist_file)
    return wordlist

def spell_check(text, wordlist):
    words = text.split()
    corrected_text = []

    for word in words:

        lower_word = word.lower()

        if lower_word not in wordlist:

            corrected_text.append(f'*{word}*')
        else:
            corrected_text.append(word)

    return ' '.join(corrected_text)

def main():
    wordlist_path = "wordlist.txt"
    wordlist = load_wordlist(wordlist_path)

    user_text = input("Write text: ")
    corrected_text = spell_check(user_text, wordlist)

    print(corrected_text)


main()
