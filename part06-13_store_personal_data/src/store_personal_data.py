# Write your solution here
def store_personal_data(person):
    name, age, height = person
    entry = f"{name};{age};{height}\n"

    try:
        with open("people.csv", 'a') as file:
            file.write(entry)
        print("Data stored successfully.")
    except Exception as e:
        print(f"Error storing data: {e}")

def store_personal_data(person):
    name, age, height = person
    entry = f"{name};{age};{height}\n"

    try:
        with open("people.csv", 'a') as file:
            file.write(entry)
        print("Data stored successfully.")
    except Exception as e:
        print(f"Error storing data: {e}")

# Пример использования функции
person_data = ("Paul Paulson", 37, 175.5)
store_personal_data(person_data)

