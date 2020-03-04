class Board:
    def __init__(self, board, size, parent=None):
        self.size = size
        self.board = board
        self.parent = parent

    def empty_space(self):
        pos = 0
        for piece in self.board:
            if piece == 0:
                return pos
            pos += 1

        return None

    def move(self, direction):
        board = self.board
        if direction == "UP" and self.empty_space() < self.size * (self.size - 1):
            empty_space = self.empty_space()
            board[empty_space] = board[empty_space + self.size]
            board[empty_space + self.size] = 0
            return Board(board, self.size, self)
        if direction == "DOWN" and self.empty_space() > self.size:
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

    def __eq__(self, other):
        return self.size == other.size and self.board == other.board
