minutes = int(input())
seconds = int(input())
length = float(input())
time_for_100_meters = int(input())

control_time = minutes * 60 + seconds
delay = length / 120
total_delay = 2.5 * delay
race_time_marin = (length / 100) * time_for_100_meters - total_delay


if control_time >= race_time_marin:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {race_time_marin:.3f}.")
elif control_time < race_time_marin:
    needed_time = race_time_marin - control_time
    print(f"No, Marin failed! He was {needed_time:.3f} second slower.")

