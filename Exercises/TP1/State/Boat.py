class Boat:
    def __init__(self, n_missionaries1, n_cannibals1, n_missionaries2, n_cannibals2,
                 n_missionaries_boat, n_cannibals_boat, boat, parent=None):
        self.boat = boat
        self.n_missionaries_boat = n_missionaries_boat
        self.n_cannibals2 = n_cannibals2
        self.n_missionaries2 = n_missionaries2
        self.n_cannibals_boat = n_cannibals_boat
        self.n_cannibals1 = n_cannibals1
        self.n_missionaries1 = n_missionaries1
        self.parent = parent

    def transport(self, n_missionaries, n_cannibals):
        if (n_cannibals + n_missionaries) == 0:
            return Boat(self.n_missionaries1 + self.n_missionaries_boat - n_missionaries,
                        self.n_cannibals1 + self.n_cannibals_boat - n_cannibals,
                        self.n_missionaries2, self.n_cannibals2,
                        n_missionaries, n_cannibals, 0)
        if self.boat == 1:
            return Boat(self.n_missionaries1 + self.n_missionaries_boat - n_missionaries,
                        self.n_cannibals1 + self.n_cannibals_boat - n_cannibals,
                        self.n_missionaries2, self.n_cannibals2,
                        n_missionaries, n_cannibals, 2)