import sys
import random
from src.files import parse_input, dump_rides
from src.objects.Car import Car

# 1st file instant - 10
# 2nd file instant - 176877
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

    while len(rides) > 0:
        # chooses the car with less current_t
        chosen_car = min(cars, key=lambda car_in_cars: car_in_cars.current_t)
        # chooses the ride that gives the highest score
        chosen_ride = hill_climbing_random_choose_ride(chosen_car, rides, bonus)
        chosen_car.add_ride(chosen_ride, bonus)
        print(chosen_ride)
        rides.remove(chosen_ride)

    dump_rides(file + ".out", cars)

    score = 0
    for car in cars:
        for ride in car.rides:
            score += ride.score

    global_score += score
    print("Score for file {} -->\t\t{}".format(filename, score))


def hill_climbing_basic_choose_ride(car, rides, bonus):
    best_ride = rides[0]
    max_score = score_ride(car, rides[0], bonus)
    for ride in rides:
        ride_score = score_ride(car, ride, bonus)
        if ride_score > max_score:
            max_score = ride_score
            best_ride = ride
        else:
            break
    return best_ride


def hill_climbing_random_choose_ride(car, rides, bonus):
    best_ride = random.choice(rides)
    max_score = score_ride(car, rides[0], bonus)

    while True:
        next_ride = random.choice(rides)
        ride_score = score_ride(car, next_ride, bonus)
        if ride_score > max_score:
            max_score = ride_score
            best_ride = next_ride
        else:
            break

    return best_ride


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
