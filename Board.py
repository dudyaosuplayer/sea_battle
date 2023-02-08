from Ship import Ship
from Dot import Dot
from Exceptions import BoardException, BoardWrongShipException, BoardOutException, BoardUsedException


class Board:
    def __init__(self, hid=False, size=6):
        self.hid = hid
        self.size = size
        self.count = 0
        self.field = [["O"]*size for _ in range(size)]
        self.busy = []
        self.ships = []

    def __str__(self):
        res = ''
        res += '  | 1 | 2 | 3 | 4 | 5 | 6 |'
        for i, row in enumerate(self.field):
            res += f"\n{i+1} | " + " | ".join(row) + " | "

        if self.hid:
            res = res.replace("■", "O")

        return res

    def out(self, d):
        return not((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def contour(self, ship, verb=False):
        near = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 0), (0, 1),
                (1, -1), (1, 0), (1, 1)
                ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.y + dy, d.x + dx)
                if not(self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.y][cur.x] = '.'
                    self.busy.append(cur)

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.y][d.x] = '■'
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d):
        if self.out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.y][d.x] = 'X'
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print('Корабль уничтожен!')
                    return False
                else:
                    print('Корабль ранен!')
                    return True

        self.field[d.y][d.x] = 'T'
        print('Мимо!')
        return False

    def begin(self):
        self.busy = []

    def defeat(self):
        return self.count == len(self.ships)
