# Write your solution here
from math import sqrt

def hypotenuse(leg1: float, leg2: float) -> float:
    
    hypotenuse_length = sqrt(leg1**2 + leg2**2)
    return hypotenuse_length