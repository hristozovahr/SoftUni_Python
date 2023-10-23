contract_term = input()
contract_type = input()
mobile_internet = input()
num_months = int(input())

base_fee = 0

if contract_term == 'one':
    if contract_type == 'Small':
        base_fee = 9.98
    elif contract_type == 'Middle':
        base_fee = 18.99
    elif contract_type == "Large":
        base_fee = 25.98
    elif contract_type == "ExtraLarge":
        base_fee = 35.99

elif contract_term == 'two':
    if contract_type == 'Small':
        base_fee = 8.58
    elif contract_type == 'Middle':
        base_fee = 17.09
    elif contract_type == "Large":
        base_fee = 23.59
    elif contract_type == "ExtraLarge":
        base_fee = 31.79

if mobile_internet == "yes":
    if base_fee <= 10:
        base_fee += 5.5
    elif base_fee <= 30:
        base_fee += 4.35
    else:
        base_fee += 3.85

if contract_term == "two":
    base_fee -= base_fee * 0.0375

total_amount = num_months * base_fee
print(f"{total_amount:.2f} lv.")