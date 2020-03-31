class Position(object):
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self) -> str:
        return '({},{})'.format(self.x, self.y)

    def __eq__(self, other) -> bool:
        if other.__class__.__name__ is not self.__class__.__name__:
            return False

        return other.x == self.x and other.y == self.y

    def distance(self, position) -> int:
        if position.__class__ != Position:
            return -1

        return abs(self.x - position.x) + abs(self.y - position.y)
