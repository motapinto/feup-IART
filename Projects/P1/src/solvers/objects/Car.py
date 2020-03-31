from .Position import Position
from .Ride import Ride
import random


class Car(object):
    BONUS = 0
    RIDES = []
    RIDES_PER_CAR = 0

    def __init__(self, rides=None):
        self.number = 0
        self.position = Position(0, 0)
        self.current_t = 0
        self.fitness = 0
        if rides is None:
            self.rides = random.sample(self.RIDES, self.RIDES_PER_CAR)
        else:
            self.rides = rides

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
            ride.score = 0

            # time it takes the car to get to position
            time = max(ride.earliest, self.current_t)

            # for every ride that starts precisely on time you will earn and additional bonus
            if time == ride.earliest:
                self.fitness += int(self.BONUS)
                ride.score += int(self.BONUS)

            # updates the time after completing the ride
            self.current_t = time + ride.distance

            # for every ride that finishes on time you will earn points proportional to the distance of that ride
            if self.current_t <= ride.latest:
                self.fitness += ride.distance
                ride.score += ride.distance

            self.position = ride.destination_position
        return self.fitness

    def reproduce(self, parent):
        self.sort_rides()
        parent.sort_rides()

        children = []
        i = random.randint(0, self.RIDES_PER_CAR)
        children.append(Car(self.rides[0:i] + parent.rides[i:len(self.rides)]))
        children.append(Car(parent.rides[0:i] + self.rides[i:len(self.rides)]))
        return children

    def mutate(self):
        for ride in self.rides:
            if random.random() < 0.01:
                ride = random.choice(self.RIDES)

    def normalize(self):
        self.rides = list(set(self.rides))
        self.sort_rides()

    def add_ride(self, ride: Ride):
        self.rides.append(ride)

    def remove_ride(self, ride: Ride):
        for ride_in_car in self.rides:
            if ride_in_car == ride:
                self.rides.remove(ride_in_car)
