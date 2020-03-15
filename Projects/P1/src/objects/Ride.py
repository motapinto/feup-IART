from Projects.P1.src.objects.Position import Position


class Ride(object):
    def __init__(self, number, start_x, start_y, dest_x, dest_y, earliest, latest) -> None:
        super().__init__()
        self.number = int(number)
        self.start_position = Position(start_x, start_y)
        self.destination_position = Position(dest_x, dest_y)
        self.earliest = int(earliest)
        self.latest = int(latest)
        self.car = None
        self.score = 0

    def __str__(self):
        return '[{}] from {} to {}'.format(self.number, self.start_position, self.destination_position)