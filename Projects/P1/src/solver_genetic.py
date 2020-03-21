import sys
import random
from src.files import parse_input, dump_rides
from src.objects.CarGenetic import CarGenetic
from src.objects.FIFO import FIFO

# final score
global_score = 0

# constants
POPULATION_SIZE = 8000
POOLING_SIZE = 2000
CONSTANT_GENERATION_NUMBER = 5
MUTATION_RATE = 0.01


def run(filename):
    global global_score
    file = "../assets/input/" + filename
    rides, rows, cols, n_vehicles, bonus, t = parse_input(file + ".in")
    CarGenetic.BONUS = bonus
    cars = []

    for i in range(n_vehicles - 1):
        population = [CarGenetic() for i in range(POPULATION_SIZE)]
        generation = 1
        max_fitness_car = population[0]
        fitness_pile = FIFO(CONSTANT_GENERATION_NUMBER)
        fitness_pile.put(max_fitness_car.fitness)

        while not fitness_pile.is_constant():
            for car in population:
                car.calculate_fitness()

            population.sort(key=lambda car_elem: car_elem.fitness, reverse=True)

            if population[0].fitness > max_fitness_car.fitness:
                max_fitness_car = population[0]
            fitness_pile.put(max_fitness_car.fitness)

            new_population = []
            while len(new_population) < POPULATION_SIZE:
                childs = population[random.randint(0, POOLING_SIZE - 1)].reproduce(
                    population[random.randint(0, POOLING_SIZE - 1)])
                childs[0].mutate(rides)
                childs[1].mutate(rides)
                new_population.append(childs[0])
                new_population.append(childs[1])

            population = new_population
            generation += 1

            max_fitness_car.normalize()
            cars.append(max_fitness_car)
            for ride in max_fitness_car.rides:
                rides.remove(ride)

    last_car = CarGenetic(rides)
    last_car.normalize()
    cars.append(last_car)

    dump_rides(file + ".out", cars)


    score = 0
    for car in cars:
        car.calculate_fitness()
        for ride in car.rides:
            score += ride.score


    global_score += score
    print("Score for file {} -->\t\t{}".format(filename, score))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        run(sys.argv[1])

    else:
        run("a_example")
        run("b_should_be_easy")
        run("c_no_hurry")
        run("d_metropolis")
        run("e_high_bonus")

        print("\nGlobal score is {}".format(global_score))
