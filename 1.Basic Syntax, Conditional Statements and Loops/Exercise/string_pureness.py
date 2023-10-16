number_of_strings = int(input())

for current_string in range(number_of_strings):
    strings = input()
    if "," in strings or\
            "." in strings or\
            "_" in strings:
        print(f"{strings} is not pure!")
    else:
        print(f"{strings} is pure.")