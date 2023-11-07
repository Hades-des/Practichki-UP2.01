from moduls.M5_figures.square.code import *
from moduls.M5_figures.triangle.code import *
from moduls.M5_figures.circle.code import *
s = int(input("Введите строну квадрата: "))

print(f"Периметр:{square_perimeter(s)}")
print(f"Площадь:{square_area(s)}")

s1 = int(input("Введите первую сторону треугольника: "))
s2 = int(input("Введите вторую сторону треугольника: "))
s3 = int(input("Введите третью сторону треугольника: "))
height = int(input("Введите высоту треугольника: "))
base = int(input("Введите основание треугольника: "))

print(f"Периметр:{triangle_perimeter(s1,s2,s3)}")
print(f"Площадь:{triangle_area(base,height)}")

radius = int(input("Введите радиус круга: "))
print(f"Периметр:{circle_perimeter(radius)}")
print(f"Площадь:{circle_area(radius)}")
