from Exercises.TP1.State.Boat import Boat

if __name__ == '__main__':
    state = Boat(3, 3, 0, 0, 1)
    potential_states = [state]
    visited_states = []
    depth = 1

    while not state == Boat(0, 0, 3, 3, 2):
        state = potential_states.pop(0)

        if state.depth() > depth:
            state = Boat(3, 3, 0, 0, 1)
            potential_states = [state]
            visited_states = []
            depth += 1
            continue

        if state in visited_states:
            continue

        if state.boat == 1:
            if state.n_missionaries1 > 0 and (state.n_cannibals1 < state.n_missionaries1 or state.n_missionaries1 == 1)\
                    and state.n_cannibals2 <= state.n_missionaries2 + 1:
                potential_states.append(state.transport(1, 0))
            if state.n_missionaries1 > 1 and (state.n_cannibals1 <= state.n_missionaries1 - 2
                                              or state.n_missionaries1 == 2) \
                    and state.n_cannibals2 <= state.n_missionaries2 + 2:
                potential_states.append(state.transport(2, 0))
            if state.n_cannibals1 >= 1 and (state.n_cannibals2 + 1 <= state.n_missionaries2
                                            or state.n_missionaries2 == 0):
                potential_states.append(state.transport(0, 1))
            if state.n_cannibals1 >= 2 and (state.n_cannibals2 + 2 <= state.n_missionaries2
                                            or state.n_missionaries2 == 0):
                potential_states.append(state.transport(0, 2))
            if state.n_cannibals1 > 0 and state.n_missionaries1 > 0 and state.n_missionaries2 == state.n_cannibals2:
                potential_states.append(state.transport(1, 1))

        elif state.boat == 2:
            if state.n_missionaries2 > 0 and (state.n_cannibals2 < state.n_missionaries2 or state.n_missionaries2 == 1)\
                    and state.n_cannibals1 <= state.n_missionaries1 + 1:
                potential_states.append(state.transport(1, 0))
            if state.n_missionaries2 > 1 and (state.n_cannibals2 <= state.n_missionaries2 - 2 or
                                              state.n_missionaries2 == 2) \
                    and state.n_cannibals1 <= state.n_missionaries1 + 2:
                potential_states.append(state.transport(2, 0))
            if state.n_cannibals2 >= 1 and (state.n_cannibals1 + 1 <= state.n_missionaries1
                                            or state.n_missionaries1 == 0):
                potential_states.append(state.transport(0, 1))
            if state.n_cannibals2 >= 2 and (state.n_cannibals1 + 2 <= state.n_missionaries1
                                            or state.n_missionaries1 == 0):
                potential_states.append(state.transport(0, 2))
            if state.n_cannibals2 > 0 and state.n_missionaries2 > 0  and state.n_missionaries1 == state.n_cannibals1:
                potential_states.append(state.transport(1, 1))

        visited_states.append(state)

    output = []
    while state is not None:
        output.append(state)
        state = state.parent

    while len(output) > 0:
        state = output.pop()
        print("Missionaries in 1: ", state.n_missionaries1, "\tCannibals in 1: ", state.n_cannibals1,
              "\tMissionaries in 2: ", state.n_missionaries2, "\tCannibals in 2: ", state.n_cannibals2,
              "\tBoat in: ", state.boat)

    print("Depth: ", depth)
