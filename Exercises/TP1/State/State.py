class State:
    def __init__(self, bucket1, bucket2, max_bucket1, max_bucket2, parent=None):
        self.max_bucket1 = max_bucket1
        self.max_bucket2 = max_bucket2
        self.bucket1 = bucket1
        self.bucket2 = bucket2
        self.parent = parent

    def fill(self, n):
        if n == 1:
            return State(self.max_bucket1, self.bucket2, self.max_bucket1, self.max_bucket2, self)
        elif n == 2:
            return State(self.bucket1, self.max_bucket2, self.max_bucket1, self.max_bucket2, self)

    def empty(self, n):
        if n == 1:
            return State(0, self.bucket2, self.max_bucket1, self.max_bucket2, self)
        elif n == 2:
            return State(self.bucket1, 0, self.max_bucket1, self.max_bucket2, self)

    def pour(self, from_bucket):
        if from_bucket == 1:
            if self.bucket2 == self.max_bucket2:
                return State(self.bucket1, self.bucket2, self.max_bucket1, self.max_bucket2, self)
            elif self.bucket1 >= (self.max_bucket2 - self.bucket2):
                amount = self.max_bucket2 - self.bucket2
                return State(self.bucket1 - amount, self.max_bucket2, self.max_bucket1, self.max_bucket2, self)
            elif self.bucket1 < (self.max_bucket2 - self.bucket2):
                if (self.bucket2 + self.bucket1) > self.max_bucket2:
                    return State(0, self.max_bucket2, self.max_bucket1, self.max_bucket2, self)
                return State(0, self.bucket2 + self.bucket1, self.max_bucket1, self.max_bucket2, self)
        elif from_bucket == 2:
            if self.bucket1 == self.max_bucket1:
                return State(self.bucket1, self.bucket2, self.max_bucket1, self.max_bucket2, self)
            elif self.bucket2 >= (self.max_bucket1 - self.bucket1):
                amount = self.max_bucket1 - self.bucket1
                return State(self.max_bucket1, self.bucket2 - amount, self.max_bucket1, self.max_bucket2, self)
            elif self.bucket2 < (self.max_bucket1 - self.bucket1):
                if (self.bucket1 + self.bucket2) > self.max_bucket1:
                    return State(self.max_bucket1, 0, self.max_bucket1, self.max_bucket2, self)
                return State(self.bucket2 + self.bucket1, 0, self.max_bucket1, self.max_bucket2, self)
        return State(self.bucket1, self.bucket2, self.max_bucket1, self.max_bucket2, self)

    def depth(self):
        depth = 0
        state = self
        while state is not None:
            state = state.parent
            depth += 1

        return depth

    def __eq__(self, other):
        return self.bucket1 == other.bucket1 and self.bucket2 == other.bucket2 and self.max_bucket1 == other.max_bucket1 and self.max_bucket2 == other.max_bucket2
