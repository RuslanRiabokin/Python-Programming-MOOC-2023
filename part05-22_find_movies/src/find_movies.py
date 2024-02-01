# Write your solution here
def find_movies(database: list, search_term: str):
    search_term_lower = search_term.lower()
    result_movies = []

    for movie in database:
        if search_term_lower in movie["name"].lower():
            result_movies.append(movie)

    return result_movies