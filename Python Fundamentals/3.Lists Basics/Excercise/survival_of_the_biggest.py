list_of_numbers = input().split(" ")
for number in range(len(list_of_numbers)):
    list_of_numbers[number] = int(list_of_numbers[number])
numbers_to_remove = int(input())
for i in range(numbers_to_remove):
    list_of_numbers.remove(min(list_of_numbers))
print(', '.join(str(number) for number in list_of_numbers))