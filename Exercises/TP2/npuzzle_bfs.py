import random
import time

class State:
    def __init__(self, nsize):
        # size: N-Puzzle size
        # tsize: size of total nodes
        # goal: [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.nsize = nsize
        self.tsize = pow(self.nsize, 2)
        self.goal = list(range(0, self.tsize))
        self.visited = []

    def print_puzzle(self, st):
        for (index, value) in enumerate(st):
            print(' %s ' % value, end=' ')
            if index in [x for x in range(self.nsize - 1, self.tsize,
                                          self.nsize)]:
                print()
        print()

    def move(self, puzzle, direction):
        zero_position = puzzle.index(0)

        if direction == "UP":
            puzzle[zero_position] = puzzle[zero_position - self.nsize]
            puzzle[zero_position - self.nsize] = 0

        elif direction == "DOWN":
            puzzle[zero_position] = puzzle[zero_position + self.nsize]
            puzzle[zero_position + self.nsize] = 0

        elif direction == "LEFT":
            zero_position = puzzle.index(0)
            puzzle[zero_position] = puzzle[zero_position - 1]
            puzzle[zero_position - 1] = 0

        elif direction == "RIGHT":
            puzzle[zero_position] = puzzle[zero_position + 1]
            puzzle[zero_position + 1] = 0

        return puzzle

    def possible_states(self, puzzle):
        potential_states = []

        if puzzle.index(0) >= self.nsize and self.move(puzzle.copy(), "UP") not in self.visited:
            up = self.move(puzzle.copy(), "UP")
            potential_states.append(up)
            self.visited.append(up)

        if puzzle.index(0) < self.nsize*self.nsize - self.nsize and self.move(puzzle.copy(), "DOWN") not in self.visited:
            down = self.move(puzzle.copy(), "DOWN")
            potential_states.append(down)
            self.visited.append(down)

        if puzzle.index(0) % self.nsize != 0 and self.move(puzzle.copy(), "LEFT") not in self.visited:
            left = self.move(puzzle.copy(), "LEFT")
            potential_states.append(left)
            self.visited.append(left)

        if puzzle.index(0) % self.nsize != self.nsize - 1 and self.move(puzzle.copy(), "RIGHT") not in self.visited:
            right = self.move(puzzle.copy(), "RIGHT")
            potential_states.append(right)
            self.visited.append(right)

        return potential_states

    """ Calculate the Manhattan Distances of the particular State. """
    def manhattan_distance(self, puzzle):
        manhattan_dist = 0

        # Manhattan distances are calculated as Total number of Horizontal and Vertical moves required by the values in the current state to reach their position in the Goal State.
        for number in puzzle:
            if number != 0:
                # delta: delta between number and goal position
                delta = abs(self.goal.index(number) - puzzle.index(number))
                # distance related to goal position in x and y
                (delta_x, delta_y) = (delta // self.nsize, delta % self.nsize)
                manhattan_dist += delta_x + delta_y

        return manhattan_dist

    """ Determines the next state to follow and uses Mahattan distances method as the huristics. """
    def heuristic_next_state(self, puzzle):
        potential_states = self.possible_states(puzzle.copy())
        manhattan_dist_values = []

        for state in potential_states:
            manhattan_dist_values.append(self.manhattan_distance(state))

        shortest_path = min(manhattan_dist_values)

       # If more than one path have same manhattan distance, then a random choice of one of them is analyzed and carried forward """
        if manhattan_dist_values.count(shortest_path) > 1:
            min_paths = [state for state in potential_states if self.manhattan_distance(state) == shortest_path]
            return random.choice(min_paths)

        # Chooses the state with that has the minimum manhattan distance
        else:
            for state in potential_states:
                if self.manhattan_distance(state) == shortest_path:
                    return state

    """ Determines best next state based on heuristic until it has reached the goal"""
    def solve(self, puzzle):
        while not puzzle == self.goal:
            puzzle = self.heuristic_next_state(puzzle.copy())
            self.print_puzzle(puzzle)

if __name__ == '__main__':
    print('N-Puzzle Solver!')
    print(23 * '-')
    st = State(3)

    print('The Starting State is:')
    start = [5, 0, 2, 1, 4, 3, 6, 7, 8]
    st.print_puzzle(start)

    print('The Goal State should be:')
    st.print_puzzle(st.goal)

    print('Here it Goes:')
    st.print_puzzle(start)
    start_time = time.time()
    st.solve(start)
    end_time = time.time()
    print("Time: ")
    print(end_time - start_time)
