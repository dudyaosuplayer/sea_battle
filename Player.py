from random import randint
from Board import Board
from Dot import Dot
from Ship import Ship
from Exceptions import BoardException, BoardWrongShipException, BoardOutException, BoardUsedException


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f'Ход компьютера: {d.y+1} {d.x+1}')
        return d


class User(Player):
    def ask(self):
        while True:
            cords = input('Ваш ход: ').split()

            if len(cords) != 2:
                print('Введите 2 координаты!')
                continue

            y, x = cords

            if not(y.isdigit()) or not(x.isdigit()):
                print('Введите числа!')
                continue

            y, x = int(y), int(x)

            return Dot(y-1, x-1)
