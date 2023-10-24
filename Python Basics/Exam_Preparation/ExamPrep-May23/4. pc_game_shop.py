number_of_games = int(input())

hearthstone_count = 0
fornite_count = 0
overwatch_count = 0
others_count = 0

for _ in range(number_of_games):
    game_name = input()

    if game_name == 'Hearthstone':
        hearthstone_count += 1
    elif game_name == 'Fornite':
        fornite_count += 1
    elif game_name == 'Overwatch':
        overwatch_count += 1
    else:
        others_count += 1

hearthstone_percentage = (hearthstone_count / number_of_games) * 100
fornite_percentage = (fornite_count / number_of_games) * 100
overwatch_percentage = (overwatch_count / number_of_games) * 100
others_percentage = (others_count / number_of_games) * 100

print(f"Hearthstone - {hearthstone_percentage:.2f}%")
print(f"Fornite - {fornite_percentage:.2f}%")
print(f"Overwatch - {overwatch_percentage:.2f}%")
print(f"Others - {others_percentage:.2f}%")