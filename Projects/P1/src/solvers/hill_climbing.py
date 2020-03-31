import sys
import time

from src.files import parse_input, dump_rides, group
from src.objects.Rides import Rides
from src.objects.CarGeneticRides import CarGeneticRides

# a_example           TIME 0.0008s                    SCORE 4
# b_should_be_easy    TIME 0.5055s                    SCORE 164,636
# c_no_hurry          TIME 415.8198s  (+- 6.93 min)   SCORE 6,704,699
# d_metropolis        TIME 592.1818s  (+- 17.2 min)   SCORE 4,189,112
# e_high_bonus        TIME 1032.0356s (+- 32.5 min)   SCORE 15,706,741
# global score is     26,765,192
# total runtime is    1950.5438s (+- 32.5 min)

global_score = 0


def run(filename):
    global global_score
    file = "../../assets/input/" + filename
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
    print("\nHILL CLIMBING")

    if len(sys.argv) > 1:
        start_time = time.time()
        run(sys.argv[1])
        print(sys.argv[1] + " \t\t\ttime {:.6f}s with score {}".
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
