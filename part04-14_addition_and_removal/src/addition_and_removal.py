my_list = []
d = 1
while True:
    print("The list is now",my_list)
    addition = input("a(d)d, (r)emove or e(x)it: ")
    if addition == "d":
        my_list.append(d)
        d += 1

    elif addition == "r":
        if my_list:
            d -= 1
            my_list.pop(-1)

    elif addition == "x":
        print("Bye!")
        break
