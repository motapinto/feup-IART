import sys
import random
import time

from src.files import parse_input, dump_rides
from src.objects.Car import Car
from src.objects.FIFO import FIFO

# Finished a_example: time 1.4856s with score 10
# Finished b_should_be_easy: time 224.3284s with score 176877
# 3rd file takes s -
# 4th file takes s -
# 5th file takes s -
# all combined take s -

# final score
global_score = 0

# constants
POPULATION_SIZE = 5000
POOLING_SIZE = 2000
CONSTANT_GENERATION_NUMBER = 5
MUTATION_RATE = 0.01


def run(filename):
    global global_score
    file = "../assets/input/" + filename
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

        #print(filename + ": Car " + str(i + 1) + " -- generation " + str(generation) + " -- max fitness (" +
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
                childs = population[random.randrange(0, POOLING_SIZE)].reproduce(
                    population[random.randrange(0, POOLING_SIZE)])
                childs[0].mutate()
                childs[1].mutate()
                new_population.append(childs[0])
                new_population.append(childs[1])

            population = new_population
            generation += 1
            #print(filename + ": Car " + str(i + 1) + " -- generation " + str(generation) + " -- max fitness (" + str(
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
    if len(sys.argv) > 1:
        run(sys.argv[1])

    else:
        start_time = time.time()
        run("a_example")
        print("Finished a_example: \t\ttime", time.time() - start_time, "with score", global_score)

        start_time = time.time()
        last_global_score = global_score
        run("b_should_be_easy")
        print("Finished b_should_be_easy: \ttime", time.time() - start_time, "with score",
              global_score - last_global_score)

        start_time = time.time()
        last_global_score = global_score
        run("c_no_hurry")
        print("Finished c_no_hurry: \t\ttime", time.time() - start_time, "with score", global_score - last_global_score)

        start_time = time.time()
        last_global_score = global_score
        run("d_metropolis")
        print("Finished d_metropolis: \t\ttime", time.time() - start_time, "with score", global_score - last_global_score)

        start_time = time.time()
        last_global_score = global_score
        run("e_high_bonus")
        print("Finished e_high_bonus: \t\ttime", time.time() - start_time, "with score", global_score - last_global_score)

        print("\nGlobal score is {}".format(global_score))
