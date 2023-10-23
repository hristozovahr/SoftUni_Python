people = int(input())
current_lift_state = [int(x) for x in input().split()]
max_people = 4

for wagon in range(len(current_lift_state)):
    max_people = min(max_people - current_lift_state[wagon], people)
    current_lift_state[wagon] += max_people
    people -= max_people

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
e
print(' '.join([str(i) for i in current_lift_state]))
