budged = float(input())
kg_flour_price = float(input())
eggs_price = kg_flour_price * 0.75
milk_price_for_one_loaf = (kg_flour_price * 1.25) / 4
one_loaf_price = kg_flour_price + milk_price_for_one_loaf + eggs_price
eggs_counter = 0
loaf_counter = 0
while budged > 0:
    if one_loaf_price > budged:
        break
    budged -= one_loaf_price
    loaf_counter += 1
    eggs_counter += 3
    if loaf_counter % 3 == 0:
        eggs_counter -= loaf_counter -2
    if eggs_counter <= 0:
        break
print(f"You made {loaf_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {budged:.2f}BGN left.")
