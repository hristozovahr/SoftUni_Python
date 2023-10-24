number_of_bread = int(input())
best_chef_name = ""
best_points = 0

for breads in range(number_of_bread):
    personal_points = 0
    cooker_name = input()
    command = input()
    while command != 'Stop':
        bread_value = int(command)
        personal_points += bread_value
        command = input()
    print(f"{cooker_name} has {personal_points} points.")
    if personal_points > best_points:
        best_points = personal_points
        best_chef_name = cooker_name
        print(f"{cooker_name} is the new number 1!")
print(f"{best_chef_name} won competition with {best_points} points!")
