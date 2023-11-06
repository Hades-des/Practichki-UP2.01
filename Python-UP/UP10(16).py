class Student:
    def __init__(self, name, scholarship):
        self.name = name
        self.scholarship = scholarship
    def display_info(self):
        if self.scholarship > 0:
            print(f"{self.name} имеет стипендию в размере {self.scholarship} рублей.")
        else:
            print(f"{self.name} не получает стипендию.")
students = []
while True:
    name = input("Введите имя студента (или нажмите Enter для завершения): ")
    if name == "":
        break
    scholarship = int(input("Введите размер стипендии: "))
    student = Student(name, scholarship)
    students.append(student)
for student in students:
    student.display_info()

