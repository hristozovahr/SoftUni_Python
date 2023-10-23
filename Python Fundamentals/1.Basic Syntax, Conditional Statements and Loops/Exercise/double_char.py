strings = input()

while strings != "End":
    if strings != "SoftUni":
        new_string = ""
        for character in strings:
            new_string += character * 2
        print(new_string)
    strings = input()
