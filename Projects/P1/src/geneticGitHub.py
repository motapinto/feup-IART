POPULATION_SIZE = 8000
POOLING_SIZE = 2000
CONSTANT_GENERATION_NUMBER = 5
MUTATION_RATE = 0.01

# 1st file instant - 12
# 2nd 2/3 min - 175798


import random as rd

global_score = 0


class Ride:
    def __init__(self, values, id):
        self.a = values[0]
        self.b = values[1]
        self.x = values[2]
        self.y = values[3]
        self.d = abs(self.a-self.x) + abs(self.b-self.y)
        self.s = values[4]
        self.f = values[5]
        self.ls = self.f - self.d  # last start
        self.id = id


class Car:
    B = 0  # per ride bonus for starting the ride on time
    F = 0  # number of vehicles in fleet
    N = 0  # number of pre bocked rides

    RPC = 0  # Rides per car
    RIDES = []

    def __init__(self, rides = []):
        self.pos = [0,0]
        self.t = 0
        self.fitness = 0
        if rides == []:
            self.rides = rd.sample(Car.RIDES,Car.RPC)
        else:
            self.rides = rides

    def sort_rides(self):
        #I've also used ride.ls and ride.s individually for sorting, giving different results in function of the input files
        self.rides.sort(key = lambda ride: ride.ls + ride.s)

    def calculate_fitness(self):
        self.pos = [0,0]
        self.t = 0
        self.fitness = 0
        self.sort_rides
        for ride in self.rides:
            self.t += abs(self.pos[0] - ride.a) + abs(self.pos[1] - ride.b)
            self.pos = [ride.a, ride.b]
            if self.t <= ride.s:
                self.fitness += Car.B
                self.t = ride.s
            self.t += abs(self.pos[0] - ride.x) + abs(self.pos[1] - ride.y)
            self.pos = [ride.x, ride.y]
            if self.t <= ride.f:
                self.fitness += ride.d

    def reproduce(self,parent):
        self.sort_rides()
        parent.sort_rides()

        childs = []
        i = rd.randint(0,Car.RPC)
        childs.append(Car(self.rides[0:i] + parent.rides[i:Car.RPC]))
        childs.append(Car(parent.rides[0:i] + self.rides[i:Car.RPC]))
        return childs

    def mutate(self):
        for ride in self.rides:
            if rd.random() < MUTATION_RATE:
                ride = rd.choice(Car.RIDES)

    def normalize(self):
        self.rides = list(set(self.rides))
        self.sort_rides()


class FIFO:
    def __init__(self,l):
        self.pile = [-1]*l

    def put(self,n):
        for i in range(len(self.pile) - 1):
            self.pile[len(self.pile) - 1 - i] = self.pile[len(self.pile) - 2 - i]
        self.pile[0] = n

    def is_constant(self):
        for i in range(len(self.pile) - 1):
            if self.pile[i] != self.pile[i+1]:
                return False
        return True


def cars_to_file(cars, file_name):
    global global_score
    #output = open(file_name + ".out", "w")
    for car in cars:
        global_score += car.B
        car_line = str(len(car.rides))
        for ride in car.rides:
            global_score += ride.d
            car_line += " " + str(ride.id)
        car_line += "\n"
        #output.write(car_line)


def hash_code(file_name):
    #Parsing
    input = open("../assets/input/" + file_name + ".in","r")
    R,C,F,N,B,T = [int(i) for i in input.readline().split()]
    Car.B, Car.F, Car.N = B,F,N
    Car.RPC = N//F
    rides = []
    for i in range(N):
        rides.append(Ride([int(i) for i in input.readline().split()],i))
    Car.RIDES = rides

    cars = []
    for n_car in range(F-1): # The last car is a special case
        population = [Car() for i in range(POPULATION_SIZE)]
        generation = 1
        max_fitness_car = population[0]
        fitness_pile = FIFO(CONSTANT_GENERATION_NUMBER)
        fitness_pile.put(max_fitness_car.fitness)
        print(file_name + ": Car " + str(n_car + 1) + " -- generation " + str(generation) + " -- max fitness (" + str(max_fitness_car.fitness)+")")

        while not fitness_pile.is_constant():
            for car in population:
                car.calculate_fitness()
            population.sort(key=lambda car: car.fitness)
            population.reverse()
            if population[0].fitness > max_fitness_car.fitness:
                max_fitness_car = population[0]
            fitness_pile.put(max_fitness_car.fitness)
            print(fitness_pile.is_constant())

            new_population = []
            while len(new_population) < POPULATION_SIZE:
                i = rd.randint(0, POOLING_SIZE - 1)
                j = rd.randint(0, POOLING_SIZE - 1)
                childs = population[i].reproduce(population[j])
                childs[0].mutate()
                childs[1].mutate()
                new_population.append(childs[0])
                new_population.append(childs[1])
            population = new_population

            generation += 1
            print(file_name + ": Car " + str(n_car + 1) + " -- generation " + str(generation)+ " -- max fitness (" + str(max_fitness_car.fitness)+")")

        max_fitness_car.normalize()
        cars.append(max_fitness_car)
        for ride in max_fitness_car.rides:
            Car.RIDES.remove(ride)

    last_car = Car(Car.RIDES)
    last_car.normalize
    cars.append(last_car)

    cars_to_file(cars, file_name)


if __name__ == '__main__':
    #hash_code("a_example")
    hash_code("b_should_be_easy")
    #hash_code("../assets/input/c_no_hurry")
    #hash_code("../assets/input/d_metropolis")
    #hash_code("../assets/input/e_high_bonus")
    print(global_score)