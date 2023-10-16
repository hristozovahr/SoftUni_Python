value = float(input())
if value == 0:
    print("zero")
elif value > 0:
    if value < 1:
        print("small positive")
    elif value > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if abs(value) < 1:
        print("small negative")
    elif abs(value) > 1000000:
        print("large negative")
    else:
        print("negative")