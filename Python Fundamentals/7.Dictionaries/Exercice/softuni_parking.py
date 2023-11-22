number = int(input())
registered_users = {}
for current_user in range(number):
    action = input().split()
    action_type = action[0]
    user = action[1]
    if action_type == "register":
        license_plate_number = action[2]
        if user not in registered_users:
            registered_users[user] = license_plate_number
            print(f"{user} registered {license_plate_number} successfully")
        elif user in registered_users:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif action_type == "unregister":
        if user not in registered_users:
            print(f"ERROR: user {user} not found")
        elif user in registered_users:
            value = registered_users.pop(user)
            print(f"{user} unregistered successfully")


for user, plate in registered_users.items():
    print(f"{user} => {plate}")
