import sys
from src.files import parse_input, dump_rides
from src.objects.Car import Car

global_score = 0
# 1st and 2nd files are almost instant
# 3rd file takes 00:04:30
# 4th file takes 00:04:46
# 5th file takes 00:04:35
# all combined take 00:13:51


def special_print(n):
    number = str(n)
    result = ""
    for i in range(len(number), 0, -1):
        if ((i + 1) % 4) == 0:
            result += ","
        result += number[i - 1]

    return result[::-1]


def run(filename):
    global global_score
    file = "../assets/input/" + filename
    rides, rows, cols, n_vehicles, bonus, t = parse_input(file + ".in")
    cars = [Car(i + 1) for i in range(n_vehicles)]

    while len(rides) > 0:
        chosen_car = min(cars, key=lambda car_in_cars: car_in_cars.current_t)
        chosen_ride = max(rides, key=lambda ride_in_rides: score_ride(chosen_car, ride_in_rides, bonus))
        chosen_car.add_ride(chosen_ride, bonus)
        rides.remove(chosen_ride)

    dump_rides(file + ".out", cars)

    score = 0
    for car in cars:
        for ride in car.rides:
            score += ride.score

    global_score += score
    print("Score for file {} -->\t\t{}".format(filename, score))


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

        print("\nGlobal score is {}".format(special_print(global_score)))

