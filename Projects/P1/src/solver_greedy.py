import sys

from Projects.P1.src.files import parse_input, dump_rides
from Projects.P1.src.objects.Car import Car


def score_ride(car_to_score, ride_to_score, bonus_to_score):
    drive_distance = ride_to_score.start_position.distance(ride_to_score.destination_position)
    pick_distance = car_to_score.position.distance(ride_to_score.start_position)
    wait_time = max(0, ride_to_score.earliest - (car_to_score.current_t + pick_distance))
    on_time = pick_distance + car_to_score.current_t <= ride_to_score.earliest

    return drive_distance - pick_distance - wait_time + (bonus_to_score if on_time else 0)


if __name__ == '__main__':
    file = "../assets/input/" + sys.argv[1]
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

    print("Score for file {} -->\t{}".format(sys.argv[1], score))

