class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Круг(Радиус: {self.radius})"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник(Ширина: {self.width}, Высота: {self.height})"

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __str__(self):
        return f"Треугольник(Стороны: {self.side1}, {self.side2}, {self.side3})"
    
shapes = [Circle(5.0), Rectangle(4.0, 3.0), Triangle(1.0, 2.0, 3.0)]

def print_shapes(shapes):
    for i, shape in enumerate(shapes, 1):
        print(f"Фигура {i}: {shape}")

print_shapes(shapes)
