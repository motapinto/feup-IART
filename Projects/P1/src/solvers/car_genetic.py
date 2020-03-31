import sys
import random
import time

from src.files import parse_input, dump_rides, group
from src.objects.Car import Car
from src.objects.FIFO import FIFO

# a_example           TIME 0.1681s                      SCORE 10
# b_should_be_easy    TIME 59.7397s    (+- 1.0 min)     SCORE 176,877
# c_no_hurry          TIME 6767.7762s  (+- 112.8 min)   SCORE 11,048,950
# d_metropolis        TIME 2767.8569s  (+- 46.13 min)   SCORE 8,678,841
# e_high_bonus        TIME 6332.6728s  (+- 105.5 min)   SCORE 21,243,463
# global score is 41,148,141
# total runtime is 15928.2139s (+- 265.5 min --> +- 04:25:29)

# final score
global_score = 0

# constants
POPULATION_SIZE = 2000
POOLING_SIZE = 0.001 * POPULATION_SIZE
CONSTANT_GENERATION_NUMBER = 5
MUTATION_RATE = 0.01


def run(filename):
    global global_score
    file = "../../assets/input/" + filename
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

        # print(filename + ": Car " + str(i + 1) + " -- generation " + str(generation) + " -- max fitness (" +
        #       str(max_fitness_car.fitness)+")")

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
            # print(filename + ": Car " + str(i + 1) + " -- generation " + str(generation) + " -- max fitness (" + str(
            #        max_fitness_car.fitness) + ")")

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

    global_score += score


if __name__ == '__main__':
    print("\nGENETIC (CAR)\n")
    print("Population size:", POPULATION_SIZE)
    print("Pooling size:", POOLING_SIZE)
    print("Mutation rate:", MUTATION_RATE)
    print("Generation number:", CONSTANT_GENERATION_NUMBER, "\n")

    if len(sys.argv) > 1:
        start_time = time.time()
        run(sys.argv[1])
        print(sys.argv[1] + " \t\t\ttime {:.4f}s with score {}".
              format(time.time() - start_time, group(global_score)))

    else:
        # save start time in S for later
        start_time = time.time()
        S = start_time

        run("a_example")
        print("a_example \t\t\ttime {:.4f}s with score {}".
              format(time.time() - start_time, group(global_score)))

        start_time = time.time()
        last_global_score = global_score
        run("b_should_be_easy")
        print("b_should_be_easy \ttime {:.4f}s with score {}".
              format(time.time() - start_time, group(global_score - last_global_score)))

        start_time = time.time()
        last_global_score = global_score
        run("c_no_hurry")
        print("c_no_hurry \t\t\ttime {:.4f}s with score {}".
              format(time.time() - start_time, group(global_score - last_global_score)))

        start_time = time.time()
        last_global_score = global_score
        run("d_metropolis")
        print("d_metropolis \t\ttime {:.4f}s with score {}".
              format(time.time() - start_time, group(global_score - last_global_score)))

        start_time = time.time()
        last_global_score = global_score

        run("e_high_bonus")
        print("e_high_bonus \t\ttime {:.4f}s with score {}".
              format(time.time() - start_time, group(global_score - last_global_score)))

        print("Global score is {}".format(group(global_score)))
        print("Total runtime is {:.4f}s".format(time.time() - S))
