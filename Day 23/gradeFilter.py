# Print only students with grades above or equal to 75
students = {'Alice': 82, 'Bob': 67, 'Clara': 91, 'David': 74}

for name, grade in students.items():
    if grade >= 75:
        print(f"{name} passed with a grade of {grade}")
    else:
        print(f"{name} failed with a grade of {grade}")