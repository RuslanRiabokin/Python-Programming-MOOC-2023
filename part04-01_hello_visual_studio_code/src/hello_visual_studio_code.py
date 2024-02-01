# Write your solution here
while True:
    editor = input("Editor:")
    editors = editor.lower()
    if editors == "visual studio code":
        print("an excellent choice!")
        break
    elif editors == "word" or editors == "notepad":
        print("awful")
    else:
        print("not good")

