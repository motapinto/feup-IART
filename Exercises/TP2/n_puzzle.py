from Exercises.TP2.classes.Board import Board

if __name__ == '__main__':
    state = Board([1, 3, 6, 5, 2, 0, 4, 7, 8], 3)
    potential_states = [state]
    visited_states = []

    while not state == Board([1, 2, 3, 4, 5, 6, 7, 8, 0], 3):
        state = potential_states.pop()

        if state in visited_states:
            continue

        if state.empty_space() < state.size * (state.size - 1):
            potential_states.append(state.move("UP"))
        if state.empty_space() < state.empty_space() >= state.size:
            potential_states.append(state.move("DOWN"))
        if state.empty_space() < state.empty_space() % state.size < state.size - 1:
            potential_states.append(state.move("LEFT"))
        if state.empty_space() < state.empty_space() % state.size > 0:
            potential_states.append(state.move("RIGHT"))

        visited_states.append(state)

    output = []
    while state is not None:
        output.append(state)
        state = state.parent

    while len(output) > 0:
        state = output.pop()
        size = 0
        print("Board: ")
        for piece in state.board:
            if size % state.size + 1 == state.size:
                print("\n")
            if piece == 0:
                print("  ")
            else:
                print(piece, " ")
            size += 1
