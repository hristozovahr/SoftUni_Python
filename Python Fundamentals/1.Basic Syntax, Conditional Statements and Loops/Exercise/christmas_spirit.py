quantity_of_decoration = int(input())
days_left = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

total_points = 0
total_price = 0

for current_day in range(1, days_left + 1):
    if current_day % 11 == 0:
        quantity_of_decoration += 2
    if current_day % 2 == 0:
        total_price += quantity_of_decoration * ornament_set_price
        total_points += 5
    if current_day % 3 == 0:
        total_price += (quantity_of_decoration * tree_skirt_price) + (quantity_of_decoration * tree_garland_price)
        total_points += 3 + 10
    if current_day % 5 == 0:
        total_price += quantity_of_decoration * tree_lights_price
        total_points += 17
        if current_day % 3 == 0:
            total_points += 30
    if current_day % 10 == 0:
        total_points -= 20
        total_price += tree_skirt_price + tree_garland_price + tree_lights_price
if days_left % 10 == 0:
    total_points -= 30
print(f"Total cost: {total_price}")
print(f"Total spirit: {total_points}")
