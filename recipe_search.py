def search_by_name(filename: str, word: str):
    found_recipes = []

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            recipe_name = None
            for line in lines:
                stripped_line = line.strip()

                if not stripped_line:
                    if recipe_name and word.lower() in recipe_name.lower():
                        found_recipes.append(recipe_name)
                    recipe_name = None
                elif recipe_name is None:
                    recipe_name = stripped_line

            if recipe_name and word.lower() in recipe_name.lower():
                found_recipes.append(recipe_name)

    except FileNotFoundError:
        print(f"File {filename} not found.")

    return found_recipes


def search_by_time(filename: str, prep_time: int):
    found_recipes = []

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            recipe_name = None
            prep_time_recipe = None

            for line in lines:
                stripped_line = line.strip()

                if stripped_line.isdigit() and recipe_name is not None and prep_time_recipe is None:
                    try:
                        prep_time_recipe = int(stripped_line)
                    except ValueError:
                        print(f"Error parsing time in recipe: {recipe_name}")
                elif prep_time_recipe is not None:
                    if prep_time_recipe <= prep_time:
                        found_recipes.append(f"{recipe_name}, preparation time {prep_time_recipe} min")
                    recipe_name = None
                    prep_time_recipe = None
                elif stripped_line:
                    recipe_name = stripped_line

            # Проверка последнего рецепта
            if recipe_name is not None and prep_time_recipe is not None and prep_time_recipe <= prep_time:
                found_recipes.append(f"{recipe_name}, preparation time {prep_time_recipe} min")

    except FileNotFoundError:
        print(f"File {filename} not found.")

    return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
    found_recipes = []

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            recipe_name = None
            ingredients = []
            prep_time = None

            for line in lines:
                stripped_line = line.strip()

                if not stripped_line:
                    if recipe_name and any(ingredient.lower() in item.lower() for item in ingredients):
                        if prep_time is not None:
                            found_recipes.append(f"{recipe_name}, preparation time {prep_time} min")

                    recipe_name = None
                    ingredients = []
                    prep_time = None
                elif not prep_time and stripped_line.isdigit():
                    prep_time = int(stripped_line)
                elif not prep_time:
                    recipe_name = stripped_line
                else:
                    ingredients.append(stripped_line)

            if recipe_name and any(ingredient.lower() in item.lower() for item in ingredients):
                if prep_time is not None:
                    found_recipes.append(f"{recipe_name}, preparation time {prep_time} min")

    except FileNotFoundError:
        print(f"File {filename} not found.")

    return found_recipes

