class Quadrangle:
    def __init__(self, line1, line2, line3, angle1, angle2):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.anle1 = angle1
        self.anle2 = angle2

class Paralelogram(Quadrangle):
    def __init__(self, line1, line2, angle):
        Quadrangle.__init__(self, line1, line2, line1, angle, 180 - angle)

class Rectangle(Paralelogram):
    def __init__(self, line1, line2):
        Paralelogram.__init__(self, line1, line2, 90)


class Romb(Paralelogram):
    def __init__(self, line, angle):
        Paralelogram.__init__(self, line, angle)

class Squere(Rectangle, Romb):
    def __init__(self, line):
        Rectangle.__init__(self, line, line)
        Romb.__init__(self, line, 90)