from src.objects.Position import Position
from src.objects.Ride import Ride

import random


class CarGenetic(object):
    BONUS = 0

    def __init__(self, rides=[]):
        self.position = Position(0, 0)
        self.current_t = 0
        self.fitness = 0
        self.rides = rides

    def score_ride(self, ride_to_score):
        drive_distance = ride_to_score.start_position.distance(
            ride_to_score.destination_position)
        pick_distance = self.position.distance(ride_to_score.start_position)
        wait_time = max(0, ride_to_score.earliest - (self.current_t + pick_distance))
        on_time = pick_distance + self.current_t <= ride_to_score.earliest

        return drive_distance - pick_distance - wait_time + (self.BONUS if on_time else 0)

    def sort_rides(self):
        self.rides.sort(key=lambda ride: (ride.latest-ride.destination_position.distance(
            ride.start_position)) + ride.earliest)

    def calculate_fitness(self):
        self.position = Position(0, 0)
        self.current_t = 0
        self.fitness = 0
        self.sort_rides()

        for ride in self.rides:
            ride.score = 0
            self.fitness += self.score_ride(ride)
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

    def reproduce(self, parent):
        self.sort_rides()
        parent.sort_rides()

        childs = []
        i = random.randint(0, len(self.rides))
        childs.append(CarGenetic(self.rides[0:i] + parent.rides[i:len(self.rides)]))
        childs.append(CarGenetic(parent.rides[0:i] + self.rides[i:len(self.rides)]))
        return childs

    def mutate(self, rides):
        for ride in self.rides:
            if random.random() < 0.01:
                ride = random.choice(rides)

    def normalize(self):
        self.rides = list(set(self.rides))
        self.sort_rides()

    def add_ride(self, ride: Ride, bonus):
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