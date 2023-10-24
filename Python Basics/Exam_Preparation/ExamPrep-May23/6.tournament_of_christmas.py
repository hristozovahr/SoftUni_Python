number_of_days = int(input())
games_won = 0
games_lost = 0
total_money = 0

for current_day in range(number_of_days):
    current_number_of_wins = 0
    current_number_of_lost = 0
    current_money = 0
    while True:
        sport = input()

        if sport == 'Finish':
            break

        result = input()

        if result == 'win':
            games_won += 1
            current_money += 20
            current_number_of_wins += 1

        elif result == 'lose':
            current_number_of_lost += 1

    if current_number_of_wins > current_number_of_lost:
        total_money += current_money + (current_money * 0.10)
    else:
        total_money += current_money

    games_lost += current_number_of_lost

if games_won > games_lost:
    total_money += total_money * 0.20
    print(f'You won the tournament! Total raised money: {total_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')
