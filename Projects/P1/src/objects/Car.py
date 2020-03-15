class Car(object):
    def __init__(self, number) -> None:
        super().__init__()
        self.number = int(number)
        self.position = (0, 0)
        self.rides = []
        self.current_t = 0

