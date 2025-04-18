import random

class Character:
    def __init__(self, grid, x, y, pattern=None):
        self.grid = grid
        self.x = x
        self.y = y
        self.pattern = pattern if pattern else self.random_pattern()

    def random_pattern(self):
        return [[random.randint(0, 1) for _ in range(3)] for _ in range(3)]

    def place_on_grid(self):
        for i in range(len(self.pattern)):
            for j in range(len(self.pattern[i])):
                if 0 <= self.x + i < self.grid.size and 0 <= self.y + j < self.grid.size:
                    self.grid.grid[self.x + i][self.y + j] = self.pattern[i][j]
