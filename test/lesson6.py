import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))


class Circle(Point):
    def __init__(self, x, y, r):
        Point.__init__(self, x, y)
        self.r = r

    def square(self):
        return 3.14 * self.r ** 2


def main():
    circle = Circle(10, 20, 100)
    print(circle.r, circle.x, circle.y)
    print(circle.square())
    circle2 = Circle(5, 8, 80)
    print(circle2.distance(circle))


main()
