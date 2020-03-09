import time

from Exercises.TP2.classes.Board import Board


if __name__ == '__main__':
    # state = Board([5, 1, 3, 4, 2, 0, 7, 8, 10, 6, 11, 12, 9, 13, 14, 15], 4)
    # state = Board([1, 6, 2, 5, 7, 3, 0, 4, 8], 3)
    # state = Board([1, 3, 6, 5, 2, 0, 4, 7, 8], 3)
    state = Board([5, 0, 2, 1, 4, 3, 6, 7, 8], 3)
    potential_states = [state]
    visited_states = []
    max_depth = 2

    start = time.time()

    # while not state == Board([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0], 4):
    while not state == Board([1, 2, 3, 4, 5, 6, 7, 8, 0], 3):
        state = potential_states.pop(0)

        if state in visited_states:
            continue

        if state.empty_space() < state.size * (state.size - 1):
            new_state = state.move("UP")
            inserted = False
            for i in range(len(potential_states)):
                if new_state.h1_and_h2 < potential_states[i].h1_and_h2:
                    potential_states.insert(i, new_state)
                    inserted = True
                    break
            if not inserted:
                potential_states.append(new_state)

        if state.empty_space() >= state.size:
            new_state = state.move("DOWN")
            inserted = False
            for i in range(len(potential_states)):
                if new_state.h1_and_h2 < potential_states[i].h1_and_h2:
                    potential_states.insert(i, new_state)
                    inserted = True
                    break
            if not inserted:
                potential_states.append(new_state)
        if state.empty_space() % state.size < state.size - 1:
            new_state = state.move("LEFT")
            inserted = False
            for i in range(len(potential_states)):
                if new_state.h1_and_h2 < potential_states[i].h1_and_h2:
                    potential_states.insert(i, new_state)
                    inserted = True
                    break
            if not inserted:
                potential_states.append(new_state)

        if state.empty_space() % state.size > 0:
            new_state = state.move("RIGHT")
            inserted = False
            for i in range(len(potential_states)):
                if new_state.h1_and_h2 < potential_states[i].h1_and_h2:
                    potential_states.insert(i, new_state)
                    inserted = True
                    break
            if not inserted:
                potential_states.append(new_state)

        visited_states.append(state)

    output = []
    while state is not None:
        output.append(state)
        state = state.parent

    while len(output) > 0:
        state = output.pop()
        # size = 0
        print("Board: ", state.board)

    print(time.time() - start)
