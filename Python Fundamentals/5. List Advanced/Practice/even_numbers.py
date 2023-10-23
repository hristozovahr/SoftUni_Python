numbers = input().split(", ")
numbers = [int(x) for x in numbers]
even_indexes = []
for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        even_indexes.append(index)
print(even_indexes)
