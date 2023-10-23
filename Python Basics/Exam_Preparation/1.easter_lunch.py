number_of_bread = int(input())
number_of_eggs = int(input())
kg_of_cookies = int(input())

bread_price = number_of_bread * 3.2
eggs_price = number_of_eggs * 4.35
cookies_price = kg_of_cookies * 5.4
color_price = (number_of_eggs * 12) * 0.15

total_price = bread_price + eggs_price + cookies_price + color_price

print(f"{total_price:.2f}")
