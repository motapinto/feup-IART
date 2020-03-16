from src.objects.Position import Position
from src.objects.Ride import Ride


class Car(object):
    def __init__(self, number) -> None:
        self.number = int(number)
        self.position = Position(0, 0)
        self.rides = []
        self.current_t = 0

    def add_ride(self, ride: Ride, bonus) -> None:
        # time it takes the car to get to position
        time = max(ride.earliest, self.current_t + self.position.distance(ride.start_position))
        ride.car = self

        # for every ride that starts precisely on time you will earn and additional bonus
        if time == ride.earliest:
            ride.score += int(bonus)

        # updates the time after completing the ride
        self.current_t = time + ride.start_position.distance(ride.destination_position)

        # for every ride that finishes on time you will earn points proportional to the distance of that ride
        if self.current_t < ride.latest:
            ride.score += ride.start_position.distance(ride.destination_position)

        self.rides.append(ride)
        self.position = ride.destination_position
