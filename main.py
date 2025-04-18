import pygame
from config import WIDTH, HEIGHT, TICK_RATE
from core.grid import Grid
from entities.character import Character
from core.automaton import Automaton
import random

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Создание сетки
grid = Grid()

# Создание персонажей
characters = [
    Character(grid, random.randint(10, grid.size - 10), random.randint(10, grid.size - 10)) for _ in range(10)
]

# Запуск автомата
automaton = Automaton(grid, characters)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid.draw(screen)
    automaton.step()
    clock.tick(TICK_RATE)

pygame.quit()
