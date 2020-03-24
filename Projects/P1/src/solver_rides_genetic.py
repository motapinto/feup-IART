import sys
import random
import time

from src.files import parse_input, dump_rides
from src.objects.CarGeneticRides import CarGeneticRides
from src.objects.Rides import Rides
from src.objects.FIFO import FIFO

# Finished a_example: time 0.37897777557373047 with score 10
# Finished b_should_be_easy: time 48.94636273384094 with score 172588
# 3rd file takes s -
# 4th file takes s -
# 5th file takes s -
# all combined take s -

# final score

global_score = 0

# constants
POPULATION_SIZE = 2000
POOLING_SIZE = 800
CONSTANT_GENERATION_NUMBER = 6
MUTATION_RATE = 0.01


def run(filename):
    global global_score
    file = "../assets/input/" + filename
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

    global_score += max_fitness_rides.fitness
    print("Score for file {} -->\t\t{}".format(filename, max_fitness_rides.fitness))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        run(sys.argv[1])

    else:
        start_time = time.time()
        run("a_example")
        print("Finished a_example: time", time.time() - start_time, "with score", global_score)

        start_time = time.time()
        last_global_score = global_score
        run("b_should_be_easy")
        print("Finished b_should_be_easy: time", time.time() - start_time, "with score",
              global_score - last_global_score)

        start_time = time.time()
        last_global_score = global_score
        run("c_no_hurry")
        print("Finished c_no_hurry: time", time.time() - start_time, "with score", global_score - last_global_score)

        start_time = time.time()
        last_global_score = global_score
        run("d_metropolis")
        print("Finished d_metropolis: time", time.time() - start_time, "with score", global_score - last_global_score)

        start_time = time.time()
        last_global_score = global_score
        run("e_high_bonus")
        print("Finished e_high_bonus: time", time.time() - start_time, "with score", global_score - last_global_score)

        print("\nGlobal score is {}".format(global_score))
