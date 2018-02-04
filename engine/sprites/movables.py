from base import Square

class Movable(object):
    def move_left(self, px):
        if "move_left" in self.capabilities:
            self.rect.x -= px

    def move_right(self, px):
        if "move_right" in self.capabilities:
            self.rect.x += px

    def move_up(self, px):
        if "move_up" in self.capabilities:
            self.rect.y -= px

    def move_down(self, px):
        if "move_down" in self.capabilities:
            self.rect.y += px



class MoveSquare(Square, Movable):
    def __init__(self, size, pos, color):
        super(MoveSquare, self).__init__(size,pos,color)
        self.add_capabilities("move_down", "move_left", "move_right")