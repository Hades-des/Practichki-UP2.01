try:
    divident = float(input("Введите делимое: "))
    divisor = float(input("Введите делитель: "))
    result = divident / divisor
    print("Результат деления:", result)
except ZeroDivisionError:
    print("Ошибка: Делитель равен нулю")
except ValueError:
    print("Ошибка: Введены некорректные данные")