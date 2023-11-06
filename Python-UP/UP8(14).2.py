class Student:
    def __init__(self, first_name, last_name, group, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.average_grade = average_grade
    def __str__(self):
        return f"Студент: {self.first_name} {self.last_name}, Группа: {self.group}, Средний балл: {self.average_grade}"
class StudentDatabase:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def remove_student(self, student):
        self.students.remove(student)
    def find_student_by_name(self, name):
        return [student for student in self.students if name in student.first_name or name in student.last_name]
    def find_student_by_group(self, group):
        return [student for student in self.students if group == student.group]
database = StudentDatabase()
def input_student_info():
    first_name = input("Введите имя студента: ")
    last_name = input("Введите фамилию студента: ")
    group = input("Введите группу студента: ")
    average_grade = float(input("Введите средний балл студента: "))
    student = Student(first_name, last_name, group, average_grade)
    return student
while True:
    student = input_student_info()
    database.add_student(student)
    another = input("Добавить еще студента? (да/нет): ")
    if another.lower() != "да":
        break
print("Список студентов в базе данных:")
for student in database.students:
    print(student)
search_option = input("Выберите опцию поиска (по имени/по группе): ")
if search_option == "по имени":
    search_name = input("Введите имя или фамилию для поиска: ")
    found_students = database.find_student_by_name(search_name)
elif search_option == "по группе":
    search_group = input("Введите группу для поиска: ")
    found_students = database.find_student_by_group(search_group)
if found_students:
    print("Найденные студенты:")
    for student in found_students:
        print(student)
else:
    print("Студенты с такими данными не найдены.")
