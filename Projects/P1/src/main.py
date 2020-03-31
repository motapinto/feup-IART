from src.files import group
from src.solvers.car_genetic import car_genetic
from src.solvers.hill_climbing import hill_climbing
from src.solvers.rides_genetic import rides_genetic
from src.solvers.simulated_annealing import simulated_annealing
from src.solvers.greedy import greedy

import sys
import time

# final score
global_score = 0


def run(algorithm):
    if len(sys.argv) == 3:
        start_time = time.time()
        algorithm(sys.argv[2])
        print(sys.argv[2] + " \t\t\ttime {:.4f}s with score {}".
              format(time.time() - start_time, group(global_score)))

    else:
        # save start time in S for later
        start_time = time.time()
        start = start_time

        algorithm("a_example")
        print("a_example \t\t\ttime {:.4f}s with score {}".
              format(time.time() - start_time, group(global_score)))

        start_time = time.time()
        last_global_score = global_score

        algorithm("b_should_be_easy")
        print("b_should_be_easy \ttime {:.4f}s with score {}".
              format(time.time() - start_time, group(global_score - last_global_score)))

        start_time = time.time()
        last_global_score = global_score

        algorithm("c_no_hurry")
        print("c_no_hurry \t\t\ttime {:.4f}s with score {}".
              format(time.time() - start_time, group(global_score - last_global_score)))

        start_time = time.time()
        last_global_score = global_score

        algorithm("d_metropolis")
        print("d_metropolis \t\ttime {:.4f}s with score {}".
              format(time.time() - start_time, group(global_score - last_global_score)))

        start_time = time.time()
        last_global_score = global_score

        algorithm("e_high_bonus")
        print("e_high_bonus \t\ttime {:.4f}s with score {}".
              format(time.time() - start_time, group(global_score - last_global_score)))

        print("Global score is {}".format(group(global_score)))
        print("Total runtime is {:.4f}s".format(time.time() - start))


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("python main.py <algorithm> <specific file>\t -> For a specific file")
        print("python main.py <algorithm>\t\t\t\t\t -> For all test files\n")
        print("algorithm options : car_genetic | greedy | hill_climbing  | rides_genetic | simulated_annealing")
        print("file options : a_example.in | b_should_be_easy.in | c_no_hurry.in | d_metropolis.in | e_high_bonus.in\n")
        print("Try again...")
        exit(1)

    if sys.argv[1] == "car_genetic":
        run(car_genetic)
    elif sys.argv[1] == "hill_climbing":
        run(hill_climbing)
    elif sys.argv[1] == "rides_genetic":
        run(rides_genetic)
    elif sys.argv[1] == "simulated_annealing":
        run(simulated_annealing)
    elif sys.argv[1] == "greedy":
        run(greedy)
