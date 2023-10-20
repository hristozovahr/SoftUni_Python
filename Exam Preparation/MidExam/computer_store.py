price_without_taxes = 0
taxes = 0
total_price = 0
while True:
    parts_price = input()
    if parts_price == 'regular':
        total_price = price_without_taxes + taxes
        break
    elif parts_price == 'special':
        total_price = (price_without_taxes + taxes) * 0.9
        break
    parts_price_integer = float(parts_price)
    if parts_price_integer < 0:
        print('Invalid price!')
        continue
    taxes += parts_price_integer * 0.2
    price_without_taxes += parts_price_integer
if total_price == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {price_without_taxes:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price:.2f}$")