registered_users_in_the_courses = {}
command = input()
while command != "end":
    current_course, user_name = command.split(" : ")
    if current_course not in registered_users_in_the_courses:
        registered_users_in_the_courses[current_course] = []
    elif current_course in registered_users_in_the_courses:
        registered_users_in_the_courses[current_course].append(user_name)
        command = input()

for course, students in registered_users_in_the_courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")






