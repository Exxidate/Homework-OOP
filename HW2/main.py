import turtle
import random

class Petal:
    def __init__(self, size=50, color="red"):
        self.size = size
        self.color = color

    def draw(self, t):
        t.color(self.color)
        t.begin_fill()
        for _ in range(2):
            t.circle(self.size, 60)
            t.left(120)
        t.end_fill()


class Leaf:
    def __init__(self, size=40, color="green"):
        self.size = size
        self.color = color

    def draw(self, t):
        t.color(self.color)
        t.begin_fill()
        t.circle(self.size, 60)
        t.left(120)
        t.circle(self.size, 60)
        t.end_fill()


class Stem:
    def __init__(self, length=100, color="green"):
        self.length = length
        self.color = color

    def draw(self, t):
        t.color(self.color)
        t.width(3)
        t.left(90)
        t.forward(self.length)


class Flower:
    def __init__(self, petals=6):
        self.petals = [Petal(random.randint(30, 60),
                            random.choice(["red", "yellow", "pink", "purple"]))
                       for _ in range(petals)]
        self.leaf = Leaf()
        self.stem = Stem()

    def draw(self, x, y):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.penup()
        t.goto(x, y)
        t.pendown()

        self.leaf.draw(t)
        t.left(120)

        self.stem.draw(t)

        for _ in self.petals:
            self.petals[0].draw(t)
            t.left(360 / len(self.petals))

        t.color("orange")
        t.begin_fill()
        t.circle(5)
        t.end_fill()

screen = turtle.Screen()



for _ in range(5):
    f = Flower(random.randint(5, 8))
    f.draw(random.randint(-200, 200), random.randint(-100, 100))

turtle.done()