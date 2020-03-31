from .files import parse_input, dump_rides
from .objects.Rides import Rides
from .objects.CarGeneticRides import CarGeneticRides

# trial run
# a_example            time 000.0014s	score 4
# b_should_be_easy     time 000.8203s	score 167,601
# c_no_hurry           time 534.0957s	score 6,673,587
# d_metropolis         time 581.7603s	score 4,216,626
# e_high_bonus         time 560.0255s	score 15,667,106
# Global score is 26,724,924
# Total runtime is 1676.7033s


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
