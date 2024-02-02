# Write your solution here
def find_words(search_term: str):
    with open('words.txt', 'r') as file:
        words = file.read().split()

    matching_words = []

    if '*' in search_term:
        if search_term.startswith('*'):
            # Звездочка в начале поискового запроса
            prefix = search_term[1:]
            matching_words = [word for word in words if word.endswith(prefix)]
        elif search_term.endswith('*'):
            # Звездочка в конце поискового запроса
            suffix = search_term[:-1]
            matching_words = [word for word in words if word.startswith(suffix)]
        else:
            # Звездочка в середине поискового запроса (только одна звездочка допускается)
            prefix, suffix = search_term.split('*')
            matching_words = [word for word in words if word.startswith(prefix) and word.endswith(suffix)]
    elif '.' in search_term:
        # Подстановка точки
        pattern = search_term.replace('.', '.')
        matching_words = [word for word in words if len(word) == len(pattern) and all(c1 == c2 or c2 == '.' for c1, c2 in zip(word, pattern))]
    else:
        # Поиск точного соответствия
        matching_words = [word for word in words if word == search_term]

    return matching_words

# Пример использования
print(find_words("*vokes"))
