number_of_student = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus_points = 0
max_student_attendances = 0
for students in range(number_of_student):
    students_attendances = int(input())
    total_bonus = students_attendances / number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
        max_student_attendances = students_attendances
print(f"Max Bonus: {round(max_bonus_points)}.")
print(f"The student has attended {max_student_attendances} lectures.")