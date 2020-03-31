import random
from src.files import parse_input, dump_rides, group
from src.objects.Rides import Rides
from src.objects.CarGeneticRides import CarGeneticRides

# a_example           TIME 0.0019s     SCORE 4
# b_should_be_easy    TIME 0.0534s     SCORE 162,600
# c_no_hurry          TIME 2.1595s     SCORE 6,746,130
# d_metropolis        TIME 2.4109s     SCORE 4,181,606
# e_high_bonus        TIME 2.2745s     SCORE 15,681,615
# global score is     26,771,955
# total runtime is    6.9004s


def simulated_annealing(file):
    rides, rows, cols, n_vehicles, bonus, t = parse_input(file + ".in")

    CarGeneticRides.BONUS = bonus
    Rides.N_RIDES = len(rides)
    Rides.N_CARS = n_vehicles

    solution = Rides(rides)
    solution.calculate_fitness()
    previous_score = 0
    temperature = len(rides)

    while temperature > 0.1 or previous_score != solution.fitness:
        previous_score = solution.fitness
        solution.simulated_annealing(temperature)
        temperature = random.uniform(0.8, 0.99) * temperature

    dump_rides(file + ".out", solution.cars)
    return solution.fitness
