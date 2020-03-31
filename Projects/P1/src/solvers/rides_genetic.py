import random
from .files import parse_input, dump_rides
from .objects.CarGeneticRides import CarGeneticRides
from .objects.Rides import Rides
from .objects.FIFO import FIFO

# trial run
# population = 500 | pooling_size = 200 | generations = 6 | mutation rate = 0.01
# a_example            time 000.0473s	score 10
# b_should_be_easy     time 005.0147s	score 169,605
# c_no_hurry           time 133.6090s	score 6,784,771
# d_metropolis         time 175.1362s	score 4,307,082
# e_high_bonus         time 237.6653s	score 15,899,362
# Global score is 27,160,830
# Total runtime is 551.4726s

# constants
POPULATION_SIZE = 500
POOLING_SIZE = 0.4 * POPULATION_SIZE
CONSTANT_GENERATION_NUMBER = 6
MUTATION_RATE = 0.01


def print_rides_genetic_info():
    print("\nRIDES GENETIC")
    print("{} {}".format("Population Size:".ljust(25, ' '), POPULATION_SIZE))
    print("{} {}".format("Pooling Size:".ljust(25, ' '), int(POOLING_SIZE)))
    print("{} {}".format("Mutation Rate:".ljust(25, ' '), MUTATION_RATE))
    print("{} {}\n".format("Number of Generations:".ljust(25, ' '), CONSTANT_GENERATION_NUMBER))


# toggle comment lines 43,44 and 67,68 to show or hide progression prints
def rides_genetic(file):
    rides, rows, cols, n_vehicles, bonus, t = parse_input(file + ".in")
    CarGeneticRides.BONUS = bonus
    Rides.N_RIDES = len(rides)
    Rides.N_CARS = n_vehicles

    population = [Rides(rides) for i in range(POPULATION_SIZE)]
    generation = 1
    max_fitness_rides = population[0]
    fitness_pile = FIFO(CONSTANT_GENERATION_NUMBER)
    fitness_pile.put(max_fitness_rides.calculate_fitness())
    # print("Rides -- generation " + str(generation) + " -- max fitness (" +
    #       str(max_fitness_rides.fitness) + ")")

    while not fitness_pile.is_constant():
        for rides in population:
            rides.calculate_fitness()

        population.sort(key=lambda rides_elem: rides_elem.fitness, reverse=True)

        if population[0].fitness > max_fitness_rides.fitness:
            max_fitness_rides = population[0]
        fitness_pile.put(max_fitness_rides.fitness)

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
        # print("Rides -- generation " + str(generation) + " -- max fitness (" +
        #       str(max_fitness_rides.fitness) + ")")

    dump_rides(file + ".out", max_fitness_rides.cars)

    return max_fitness_rides.fitness
