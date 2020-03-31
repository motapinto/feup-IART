from .files import parse_input, dump_rides
from .objects.Rides import Rides
from .objects.CarGeneticRides import CarGeneticRides

# a_example           TIME 0.0008s                    SCORE 4
# b_should_be_easy    TIME 0.5055s                    SCORE 164,636
# c_no_hurry          TIME 415.8198s  (+- 6.93 min)   SCORE 6,704,699
# d_metropolis        TIME 592.1818s  (+- 17.2 min)   SCORE 4,189,112
# e_high_bonus        TIME 1032.0356s (+- 32.5 min)   SCORE 15,706,741
# global score is     26,765,192
# total runtime is    1950.5438s (+- 32.5 min)


def hill_climbing(file):
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
    return solution.fitness
