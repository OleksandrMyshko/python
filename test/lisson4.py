class Point:
    def __init__(self, x1, y1):
        self.x = x1
        self.__dict__['x'] = x1
        self.y = y1
        self.__dict__['y'] = y1
def main():
    p = Point(3,4)

    print(p.x, p.y)
    print(p.__dict__['x'])
    print(p.__dict__['y'])
    print(p.__dict__)
    p1 = Point(5,6)
    print(p1.x, p1.y)


main()


