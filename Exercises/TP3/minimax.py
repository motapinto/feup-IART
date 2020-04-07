NUM_CHILDREN = 2


def minimax_no_pruning(depth, node_index, max_turn, values):

    if depth == 0:
        return values[node_index]

    if max_turn:
        max_eval = -100  # (-infinity)
        for i in range(0, NUM_CHILDREN):
            child_eval = minimax_no_pruning(depth - 1, node_index * NUM_CHILDREN + i, False, values)
            max_eval = max(max_eval, child_eval)

        return max_eval

    else:
        min_eval = 100  # (+infinity)
        for i in range(0, 2):
            child_eval = minimax_no_pruning(depth - 1, node_index * NUM_CHILDREN + i, True, values)
            min_eval = min(min_eval, child_eval)

        return min_eval


def minimax_alfa_beta(depth, node_index, max_turn, values, alpha, beta):

    if depth == 0:
        return values[node_index]

    if max_turn:
        max_eval = -100  # (-infinity)
        for i in range(0, 2):
            child_eval = minimax_alfa_beta(depth - 1, node_index * NUM_CHILDREN + i, False, values, alpha, beta)
            max_eval = max(max_eval, child_eval)
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break

        return max_eval

    else:
        min_eval = 100  # (+infinity)
        for i in range(0, 2):
            child_eval = minimax_alfa_beta(depth - 1, node_index * NUM_CHILDREN + i, True, values, alpha, beta)
            min_eval = min(min_eval, child_eval)
            beta = min(beta, min_eval)
            if beta <= alpha:
                break

        return min_eval


if __name__ == '__main__':
    values = [-1, 3, 5, 2, -6, -4, 1, 2]

    print("minimax_no_pruning: ", end="")
    print(minimax_no_pruning(3, 0, True, values))
    print("minimax_alfa_beta: ", end="")
    print(minimax_alfa_beta(3, 0, True, values, -100, 100))
