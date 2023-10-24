food_in_kg = int(input())
food_in_grams = food_in_kg * 1000
command = input()

while command != 'Adopted':
    eaten_food_in_grams = int(command)
    food_in_grams -= eaten_food_in_grams
    command = input()

if food_in_grams >= 0:
    print(f"Food is enough! Leftovers: {food_in_grams} grams.")
else:

    print(f"Food is not enough. You need {abs(food_in_grams)} grams more.")