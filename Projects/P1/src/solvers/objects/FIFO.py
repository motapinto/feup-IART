class FIFO:
    def __init__(self, l):
        self.pile = [-1]*l

    def put(self, n):
        for i in range(len(self.pile) - 1):
            self.pile[len(self.pile) - 1 - i] = self.pile[len(self.pile) - 2 - i]
        self.pile[0] = n

    def is_constant(self):
        for i in range(len(self.pile) - 1):
            if self.pile[i] != self.pile[i+1]:
                return False
        return True
