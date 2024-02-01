# write your solution here

def read_fruits():
    fruits_data = {}  
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            grade = float(parts[1])  
            fruits_data[name] = grade  

    return fruits_data  

