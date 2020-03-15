from src.objects.Ride import Ride


def parse_input(file):
    rides = []
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            if i == 0:
                rows, cols, n_vehicles, n_rides, bonus, t = line.split(' ')
            else:
                rides.append(Ride(i - 1, *(line.split(' '))))

    return rides, int(rows), int(cols), int(n_vehicles), int(bonus), int(t)


def dump_rides(file, cars):
    with open(file, 'w') as f:
        for c in cars:
            f.write('{} '.format(len(c.rides)))
            for r in c.rides:
                f.write('{} '.format(r.number))
            f.write('\n')
