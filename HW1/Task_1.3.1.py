import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Triangle(Shape):
    def __init__(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError(f"Invalid triangle")
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

class Trapeze(Shape):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d
        s = self.perimeter() / 2
        self.value = (s - self.a) * (s - self.b) * (s - self.c) * (s - self.d)
        if self.value < 0:
            raise ValueError("Invalid trapezoid")

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        return math.sqrt(self.value)


class Parallelogram(Shape):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2

def create_shape(line):
    parts = line.split()
    name = parts[0]
    nums = list(map(float, parts[1:]))

    if name == "Triangle":
        return Triangle(*nums)
    elif name == "Rectangle":
        return Rectangle(*nums)
    elif name == "Trapeze":
        return Trapeze(*nums)
    elif name == "Parallelogram":
        return Parallelogram(*nums)
    elif name == "Circle":
        return Circle(*nums)
    else:
        raise ValueError("Невідомий тип фігури")

def process_file(filename):
    shapes = []

    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                try:
                    shapes.append(create_shape(line))
                except ValueError as e:
                    print("Пропущено рядок:", line.strip())
                    print("Причина:", e)

    if not shapes:
        print("Немає коректних фігур")
        return

    max_area_shape = max(shapes, key=lambda s: s.area())
    max_perimeter_shape = max(shapes, key=lambda s: s.perimeter())

    print("Max area:", max_area_shape.area())
    print("Max perimeter:", max_perimeter_shape.perimeter())

process_file("input01.txt")