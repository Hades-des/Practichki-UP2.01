class Person:
    def __init__(self, person_id):
        self.person_id = person_id

    def display_info(self):
        pass


class Reader(Person):
    def __init__(self, reader_id, visit_date, book_title):
        super().__init__(reader_id)
        self.visit_date = visit_date
        self.book_title = book_title

    def display_info(self):
        print(f"Reader ID: {self.person_id}")
        print(f"Last visit date: {self.visit_date}")
        print(f"Book title: {self.book_title}")


class Employee(Person):
    def __init__(self, employee_id, working_days):
        super().__init__(employee_id)
        self.working_days = working_days

    def display_info(self):
        print(f"Employee ID: {self.person_id}")
        print(f"Working days: {', '.join(self.working_days)}")


class LibraryTicket:
    def __init__(self, book_title, borrower, borrow_date, employee_shift):
        self.book_title = book_title
        self.borrower = borrower
        self.borrow_date = borrow_date
        self.employee_shift = employee_shift

    def display_info(self):
        print(f"Book title: {self.book_title}")
        print(f"Borrower: {self.borrower}")
        print(f"Borrow date: {self.borrow_date}")
        print(f"Employee shift: {self.employee_shift}")


if __name__ == "__main__":

    reader1 = Reader(1, "2023-10-07", "Python Basics")
    employee1 = Employee(101, ["Monday", "Wednesday", "Friday"])
    ticket1 = LibraryTicket("Python Basics", "John Doe", "2023-10-07", "Morning Shift")


    data = {
        1: ("Employee", employee1),
        2: ("Reader", reader1),
        3: ("Library Ticket", ticket1)
    }

    while True:
        print("Выберите действие:")
        print("(1) Вывести информацию о сотруднике")
        print("(2) Вывести информацию о читателе")
        print("(3) Вывести информацию о книге")
        print("(q) Выйти")

        choice = input("Введите номер действия: ")

        if choice == "q":
            break

        if choice.isdigit():
            choice = int(choice)
            if choice in data:
                item_type, item = data[choice]
                print(f"\nИнформация о {item_type}:")
                item.display_info()
                print()
            else:
                print("Неправильный выбор. Попробуйте снова.")
        else:
            print("Неправильный выбор. Попробуйте снова.")
