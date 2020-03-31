from .Position import Position
from .Ride import Ride


class CarGeneticRides(object):
    BONUS = 0

    def __init__(self, number):
        self.number = number
        self.position = Position(0, 0)
        self.current_t = 0
        self.rides = []
        self.fitness = 0

    def sort_rides(self):
        self.rides.sort(key=lambda ride: ride.earliest + ride.distance)

    def calculate_fitness(self):
        self.position = Position(0, 0)
        self.current_t = 0
        self.fitness = 0
        self.sort_rides()

        for ride in self.rides:
            self.current_t += self.position.distance(ride.start_position)
            self.position = ride.start_position

            # time it takes the car to get to position
            time = max(ride.earliest, self.current_t)

            # for every ride that starts precisely on time you will earn and additional bonus
            if time == ride.earliest:
                self.fitness += int(self.BONUS)

            # updates the time after completing the ride
            self.current_t = time + ride.distance

            # for every ride that finishes on time you will earn points proportional to the distance of that ride
            if self.current_t <= ride.latest:
                self.fitness += ride.distance

            self.position = ride.destination_position

        return self.fitness

    def add_ride(self, ride: Ride):
        self.rides.append(ride)

    def remove_ride(self, ride: Ride):
        for ride_in_car in self.rides:
            if ride_in_car == ride:
                self.rides.remove(ride_in_car)
