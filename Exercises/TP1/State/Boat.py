class Boat:
    def __init__(self, n_missionaries1, n_cannibals1, n_missionaries2, n_cannibals2, boat, parent=None):
        self.boat = boat
        self.n_cannibals2 = n_cannibals2
        self.n_missionaries2 = n_missionaries2
        self.n_cannibals1 = n_cannibals1
        self.n_missionaries1 = n_missionaries1
        self.parent = parent

    def transport(self, n_missionaries, n_cannibals):
        if abs(n_missionaries) + abs(n_cannibals) > 2 or abs(n_missionaries) + abs(n_cannibals) == 0:
            return None

        if self.boat == 1:
            return Boat(self.n_missionaries1 - n_missionaries, self.n_cannibals1 - n_cannibals,
                        self.n_missionaries2 + n_missionaries, self.n_cannibals2 + n_cannibals, 2, self)
        if self.boat == 2:
            return Boat(self.n_missionaries1 + n_missionaries, self.n_cannibals1 + n_cannibals,
                        self.n_missionaries2 - n_missionaries, self.n_cannibals2 - n_cannibals, 1, self)
        return None

    def depth(self):
        depth = 0
        state = self
        while state is not None:
            state = state.parent
            depth += 1

        return depth

    def __eq__(self, other):
        return self.boat == other.boat and self.n_cannibals2 == other.n_cannibals2 \
            and self.n_missionaries2 == other.n_missionaries2 and self.n_cannibals1 == other.n_cannibals1 \
            and self.n_missionaries1 == other.n_missionaries1
