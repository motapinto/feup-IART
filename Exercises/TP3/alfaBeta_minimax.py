

def minimax(cur_depth, node_index, max_turn, values, targetDepth):
    if cur_depth == targetDepth:
        return values[node_index]

    if max_turn:
        return max(
            # First child
            minimax(cur_depth + 1, node_index * 3, False, values, targetDepth),
            # Second child
            minimax(cur_depth + 1, node_index * 3 + 1, False, values, targetDepth),
            # Third child
            minimax(cur_depth + 1, node_index * 3 + 2, False, values, targetDepth)
        )

    else:
        return min(
            # First child
            minimax(cur_depth + 1, node_index * 3, True, values, targetDepth),
            # Second child
            minimax(cur_depth + 1, node_index * 3 + 1, True, values, targetDepth),
            # Third child
            minimax(cur_depth + 1, node_index * 3 + 2, True, values, targetDepth)
        )


if __name__ == '__main__':
    values = [
                3, 10, 5,
                12, 0, 4,
                6, 20, 8,
                1, 2, 6, 8,
                15, 0, 5, 2,
                3, 10, 20, 7,
                20, 30, 40,
                0, 0, 0
            ]

    print("The optimal value is : ", end="")
    print(minimax(0, 0, True, values, 3))
