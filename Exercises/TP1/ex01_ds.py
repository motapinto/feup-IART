from State.State import State

if __name__ == '__main__':
    state = State(0, 0, 4, 3)
    potential_states = [state]
    visited_states = []
    depth = 1

    while not state == State(2, 0, 4, 3):
        state = potential_states.pop(0)

        if state.depth() > depth:
            state = State(0, 0, 4, 3)
            potential_states = [state]
            visited_states = []
            depth += 1
            continue

        if state in visited_states:
            continue

        if state.bucket1 < state.max_bucket1:
            potential_states.append(state.fill(1))
        if state.bucket2 < state.max_bucket2:
            potential_states.append(state.fill(2))
        if state.bucket1 > 0:
            potential_states.append(state.empty(1))
        if state.bucket2 > 0:
            potential_states.append(state.empty(2))
        if state.bucket2 < state.max_bucket2 and state.bucket1 >= (state.max_bucket2 - state.bucket2):
            potential_states.append(state.pour(1))
        if state.bucket2 < state.max_bucket2 and state.bucket1 < (state.max_bucket2 - state.bucket2):
            potential_states.append(state.pour(1))
        if state.bucket1 < state.max_bucket1 and state.bucket2 >= (state.max_bucket1 - state.bucket1):
            potential_states.append(state.pour(2))
        if state.bucket1 < state.max_bucket1 and state.bucket2 < (state.max_bucket1 - state.bucket1):
            potential_states.append(state.pour(2))

        visited_states.append(state)

    output = []
    while state is not None:
        output.append(state)
        state = state.parent

    while len(output) > 0:
        state = output.pop()
        print("Bucket1: ", state.bucket1, " Bucket 2: ", state.bucket2)

    print("Depth: ", depth)
