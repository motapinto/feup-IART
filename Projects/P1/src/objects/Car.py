from src.objects.Position import Position
from src.objects.Ride import Ride


class Car(object):
    def __init__(self, number) -> None:
        super().__init__()
        self.number = int(number)
        self.position = Position(0, 0)
        self.rides = []
        self.current_t = 0

    def add_ride(self, ride: Ride, bonus) -> None:
        time = max(ride.earliest, self.current_t + self.position.distance(ride.start_position))
        ride.car = self
        score = 0

        if time == ride.earliest:
            score += int(bonus)

        self.current_t = time + ride.start_position.distance(ride.destination_position)

        if self.current_t < ride.latest:
            score += ride.start_position.distance(ride.destination_position)

        ride.score = score

        self.rides.append(ride)
        self.position = ride.destination_position
