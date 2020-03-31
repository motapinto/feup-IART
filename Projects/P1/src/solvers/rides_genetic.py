import random
from src.files import parse_input, dump_rides, group
from src.objects.CarGeneticRides import CarGeneticRides
from src.objects.Rides import Rides
from src.objects.FIFO import FIFO

# a_example           TIME 0.1981s                     SCORE 10
# b_should_be_easy    TIME 18.9263s                    SCORE 172,159
# c_no_hurry          TIME 1585.7304s (+- 26.43 min)   SCORE 6,826,488
# d_metropolis        TIME 559.4747s   (+- 9.33 min)   SCORE 4,352,611
# e_high_bonus        TIME 377.7967s   (+- 6.30 min)   SCORE 15,995,783
# global score is     27,347,051
# total runtime is    2542.1263s (+- 42.4 min)

# constants
POPULATION_SIZE = 2000
POOLING_SIZE = 0.4 * POPULATION_SIZE
CONSTANT_GENERATION_NUMBER = 6
MUTATION_RATE = 0.01


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

    print(filename + ": Rides -- generation " + str(generation) + " -- max fitness (" +
          str(max_fitness_rides.fitness) + ")")

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
        print(filename + ": Rides -- generation " + str(generation) + " -- max fitness (" +
              str(max_fitness_rides.fitness) + ")")

    dump_rides(file + ".out", max_fitness_rides.cars)

    return max_fitness_rides.fitness
