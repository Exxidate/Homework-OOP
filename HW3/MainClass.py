import math

class Figure:
    def dimension(self):
        raise NotImplementedError

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        if self.dimension() == 2:
            return self.square()
        else:
            return self._volume()

    def _volume(self):
        return None

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError(f"Invalid triangle: {a}, {b}, {c}")

    def dimension(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def dimension(self):
        return 2

    def perimeter(self):
        return 2*(self.a + self.b)

    def square(self):
        return self.a * self.b


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r**2

class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 3

    def squareSurface(self):
        return 4 * math.pi * self.r**2

    def _volume(self):
        return (4/3)*math.pi*self.r**3


class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h

    def dimension(self):
        return 3

    def squareBase(self):
        return super().square()

    def squareSurface(self):
        l = math.sqrt(self.r**2 + self.h**2)
        return math.pi*self.r*(self.r + l)

    def _volume(self):
        return (1/3)*math.pi*self.r**2*self.h