from .files import parse_input, dump_rides
from .objects.CarGeneticRides import CarGeneticRides

# trial run
# a_example            time 0.0013s	    score 10
# b_should_be_easy     time 0.1174s	    score 176,877
# c_no_hurry           time 114.0726s	score 7,564,919
# d_metropolis         time 109.4057s	score 4,689,009
# e_high_bonus         time 109.5141s	score 21,465,945
# Global score is 33,896,760
# Total runtime is 333.1113s


def greedy(file):
    rides, rows, cols, n_vehicles, bonus, t = parse_input(file + ".in")
    cars = [CarGeneticRides(i + 1) for i in range(n_vehicles)]
    CarGeneticRides.BONUS = bonus

    while len(rides) > 0:
        # chooses the car with less current_t
        chosen_car = min(cars, key=lambda car_in_cars: car_in_cars.current_t)
        # chooses the ride that gives the highest score
        chosen_ride = max(rides, key=lambda ride_in_rides: score_ride(chosen_car, ride_in_rides, bonus))
        chosen_car.add_ride(chosen_ride)
        chosen_car.calculate_fitness()
        rides.remove(chosen_ride)

    dump_rides(file + ".out", cars)

    score = 0
    for car in cars:
        score += car.fitness

    return score


# Evaluation function
def score_ride(car_to_score, ride_to_score, bonus_to_score):
    drive_distance = ride_to_score.start_position.distance(ride_to_score.destination_position)
    pick_distance = car_to_score.position.distance(ride_to_score.start_position)
    wait_time = max(0, ride_to_score.earliest - (car_to_score.current_t + pick_distance))
    on_time = pick_distance + car_to_score.current_t <= ride_to_score.earliest

    return drive_distance - pick_distance - wait_time + (bonus_to_score if on_time else 0)
