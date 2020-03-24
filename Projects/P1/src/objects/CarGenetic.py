from src.objects.Position import Position
from src.objects.Ride import Ride

import random


class CarGenetic(object):
    BONUS = 0
    RIDES = 0
    RIDES_PER_CAR = 0

    def __init__(self, rides=None, number=0):
        self.number = number
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
            ride.score = 0
            self.current_t += self.position.distance(ride.start_position)
            self.position = ride.start_position

            # time it takes the car to get to position
            time = max(ride.earliest, self.current_t + self.position.distance(ride.start_position))

            # for every ride that starts precisely on time you will earn and additional bonus
            if time == ride.earliest:
                ride.score += int(self.BONUS)

            # updates the time after completing the ride
            self.current_t = time + ride.start_position.distance(ride.destination_position)

            # for every ride that finishes on time you will earn points proportional to the distance of that ride
            if self.current_t < ride.latest:
                ride.score += ride.start_position.distance(ride.destination_position)

            self.position = ride.destination_position
            self.fitness += ride.score

    def reproduce(self, parent):
        self.sort_rides()
        parent.sort_rides()

        childs = []
        i = random.randint(0, self.RIDES_PER_CAR)
        childs.append(CarGenetic(self.rides[0:i] + parent.rides[i:len(self.rides)]))
        childs.append(CarGenetic(parent.rides[0:i] + self.rides[i:len(self.rides)]))
        return childs

    def mutate(self):
        for ride in self.rides:
            if random.random() < 0.01:
                ride = random.choice(self.RIDES)

    def normalize(self):
        self.rides = list(set(self.rides))
        self.sort_rides()

    def add_ride(self, ride: Ride):
        self.rides.append(ride)
