class Coffee:
    def __init__(self, type, price):
        self.type = type
        self.price = price


class Box:
    def __init__(self, volume, coffee):
        self.volume = volume
        self.coffee = coffee


class Lorry:
    def __init__(self):
        self.boxes = []

    def add_box(self, box):
        self.boxes.append(box)

    def total(self):
        sum = 0
        for box in self.boxes:
            sum += box.volume * box.coffee.price
        return sum


def main():
    coffee1 = Coffee('arabica', 20)
    coffee2 = Coffee('rabusta', 10)
    box1 = Box(40, coffee1)
    box2 = Box(50, coffee2)
    box3 = Box(10, coffee2)
    box4 = Box(30, coffee1)

    lorry = Lorry()
    lorry.add_box(box1)
    lorry.add_box(box2)
    lorry.add_box(box3)
    lorry.add_box(box4)

    print(lorry.total())


main()
