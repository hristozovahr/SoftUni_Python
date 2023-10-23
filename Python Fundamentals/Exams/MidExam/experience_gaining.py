wanted_experience = float(input())
count_of_battles = int(input())

battle_count = 0
needed_experience = 0
total_experience = 0

for current_battle in range(1, count_of_battles + 1):
    battle_count += 1
    current_battle_experience = float(input())
    total_experience += current_battle_experience

    if battle_count % 3 == 0:
        current_battle_experience += current_battle_experience * 0.15
        total_experience + current_battle_experience
    if battle_count % 5 == 0:
        current_battle_experience -= current_battle_experience * 0.10
        total_experience += current_battle_experience
    if battle_count % 15 == 0:
        current_battle_experience += current_battle_experience * 0.05
        total_experience += current_battle_experience
    if total_experience >= wanted_experience:
        print(f"Player successfully collected his needed experience for {battle_count} battles.")
        break


if total_experience < wanted_experience:
    needed_experience = wanted_experience - total_experience
    print(f"Player was not able to collect the needed experience, {needed_experience:.2f} more needed.")

