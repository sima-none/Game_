import pygame
import random

# Размеры сетки
GRID_SIZE = 100  # Увеличено поле
CELL_SIZE = 8  # Размер клетки в пикселях
WIDTH, HEIGHT = GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def update_grid(self):
        """Обновляет сетку по правилам клеточного автомата."""
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
        """Рисует сетку на экране."""
        screen.fill((50, 0, 0))  # Фон — черный
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(screen, (200, 200, 0), (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()

class Character:
    def __init__(self, grid, x, y, pattern=None):
        """Персонаж состоит из набора живых клеток в заданной позиции."""
        self.grid = grid
        self.x = x
        self.y = y
        self.pattern = pattern if pattern else self.random_pattern()

    def random_pattern(self):
        """Генерирует случайную форму персонажа (матрицу 3x3)."""
        return [[random.randint(0, 1) for _ in range(3)] for _ in range(3)]

    def place_on_grid(self):
        """Размещает персонажа на сетке."""
        for i in range(len(self.pattern)):
            for j in range(len(self.pattern[i])):
                if 0 <= self.x + i < self.grid.size and 0 <= self.y + j < self.grid.size:
                    self.grid.grid[self.x + i][self.y + j] = self.pattern[i][j]

class Automaton:
    def __init__(self, grid, characters):
        self.grid = grid
        self.characters = characters
        self.place_characters()

    def place_characters(self):
        """Размещает всех персонажей на поле."""
        for char in self.characters:
            char.place_on_grid()

    def step(self):
        """Шаг симуляции"""
        self.grid.update_grid()

# Создание сетки
grid = Grid(GRID_SIZE)

# Создание персонажей
characters = [
    Character(grid, random.randint(10, GRID_SIZE - 10), random.randint(10, GRID_SIZE - 10)) for _ in range(10)
]

automaton = Automaton(grid, characters)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid.draw(screen)
    automaton.step()
    clock.tick(10)  # Скорость обновления (10 кадров в секунду)

pygame.quit()
