import math

def my_function(x):
    y = math.sinh(4.1 * x) + 0.2 * math.cosh(5 * x)
    return y

x = float(input("Введите значение x: "))
result = my_function(x)
print(f"Значение функции y = sh(4.1x) + 0.2ch(5x) при x = {x} равно {result}")
