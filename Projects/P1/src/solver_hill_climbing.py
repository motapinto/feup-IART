import sys
import random
import time
from src.files import parse_input, dump_rides
from src.objects.Rides import Rides
from src.objects.CarGeneticRides import CarGeneticRides

# Finished a_example: time 0.0009706020355224609 with score 10
# Finished b_should_be_easy: time 32.91826629638672 with score 156966

global_score = 0


def run(filename):
    global global_score
    file = "../assets/input/" + filename
    rides, rows, cols, n_vehicles, bonus, t = parse_input(file + ".in")

    CarGeneticRides.BONUS = bonus
    Rides.N_RIDES = len(rides)
    Rides.N_CARS = n_vehicles

    solution = Rides(rides)
    solution.calculate_fitness()
    previous_score = 0

    while previous_score < solution.fitness:
        previous_score = solution.fitness
        solution = solution.hill_climbing_random()

    dump_rides(file + ".out", solution.cars)
    global_score += solution.fitness


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
