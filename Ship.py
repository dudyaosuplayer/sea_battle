from Dot import Dot


class Ship:
    def __init__(self, bow, lenth, o):
        self.bow = bow
        self.lenth = lenth
        self.o = o
        self.lives = lenth

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.lenth):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i

            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_y, cur_x))
        return ship_dots

    def shooten(self, shot):
        return shot in self.dots


