class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.speed = 0
        self.engine_started = False
    def start_engine(self):
        if not self.engine_started:
            self.engine_started = True
            print("Двигатель машины запущен.")
        else:
            print("Двигатель уже запущен.")
    def stop_engine(self):
        if self.engine_started:
            self.engine_started = False
            self.speed = 0
            print("Двигатель машины выключен.")
        else:
            print("Двигатель уже выключен.")
    def accelerate(self, amount):
        if self.engine_started:
            if self.speed + amount:
                self.speed += amount < 220
                print(f"Скорость увеличена на {amount} км/ч. Текущая скорость: {self.speed} км/ч.")
            elif self.speed > 220: print("Скорость не может быть больше 220")

        else:
            print("Предупреждение: Двигатель выключен. Запустите двигатель, прежде чем увеличивать скорость.")
    def brake(self, amount):
        if self.engine_started:
            if self.speed - amount >= 0:
                self.speed -= amount
                print(f"Скорость уменьшена на {amount} км/ч. Текущая скорость: {self.speed} км/ч.")
            else:
                print("Предупреждение: Скорость не может стать отрицательной. Текущая скорость: 0 км/ч.")
        else:
            print("Предупреждение: Двигатель выключен. Запустите двигатель, прежде чем уменьшать скорость.")
    def display_carinfo(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Тип топлива: {self.fuel_type}")
        print(f"Текущая скорость: {self.speed} км/ч.")
        if self.engine_started:
            print("Состояние двигателя: запущен")
        else:
            print("Состояние двигателя: выключен")
my_car = Car("Reno", "Logan", 2006, "Бензин")
while True:
    print("\nМеню:")
    print("1. Запустить двигатель")
    print("2. Выключить двигатель")
    print("3. Увеличить скорость")
    print("4. Уменьшить скорость")
    print("5. Вывести информацию о машине")
    print("6. Выйти из программы")
    choice = input("Выберите действие: ")
    if choice == "1":
        my_car.start_engine()
    elif choice == "2":
        my_car.stop_engine()
    elif choice == "3":
        amount = int(input("Введите количество км/ч для увеличения скорости: "))
        my_car.accelerate(amount)
    elif choice == "4":
        amount = int(input("Введите количество км/ч для уменьшения скорости: "))
        my_car.brake(amount)
    elif choice == "5":
        my_car.display_carinfo()
    elif choice == "6":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
