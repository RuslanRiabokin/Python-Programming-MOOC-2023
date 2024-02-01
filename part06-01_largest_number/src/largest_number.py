def largest():
    with open("numbers.txt") as new_file:
        contents = new_file.read().split()  
        numbers = [int(num) for num in contents]  
        
        if numbers:
            return max(numbers)
        else:
            return None
