class Game:
    def __init__(self, player1, player2, field1, field2):
        self.player1 = player1
        self.player2 = player2
        self.field1 = field1
        self.field2 = field2

    def deployment(self):
        pass

    def start_game(self):
        while True:
            self.player1.step()
            while self.field2.hitting() and not self.player1.is_winner():
                self.player1.step()
            if self.player1.is_winner():
                print('Player1 is winner!!!')
                break
            self.player2.step()
            while self.field1.hitting() and not self.player2.is_winner():
                self.player2.step()
            if self.player2.is_winner():
                print('Player2 is winner!!!')
                break


class Player:
    def __init__(self, field, mark):
        self.field = field
        self.mark = mark

    def step(self):
        pass

    def is_winner(self):
        return self.field.is_over_of_ships(self.mark)


class Human(Player):
    def __init__(self, field, mark):
        Player.__init__(self, field, mark)

    def step(self):
        self.field.show()
        x = int(input("x: \n"))  # validation is needed
        y = int(input("y: \n"))
        # validation: is cell free?
        self.field.hitting(x, y)


class Computer(Player):
    def __init__(self, field, mark):
        Player.__init__(self, field, mark)

    #logic of Artificial Intelligence
    def step(self):
        x, y = self.field.find_free_cell()
        self.field.set_mark(x, y, self.mark)


class Field:
    def __init__(self):
        self.cells = []
        for i in range(0, 10):
            temp = []
            for j in range(0, 10):
                temp.append(Cell())
            self.cells.append(temp)


    def hitting(self, x, y):
        if self.cells[x][y].status == 1:
            return True



class Cell:
    def __init__(self):
        self.status = "0"


def main():
    field1 = Field()
    field2 = Field()
    player1 = Human(field1, "X")
    player2 = Computer(field2, "O")
    game = Game(player1, player2, field)
    game.start_game()


main()