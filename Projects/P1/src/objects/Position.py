class Position(object):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = int(x)
        self.y = int(y)

    def __str__(self) -> str:
        return '({},{})'.format(self.x, self.y)

    def distance(self, position) -> int:
        if position.__class__ != Position:
            return -1

        return abs(self.x - position.x) + abs(self.y - position.y)
