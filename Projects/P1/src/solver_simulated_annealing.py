import sys
import random
import math
from src.files import parse_input, dump_rides
from src.objects.Car import Car

# 1st file instant - 10
# 2nd file instant - +- 95k
# 3rd file takes 00:04:30 -
# 4th file takes 00:04:46 -
# 5th file takes 00:04:35 -
# all combined take 00:13:51 -

global_score = 0


def run(filename):
    global global_score
    file = "../assets/input/" + filename
    rides, rows, cols, n_vehicles, bonus, t = parse_input(file + ".in")
    cars = [Car(i + 1) for i in range(n_vehicles)]

    tk = len(rides)
    while len(rides) > 0:
        chosen_car, chosen_ride = simulated_annealing(cars, rides, bonus, tk)
        chosen_car.add_ride(chosen_ride, bonus)
        rides.remove(chosen_ride)
        tk = random.uniform(0.3, 0.7) * tk

    dump_rides(file + ".out", cars)

    score = 0
    for car in cars:
        for ride in car.rides:
            score += ride.score

    global_score += score
    print("Score for file {} -->\t\t{}".format(filename, score))


def simulated_annealing(cars, rides, bonus, tk):
    best_car = min(cars, key=lambda car_in_cars: car_in_cars.current_t)
    best_ride = rides[0]
    best_score = score_ride(best_car, best_ride, bonus)

    Mk = (len(cars) * len(rides) * math.sqrt(tk))

    for m in range(0, int(Mk)):
        next_car = random.choice(cars)
        next_ride = random.choice(rides)
        ride_score = score_ride(next_car, next_ride, bonus)

        if next_car.position == best_car.position and next_car.current_t == best_car.current_t\
                and next_ride is best_ride:
            continue

        if ride_score > best_score:
            best_score = ride_score
            best_car = next_car
            best_ride = next_ride

        elif random.random() <= math.exp((ride_score - best_score)/tk):
            print(math.exp((ride_score - best_score) / tk))
            best_score = ride_score
            best_car = next_car
            best_ride = next_ride

    return best_car, best_ride


def score_ride(car_to_score, ride_to_score, bonus_to_score):
    drive_distance = ride_to_score.start_position.distance(ride_to_score.destination_position)
    pick_distance = car_to_score.position.distance(ride_to_score.start_position)
    wait_time = max(0, ride_to_score.earliest - (car_to_score.current_t + pick_distance))
    on_time = pick_distance + car_to_score.current_t <= ride_to_score.earliest

    return drive_distance - pick_distance - wait_time + (bonus_to_score if on_time else 0)


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
