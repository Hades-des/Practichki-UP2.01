
students = []
while True:
    name = input("Введите фамилию студента (или 'q' для завершения ввода): ")
    if name == 'q':
        break

    grades = []
    for i in range(3):
        grade = int(input(f"Введите оценку {i + 1} для студента {name}: "))
        grades.append(grade)

    student = {"фамилия": name, "оценки": grades}
    students.append(student)


print("Информация о студентах:")
for student in students:
    print(f"Фамилия: {student['фамилия']}")
    print(f"Оценки: {student['оценки']}")

def is_good_student(student):
    return all(grade > 3 for grade in student["оценки"])
good_students = [student for student in students if is_good_student(student)]
print("Хорошие студенты:")
for student in good_students:
    print(f"Фамилия: {student['фамилия']}")
    print(f"Оценки: {student['оценки']}")
