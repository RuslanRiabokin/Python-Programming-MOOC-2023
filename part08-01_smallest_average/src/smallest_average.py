def smallest_average(person1: dict, person2: dict, person3: dict):
    # Calculate average for each person
    person1_avg = sum(person1[key] for key in person1.keys() if key.startswith('result')) / 3
    person2_avg = sum(person2[key] for key in person2.keys() if key.startswith('result')) / 3
    person3_avg = sum(person3[key] for key in person3.keys() if key.startswith('result')) / 3
    
    # Find the person with the smallest average
    min_avg = min(person1_avg, person2_avg, person3_avg)
    if min_avg == person1_avg:
        return person1
    elif min_avg == person2_avg:
        return person2
    else:
        return person3

