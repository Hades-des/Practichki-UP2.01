from moduls.M1_math_operations import *

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

print(f"Сложение:{add(a, b)}")
print(f"Вычитание:{subtract(a, b)}")
print(f"Умножение:{multiply(a, b)}")
print(f"Деление:{divide(a, b)}")