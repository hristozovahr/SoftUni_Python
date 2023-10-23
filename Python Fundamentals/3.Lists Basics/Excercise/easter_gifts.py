name_of_the_gift = input().split()
command = input()

while command != "No Money":
    if "OutOfStock" in command:
        command_items = command.split(" ")
        gift = command_items[-1]
        name_of_the_gift = [item.replace(gift, "None") for item in name_of_the_gift]


print(name_of_the_gift)