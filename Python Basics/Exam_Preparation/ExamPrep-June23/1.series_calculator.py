from math import floor
serial_name = input()
seasons = int(input())
series = int(input())
duration = float(input())

duration = duration + duration * 0.2
total_time = seasons * duration * series
total_time += seasons * 10

print(f"Total time needed to watch the {serial_name} series is {floor(total_time)} minutes.")