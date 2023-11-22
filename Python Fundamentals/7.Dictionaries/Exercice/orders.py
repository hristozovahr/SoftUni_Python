all_products_dictionary = {}
command = input()
while command != "buy":
    product, price, quantity = command.split()
    price, quantity = float(price), int(quantity)

    if product not in all_products_dictionary:
        all_products_dictionary[product] = [price, quantity]

    elif product in all_products_dictionary:
        all_products_dictionary[product][0] = price
        all_products_dictionary[product][1] += quantity
    command = input()
for product in all_products_dictionary.keys():
    all_products_dictionary[product] = all_products_dictionary[product][0] * all_products_dictionary[product][1]
    print(f"{product} -> {all_products_dictionary[product]:.2f}")

