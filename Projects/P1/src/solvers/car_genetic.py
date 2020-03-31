import random
from .files import parse_input, dump_rides
from .objects.Car import Car
from .objects.FIFO import FIFO

# trial run
# population = 500 | pooling_size = 200 | generations = 6 | mutation rate = 0.01
# a_example            time 000.0215s	score 10
# b_should_be_easy     time 004.5540s	score 176,877
# c_no_hurry           time 587.2439s	score 9,550,340
# d_metropolis         time 396.5267s	score 8,251,484
# e_high_bonus         time 631.7614s	score 21,168,560
# Global score is 39,147,271
# Total runtime is 1620.1077s

# final score
global_score = 0

# constants
POPULATION_SIZE = 500
POOLING_SIZE = 0.4 * POPULATION_SIZE
CONSTANT_GENERATION_NUMBER = 6
MUTATION_RATE = 0.01


def print_car_genetic_info():
    print("\nCAR GENETIC")
    print("{} {}".format("Population Size:".ljust(25, ' '), POPULATION_SIZE))
    print("{} {}".format("Pooling Size:".ljust(25, ' '), int(POOLING_SIZE)))
    print("{} {}".format("Mutation Rate:".ljust(25, ' '), MUTATION_RATE))
    print("{} {}\n".format("Number of Generations:".ljust(25, ' '), CONSTANT_GENERATION_NUMBER))


# toggle comment lines 51,52 and 76,77 to show or hide progression prints
def car_genetic(file):
    rides, rows, cols, n_vehicles, bonus, t = parse_input(file + ".in")
    Car.BONUS = bonus
    Car.RIDES = rides
    Car.RIDES_PER_CAR = len(rides) // n_vehicles
    cars = []

    for i in range(n_vehicles - 1):
        population = [Car() for i in range(POPULATION_SIZE)]
        generation = 1

        max_fitness_car = population[0]
        max_fitness_car.calculate_fitness()

        fitness_pile = FIFO(CONSTANT_GENERATION_NUMBER)
        fitness_pile.put(max_fitness_car.fitness)

        # print("Car " + str(i+1) + " -- generation " + str(generation)
        #       + " -- max fitness ("+str(max_fitness_car.fitness)+")")

        while not fitness_pile.is_constant():
            for car in population:
                car.calculate_fitness()

            population.sort(key=lambda car_elem: car_elem.fitness, reverse=True)

            if population[0].fitness > max_fitness_car.fitness:
                max_fitness_car = population[0]

            fitness_pile.put(max_fitness_car.fitness)

            new_population = []
            while len(new_population) < POPULATION_SIZE:
                children = population[random.randrange(0, POOLING_SIZE)].reproduce(
                    population[random.randrange(0, POOLING_SIZE)])
                children[0].mutate()
                children[1].mutate()
                new_population.append(children[0])
                new_population.append(children[1])

            population = new_population
            generation += 1
            # print("Car " + str(i+1) + " -- generation " + str(generation)
            #       + " -- max fitness ("+str(max_fitness_car.fitness)+")")

        max_fitness_car.normalize()
        cars.append(max_fitness_car)
        for ride in max_fitness_car.rides:
            Car.RIDES.remove(ride)

    last_car = Car(rides)
    last_car.normalize()
    cars.append(last_car)

    dump_rides(file + ".out", cars)

    score = 0
    for car in cars:
        car.calculate_fitness()
        for ride in car.rides:
            score += ride.score

    return score
