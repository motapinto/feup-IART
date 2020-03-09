from board import Board


class Board(object):
    def __init__(self, board, size, parent=None):
        self.size = size
        self.board = board
        self.parent = parent

        h1 = 0
        h2 = self.depth()
        for i in range(8):
            if self.board[i] != 0 and self.board[i] != i + 1:
                current_position = self.board.index(i + 1)
                # h1 += 1
                h1 += abs(i % self.size - current_position % self.size) + abs(
                    i // self.size - current_position // self.size)

        self.h1_and_h2 = h1 + h2

    def empty_space(self):
        return self.board.index(0)

    def move(self, direction):
        board = []
        for piece in self.board:
            board.append(piece)

        if direction == "UP" and self.empty_space() < self.size * (self.size - 1):
            empty_space = self.empty_space()
            board[empty_space] = board[empty_space + self.size]
            board[empty_space + self.size] = 0
            return Board(board, self.size, self)
        if direction == "DOWN" and self.empty_space() >= self.size:
            empty_space = self.empty_space()
            board[empty_space] = board[empty_space - self.size]
            board[empty_space - self.size] = 0
            return Board(board, self.size, self)
        if direction == "LEFT" and self.empty_space() % self.size < self.size - 1:
            empty_space = self.empty_space()
            board[empty_space] = board[empty_space + 1]
            board[empty_space + 1] = 0
            return Board(board, self.size, self)
        if direction == "RIGHT" and self.empty_space() % self.size > 0:
            empty_space = self.empty_space()
            board[empty_space] = board[empty_space - 1]
            board[empty_space - 1] = 0
            return Board(board, self.size, self)

    def depth(self):
        depth = 0
        state = self
        while state is not None:
            state = state.parent
            depth += 1

        return depth

    def __eq__(self, o: Board) -> bool:
        if o is None:
            return False

        return self.size == o.size and self.board == o.board
