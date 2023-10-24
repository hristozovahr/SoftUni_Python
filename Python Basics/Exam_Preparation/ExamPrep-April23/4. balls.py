number_of_balls = int(input())
total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_balls = 0
divides_balls = 0
for balls in range(number_of_balls):
    current_color = input()

    if current_color == 'red':
        total_points += 5
        red_balls += 1
    elif current_color == 'orange':
        total_points += 10
        orange_balls += 1
    elif current_color == 'yellow':
        total_points += 15
        yellow_balls += 1
    elif current_color == 'white':
        total_points += 20
        white_balls += 1
    elif current_color == 'black':
        total_points //= 2
        divides_balls += 1
    else:
        other_balls += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {divides_balls}")