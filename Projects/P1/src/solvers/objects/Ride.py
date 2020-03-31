from .Position import Position


class Ride(object):
    def __init__(self, number, start_x, start_y, dest_x, dest_y, earliest, latest):
        self.number = int(number)
        self.start_position = Position(start_x, start_y)
        self.destination_position = Position(dest_x, dest_y)
        self.earliest = int(earliest)
        self.latest = int(latest)
        self.distance = self.start_position.distance(self.destination_position)
        self.car = None
        self.score = 0

    def __hash__(self):
        return self.number

    def __str__(self):
        return '[{}] from {} to {} via car {}'.format(self.number, self.start_position,
                                                      self.destination_position, self.car.number)

    def __eq__(self, other):
        if other.__class__.__name__ is not self.__class__.__name__:
            return False

        return self.number == other.number
