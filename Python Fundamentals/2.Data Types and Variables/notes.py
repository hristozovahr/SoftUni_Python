#SET  #immmutable
some_string = "AAAMMMDDKKRRRRAAAIIII"
print(set(some_string))


#TUPLE  #immmutable
(1, 3)

#LIST


order_count = int(input())
total_cost = 0

for order in range(order_count):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue

    order_total = capsule_price * days * capsules_per_day
    total_cost += order_total
    print(f'The price for the coffee is: ${order_total:.2f}')

print(f'Total: ${total_cost:.2f}')