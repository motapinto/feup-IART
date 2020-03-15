import sys

from Projects.P1.src.files import parse_input, dump_rides
from Projects.P1.src.objects.Car import Car

if __name__ == '__main__':
    rides, rows, cols, n_vehicles, bonus, t = parse_input(sys.argv[1])
    cars = [Car(i + 1) for i in range(n_vehicles)]



