import math
from itertools import combinations, permutations, product
import numpy as np
import random


class Class(object):
    def __init__(self, id, students_assigned):
        self.id = id
        self.students_assigned = students_assigned

    def calculate_incompatibilities(self, other_class):
        num_incompatibilities = 0
        for student in self.students_assigned:
            if student in other_class.students_assigned:
                num_incompatibilities += 1

        return num_incompatibilities


class Schedule(object):
    def __init__(self, schedules, slots, initial_solution):
        self.schedules = schedules
        self.slots = slots
        self.initial_solution = initial_solution

        self.evaluation = 0
        self.evaluation_solution(self.initial_solution)

    def evaluation_solution(self, initial_solution):
        processed = []
        values = np.array(initial_solution)
        num_incompatibilities = 0

        for i in range(0, len(values)):
            val = values[i]
            if val in processed:
                continue

            # gets all the same values in array and deletes the number of the current iteration
            equal_vals = np.delete(np.where(values == val)[0], 0, 0)

            # evaluates all schedules and calculates evaluation function based on the number of incompatibilities
            for equal_val in equal_vals:
                num_incompatibilities += self.schedules[val].calculate_incompatibilities(self.schedules[equal_val])

            processed.append(val)

        return -num_incompatibilities

    # takes a while...
    def get_best_sol(self):
        array = list(range(1, self.slots + 1))
        ll = [p for p in product(array, repeat=9)]
        solution = max(ll, key=lambda l: self.evaluation_solution(l))
        print("best solution: ", end="")
        print(solution)
        print("num incompatibilities: " + str(self.evaluation_solution(solution)))

    # gets stuck on local maximums
    def hill_climbing_random(self):
        while True:
            neighbours = self.get_neighbours()
            new_sol = random.choice(neighbours)
            if self.evaluation_solution(new_sol) > self.evaluation_solution(self.initial_solution):
                self.initial_solution = new_sol
            else:
                break

        print(self.initial_solution)
        return self.evaluation_solution(self.initial_solution)

    def simulated_annealing(self):
        # if we start with a high temperature high the probability below will be almost one
        temperature = len(self.initial_solution)

        while temperature >= 1:
            # random successor (alternative is to do: foreach successor)
            # value = random.randint(1, self.slots)
            # index = random.randint(0, len(self.initial_solution) - 1)
            # new_sol = self.initial_solution.copy()
            # new_sol[index] = value
            neighbours = self.get_neighbours()
            new_sol = random.choice(neighbours)

            if self.evaluation_solution(new_sol) > self.evaluation_solution(self.initial_solution):
                self.initial_solution = new_sol
            else:
                # probability = math.exp(-(loss / temperature))
                # loss is simply a measure of how much worse the neighbour is from the current state
                # with a higher loss we will have a worse probability of taking that state
                # the higher the temperature the greater the probability of taking that state
                loss = self.evaluation_solution(self.initial_solution) - self.evaluation_solution(new_sol)
                probability = math.exp(- (loss / temperature))

                if random.random() <= probability:
                    # we choose a worst neighbour to escape local maximums
                    self.initial_solution = new_sol

            temperature = random.uniform(0.9, 0.99) * temperature

        print(self.initial_solution)
        return self.evaluation_solution(self.initial_solution)

    # neighbourhood is considered as follows:
    #   for each value on self.initial_solution increments n and decreases n n(1-4)
    #   creating a neighbourhood of 8 elements
    def get_neighbours(self):
        neighbours = []

        for j in range(self.slots):
            neighbour1 = []
            neighbour2 = []
            for i in range(len(self.initial_solution)):
                neighbour1.append(self.initial_solution[i] % self.slots + j)
                neighbour2.append((self.initial_solution[i] - (1 + j)) % self.slots + j)

            neighbours.append(neighbour1)
            neighbours.append(neighbour2)

        return neighbours


if __name__ == '__main__':
    classes = []
    classes.append(Class(1, [1, 2, 3, 4, 5]))
    classes.append(Class(2, [6, 7, 8, 9]))
    classes.append(Class(3, [10, 11, 12]))
    classes.append(Class(4, [1, 2, 3, 4]))
    classes.append(Class(5, [5, 6, 7, 8]))
    classes.append(Class(6, [9, 10, 11, 12]))
    classes.append(Class(7, [1, 2, 3, 5]))
    classes.append(Class(8, [6, 7, 8]))
    classes.append(Class(9, [4, 9, 10, 11, 12]))
    classes.append(Class(10, [1, 2, 4, 5]))
    classes.append(Class(11, [3, 6, 7, 8]))
    classes.append(Class(12, [9, 10, 11, 12]))

    slots = 4
    # initial_sol = [4, 1, 2, 3, 2, 4, 1, 1, 2, 1, 2, 3]
    initial_sol = []
    for i in range(12):
        initial_sol.append(random.randint(1, slots))

    schedule = Schedule(classes, slots, initial_sol)




    # print(schedule.schedules[0].calculate_incompatibilities(schedule.schedules[6]))
    # print(abs(schedule.evaluation_solution(schedule.initial_solution)))
    print("hill climbing:")
    print("num_incompatibilities: " + str(abs(schedule.hill_climbing_random()))) # hill climbing
    print("\nsimulated annealing:")
    print("num_incompatibilities: " + str(abs(schedule.simulated_annealing()))) # simulted annealing
    # schedule.get_best_sol() # gets best solution
