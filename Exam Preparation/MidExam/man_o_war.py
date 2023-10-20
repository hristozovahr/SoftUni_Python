def fire(warship, index, damage):
    if 0 <= index < len(warship):
        warship[index] -= damage

        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()

def defend(pirate_ship, startIndex, endIndex, damage):
    if 0 <= startIndex < len(pirate_ship) and 0 <= endIndex < len(pirate_ship):
        for i in range(startIndex, endIndex + 1):
            pirate_ship[i] -= damage

            if pirate_ship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()
def repair(pirate_ship, index, health, max_health):
    if 0 <= index < len(pirate_ship):
        pirate_ship[index] = min(pirate_ship[index] + health, max_health)

def status(pirate_ship, max_health):
    count = sum(1 for section in pirate_ship if section < 0.2 * max_health)
    print(f"{count} sections need repair.")


pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())

while True:
    command = input().split()
    current_command = command[0]
    if current_command == 'Retire':
        break
    elif current_command == 'Fire':
        index, damage = int(command[1]), int(command[2])
        fire(warship, index, damage)
    elif current_command == 'Defend':
        startIndex, endIndex, damage = int(command[1]), int(command[2]), int(command[3])
        defend(pirate_ship, startIndex, endIndex, damage)

    elif current_command == 'Repair':
        index, health = int(command[1]), int(command[2])
        repair(pirate_ship, index, health, max_health)

    elif current_command == 'Status':
        status(pirate_ship, max_health)
print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")