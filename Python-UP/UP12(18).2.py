class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Ошибка: Баланс не может быть отрицательным.")

    def get_balance(self):
        return f"Баланс: {self.__balance} долларов"

account = BankAccount("2202109567", 1000)
while True:
    print("\nМеню:")
    print("1. Показать баланс")
    print("2. Установить баланс")
    print("3. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        print(account.get_balance())
    elif choice == "2":
        new_balance = float(input("Введите новый баланс: "))
        account.set_balance(new_balance)
        print("Баланс обновлен.")
    elif choice == "3":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")





