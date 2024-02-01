user_input = int(input("Layers: "))
center = 25
layer = user_input - 1
counter = 0

import string
string_x = ""
alphabet = 26
list_of_letters = [True]
while alphabet != (-1):
    string_x = string_x + string.ascii_uppercase[alphabet-1]*alphabet
    string_y = string_x[::-1]
    string_y = string_y[1:len(string_y)]
    alphabet = alphabet - 1
    string_z = string_x + string_y  
    list_of_letters.append(string_z)
    string_x = string_x[0:26-alphabet]

dictionary = { }
variable = 0
for number in range(1,27):
    dictionary[number] = 24 - variable
    variable = variable + 1

differential = user_input - dictionary[user_input]
counter = user_input - differential + 2
helper_variable = counter

while counter != 26:
    print(list_of_letters[counter][center-layer:center+user_input])
    counter = counter + 1
while counter != helper_variable - 1:
    print(list_of_letters[counter][center-layer:center+user_input])
    counter = counter - 1