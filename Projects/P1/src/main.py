from src.files import group
from src.solvers.car_genetic import car_genetic
from src.solvers.hill_climbing import hill_climbing
from src.solvers.rides_genetic import rides_genetic
from src.solvers.simulated_annealing import simulated_annealing
from src.solvers.greedy import greedy

import sys
import time


def run(algorithm):
    global_score = 0

    if len(sys.argv) == 3:
        start_time = time.time()
        score = algorithm("../assets/input/" + sys.argv[2])
        print(sys.argv[2] + " \t\ttime {:.4f}s \t\tscore {}".
              format(time.time() - start_time, group(score)))

    else:
        # save start time in start to count total time
        start_time = time.time()
        start = start_time
        score = algorithm("../assets/input/a_example")
        global_score += score
        print("a_example \t\t\ttime {:.4f}s \t\tscore {}".format(time.time() - start_time, group(score)))

        start_time = time.time()
        score = algorithm("../assets/input/b_should_be_easy")
        global_score += score
        print("b_should_be_easy \ttime {:.4f}s \t\tscore {}".format(time.time() - start_time, group(score)))

        start_time = time.time()
        score = algorithm("../assets/input/c_no_hurry")
        global_score += score
        print("c_no_hurry \t\t\ttime {:.4f}s \t\tscore {}".format(time.time() - start_time, group(score)))

        start_time = time.time()
        score = algorithm("../assets/input/d_metropolis")
        global_score += score
        print("d_metropolis \t\ttime {:.4f}s \t\tscore {}".format(time.time() - start_time, group(score)))

        start_time = time.time()
        score = algorithm("../assets/input/e_high_bonus")
        global_score += score
        print("e_high_bonus \t\ttime {:.4f}s \t\tscore {}".format(time.time() - start_time, group(score)))

        print("Global score is \t{}".format(group(global_score)))
        print("Total runtime is \t{:.4f}s".format(time.time() - start))


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("python main.py <algorithm> <specific file>\t -> For a specific file")
        print("python main.py <algorithm>\t\t\t\t\t -> For all test files\n")
        print("algorithm options : car_genetic | greedy | hill_climbing  | rides_genetic | simulated_annealing")
        print("file options      : a_example | b_should_be_easy | c_no_hurry | d_metropolis | e_high_bonus\n")
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
