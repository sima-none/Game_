import pygame
from config import GRID_SIZE, CELL_SIZE

class Grid:
    def __init__(self):
        self.size = GRID_SIZE
        self.grid = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def update_grid(self):
        new_grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                live_neighbors = sum(self.grid[x][y] 
                                     for x in range(i - 1, i + 2) 
                                     for y in range(j - 1, j + 2) 
                                     if 0 <= x < self.size and 0 <= y < self.size) - self.grid[i][j]
                if self.grid[i][j] == 1:
                    new_grid[i][j] = 1 if 2 <= live_neighbors <= 3 else 0
                else:
                    new_grid[i][j] = 1 if live_neighbors == 3 else 0
        self.grid = new_grid

    def draw(self, screen):
        screen.fill((50, 0, 0))
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(screen, (200, 200, 0), (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()