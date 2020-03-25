import random
import math

from src.objects.CarGeneticRides import CarGeneticRides


class Rides(object):
    N_CARS = 0
    N_RIDES = 0

    def __init__(self, rides: []):
        self.fitness = 0
        self.rides = rides
        self.cars = [CarGeneticRides(i) for i in range(Rides.N_CARS)]
        self.assign_rides()

    def reproduce(self, parent):
        children = []
        i = random.randrange(Rides.N_RIDES)
        children.append(Rides(self.rides[0:i] + parent.rides[i:len(self.rides)]))
        children.append(Rides(parent.rides[0:i] + self.rides[i:len(self.rides)]))
        return children

    def mutate(self):
        for ride in self.rides:
            if random.random() < 0.01:
                car = random.randrange(Rides.N_CARS)
                self.cars[ride.car].remove_ride(ride)
                self.cars[car].add_ride(ride)
                ride.car = car

    def calculate_fitness(self) -> int:
        self.fitness = 0
        for car in self.cars:
            self.fitness += car.calculate_fitness()

        return self.fitness

    def assign_rides(self):
        for ride in self.rides:
            if ride.car is None:
                ride.car = random.randrange(Rides.N_CARS)

            self.cars[ride.car].add_ride(ride)

    def hill_climbing_random(self):
        population = []

        for rideIndex in range(0, self.N_RIDES):
            ride = random.choice(self.rides)
            car = random.randrange(Rides.N_CARS)

            swap = ride.car
            ride.car = car

            population.append(Rides(self.rides))

            ride.car = swap

        return max(population, key=lambda elem: elem.calculate_fitness())

    def simulated_annealing(self, temperature):
        fitness = self.fitness
        Mk = (self.N_RIDES * math.sqrt(temperature + 1))

        for m in range(0, int(Mk)):
            ride = random.choice(self.rides)
            car = random.randrange(Rides.N_CARS)

            swap = ride.car
            ride.car = car

            if self.calculate_fitness() > fitness:
                return

            elif random.random() <= math.exp((self.fitness - fitness) / temperature):
                return

            self.fitness = fitness
