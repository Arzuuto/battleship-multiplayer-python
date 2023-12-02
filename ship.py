class Ship:
    def __init__(self, size, positions):
        self.size = size
        self.positions = positions
        self.hits = 0

    def hit(self):
        self.hits += 1

    def is_sunk(self):
        return self.hits == self.size
