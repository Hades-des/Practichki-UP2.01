import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
circle = Circle(6)
rectangle = Rectangle(8, 12)
print("Круг:")
print("Площадь:", circle.area())
print("Периметр:", circle.perimeter())
print("\nПрямоугольник:")
print("Площадь:", rectangle.area())
print("Периметр:", rectangle.perimeter())